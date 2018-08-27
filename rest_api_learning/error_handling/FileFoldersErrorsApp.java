package com.spindices.box.integration.rest.errors;

import java.io.FileReader;
import java.io.Reader;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

import com.box.sdk.BoxAPIException;
import com.box.sdk.BoxConfig;
import com.box.sdk.BoxDeveloperEditionAPIConnection;
import com.box.sdk.BoxFile;
import com.box.sdk.BoxLock;
import com.box.sdk.BoxUser;
import com.box.sdk.DeveloperEditionEntityType;
import com.box.sdk.IAccessTokenCache;
import com.box.sdk.InMemoryLRUAccessTokenCache;
import com.fasterxml.jackson.databind.ObjectMapper;


public class FileFoldersErrorsApp {
		
	private static final Logger log = LoggerFactory.getLogger(FileFoldersErrorsApp.class);
	
	public static void main(String[] args) {
		SpringApplication.run(FileFoldersErrorsApp.class, args);
	}
	
	@Bean
	public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
		
		return args -> {
			
			try {
									
				String fileTestPdfInfoId = "301579619254";
				String fileTestDocxInfoId = "302086748622";
				String fileTestXlsxInfoId = "302083656715";
				
				// Read config file into Box Config object
				Resource configFile = new ClassPathResource("key_config.json");
				Reader reader = new FileReader(configFile.getFile());
				BoxConfig boxConfig = BoxConfig.readFrom(reader);
				
				// Set cache info
				int MAX_CACHE_ENTRIES = 100;
				IAccessTokenCache accessTokenCache = new InMemoryLRUAccessTokenCache(MAX_CACHE_ENTRIES);
				
				// CARE APP Create new app enterprise connection object
				BoxDeveloperEditionAPIConnection careAppApiConn =
						BoxDeveloperEditionAPIConnection.getAppEnterpriseConnection(boxConfig, accessTokenCache);
				
				// CARE APP Info
				BoxUser.Info careAppInfo = BoxUser.getCurrentUser(careAppApiConn).getInfo();
				log.info("CARE App Info Name ===> " + careAppInfo.getName());
				
								
				// Get caredevteam@mhf.spglobal.com BoxUser
				String careUserLogin = "caredevteam@mhf.spglobal.com";
				Iterable<BoxUser.Info> users2 = BoxUser.getAllEnterpriseUsers(careAppApiConn, careUserLogin);
				String careUserId = null;
				for(BoxUser.Info user : users2) {
					careUserId = user.getID();
					log.info("CARE User Id ===> " + careUserId);
				}
				
				BoxDeveloperEditionAPIConnection careUserApiConn = new BoxDeveloperEditionAPIConnection(careUserId,
						DeveloperEditionEntityType.USER, boxConfig, accessTokenCache);
				String careUserToken = careUserApiConn.getAccessToken();
				log.info("CARE User Token ===> " + careUserToken);
								
								
				// Lock File that causes the error
				String error = "12";
				BoxFile file = new BoxFile(careUserApiConn, error);
				BoxLock lock = file.lock();
				log.info("Lock File Type ===> " + lock.getType());
				
				
			} catch (BoxAPIException e) {
				// Convert JSON string to Object
				ObjectMapper mapper = new ObjectMapper();
				String json_error = e.getResponse();				
				ErrorResponse error_response = mapper.readValue(json_error, ErrorResponse.class);
				System.out.println(error_response);	
				
							
				// Log the response code and the error message returned by the API.
				log.error("BoxAPIException Code: {} Response: {}", e.getResponseCode(), e.getResponse(), e);

			} catch (Exception e) {
				log.error("Exception ", e);
			}

		};
	}
}


