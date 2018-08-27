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


public class Main {
		
	private static final Logger log = LoggerFactory.getLogger(Main.class);
	
	public static void main(String[] args) {
		SpringApplication.run(Main.class, args);
	}
	
	@Bean
	public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
				
		return args -> {
			
			try {
				
				String fileTestPdfInfoId = "301579619254";
				String fileTestDocxInfoId = "302086748622";
				String fileTestXlsxInfoId = "302083656715";
				String error = "1234";
				
				Resource configFile = new ClassPathResource("key_config.json");
				Reader reader = new FileReader(configFile.getFile());
				BoxConfig boxConfig = BoxConfig.readFrom(reader);
				
				int MAX_CACHE_ENTRIES = 100;
				IAccessTokenCache accessTokenCache = new InMemoryLRUAccessTokenCache(MAX_CACHE_ENTRIES);
				
				BoxDeveloperEditionAPIConnection careAppApiConn =
						BoxDeveloperEditionAPIConnection.getAppEnterpriseConnection(boxConfig, accessTokenCache);
				
				BoxUser.Info careAppInfo = BoxUser.getCurrentUser(careAppApiConn).getInfo();
				log.info("CARE App Info Name ===> " + careAppInfo.getName());
				
								
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
								
				int tries = 3;
				while (tries > 0) 
				{
					tries--;				
					try 
					{
						BoxFile file = new BoxFile(careUserApiConn, error);
						BoxLock lock = file.lock();
						log.info("Lock File Type ===> " + lock.getType());
					} catch (BoxAPIException e) {
						
						log.info("TRY AGAIN");
						
						if (tries == 0) 
						{
							ObjectMapper mapper = new ObjectMapper();
							
							String sample_error_1 = "{\n \"type\": \"error\","
									+ 				"\n  \"status\": 404,\n  "
									+ 					  "\"code\": \"not_found\","
									+ 				"\n  \"context_info\": {\n    "
									+ 										"\"errors\": [\n      {\n       "
									+ 														" \"reason\": \"invalid_parameter\","
									+ 												 "\n        \"name\": \"item\",\n        "
									+ 														"\"message\": \"Invalid value \'f_12\'. \'item\' with value \'f_12\' not found\"\n      }\n    ]\n  },"
									+ 			  "\n  \"help_url\": \"http:\\/\\/developers.box.com\\/docs\\/#errors\",\n  "
									+ 				   "\"message\": \"Not Found\",\n  "
									+ 				"\"request_id\": \"25pzcftc4r2oji5\"\n}";
											
							String sample_error_2 = "{\n    \"type\": \"error\","
								 	+     "\n    \"status\": 404,\n   "
								 	+ "            \"code\": \"not_found\",\n   "
								 	+ "    \"context_info\": {\n      "
								 	+ "                 \"errors\": [\n        {\n      "
								 	+ "                                                \"reason\": \"invalid_parameter\","
								 	+ "\n                                                \"name\": \"item\",\n "
								 	+ "                                               \"message\": \"Invalid value \'f_1234\'. \'item\' with value \'f_1234\' not found\"\n        },"
								 	+ "\n                                 {\n          \"reason\": \"invalid_parameter\","
								 	+ "\n                                                \"name\": \"item\",\n          "
								 	+ "                                               \"message\": \"Invalid value \'f_1234\'. \'item\' with value \'f_1234\' not found\"\n        }\n      ]\n    },"
								 	+ "\n       \"help_url\": \"http:\\/\\/developers.box.com\\/docs\\/#errors\","
								 	+ "\n        \"message\": \"Not Found\","
								 	+ "\n     \"request_id\": \"h6uhr3ftd8fe622d\"\n  }";
							
									
							String sample_error_3 = "{\n    "
									+ 					"\"type\": \"error\","
									+ "\n 			   \"status\": 404,"
									+ "\n  	             \"code\": \"not_found\","
									+ "\n        \"context_info\": {\n  "
									+ "							\"errors\": [\n "
									+ "									{\n"
									+ "                                     \"reason\": \"invalid_parameter\","
									+ "\n 	                                  \"name\": \"item\","
									+ "\n                                  \"message\": \"Invalid value \'f_1234\'. \'item\' with value \'f_1234\' not found\"\n        },"
									+ "\n                         	   {\n"
									+ "								        \"reason\": \"invalid_parameter\","
									+ "\n                                     \"name\": \"item\","
									+ "\n                                  \"message\": \"Invalid value \'f_12346\'. \'item\' with value \'f_1234\' not found\"\n        },"
									+ "\n\n                            {\n"
									+ " 							        \"reason\": \"invalid_parameter\","
									+ "\n                                     \"name\": \"item\","
									+ "\n                                  \"message\": \"Invalid value \'f_12347\'. \'item\' with value \'f_6789\' not found\"\n        }\n"
									+ " 								    ]\n "
									+ "								    },\n"
									+ "     		  \"help_url\": \"http:\\/\\/developers.box.com\\/docs\\/#errors\",\n   "
									+ " 			   \"message\": \"Not Found\","
									+ "\n 		    \"request_id\": \"h6uhr3ftd8fe622d\"\n  }";
					
							String json_error_from_token_response = e.getResponse();
							String json_error_from_variable = sample_error_3;
							ErrorResponse error_response = mapper.readValue(json_error_from_variable, ErrorResponse.class);
							System.out.println(error_response);
						}
					} 
				}				
			} catch (Exception e) {
				log.error("Exception ", e);
			}

		};
	}
}



