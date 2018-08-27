package com.spindices.box.integration.rest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class FileLockStatusApp {
	private static final Logger log = LoggerFactory.getLogger(FileLockStatusApp.class);
	
	private String fileTestPdfInfoId = "301579619254";
	private String fileTestDocxInfoId = "302086748622";
	private String fileTestXlsxInfoId = "302083656715";
	
	public static void main(String args[]) {
		SpringApplication.run(FileLockStatusApp.class);
	}
	
	@Bean
	public RestTemplate restTemplate(RestTemplateBuilder builder) {
		return builder.build();
	}
	
	@Bean
	public CommandLineRunner run(RestTemplate restTemplate) throws Exception {
		return args -> {
			HttpHeaders headers = new HttpHeaders();
			headers.set("Authorization", "Bearer ".concat("HsoztAoP50WFXF81JopY5f3wfEjGz8me"));
			HttpEntity<String> request = new HttpEntity<String>(headers);
 
			ResponseEntity<Lock_Status> response = restTemplate.exchange(
					"https://api.box.com/2.0/files/" + fileTestDocxInfoId + "?fields=lock", 
					HttpMethod.GET, 
					request, 
					Lock_Status.class);
			
			log.info(response.getBody().toString());
		};
	}
}
