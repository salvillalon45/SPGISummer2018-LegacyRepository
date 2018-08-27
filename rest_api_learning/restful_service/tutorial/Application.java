package com.spindices.box.integration.rest.tutorial;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class Application {

	private static final Logger log = LoggerFactory.getLogger(Application.class);

	public static void main(String args[]) {
		SpringApplication.run(Application.class);
	}

	@Bean
	public RestTemplate restTemplate(RestTemplateBuilder builder) {
		return builder.build();
	}

	@Bean
	public CommandLineRunner run(RestTemplate restTemplate) throws Exception {

		return args -> {
			Quote quote = restTemplate.getForObject(
					"https://gturnquist-quoters.cfapps.io/api/random", Quote.class);
			log.info(quote.toString());
		};
	}
}




//HttpHeaders headers = new HttpHeaders();
//headers.add("Authorization", "Bearer ".concat(loginResponse.getAccess_token()));
//HttpEntity<String> request = new HttpEntity<String>(headers);
//ResponseEntity<ReportDescribeResponse> reportDescribeResponse = restTemplate.exchange("https://spglobal--midjidev.cs70.my.salesforce.com/services/data/v35.0/analytics/reports/" + reportId + "/describe", 
//		HttpMethod.GET, request, ReportDescribeResponse.class);
//log.debug(reportDescribeResponse.toString()); 





