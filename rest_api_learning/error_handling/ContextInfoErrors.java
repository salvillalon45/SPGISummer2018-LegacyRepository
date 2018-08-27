package com.spindices.box.integration.rest.errors;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@JsonIgnoreProperties(ignoreUnknown = true)
public class ContextInfoErrors {
	
	private String reason;
	private String name;
	private String message;

	public String getReason() {
		return reason;
	}
	public void setReason(String reason) {
		this.reason = reason;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	@Override
	public String toString() {
		try {
			return new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);			
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return "ContextInfoErrors{ " +
							" reason='" + reason + '\'' +
							", name='" + name+ '\'' +
							", message=" + message + '}';
	}
}
