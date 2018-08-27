package com.spindices.box.integration.rest;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Lock_Detail {

	private String type;
	private Lock_Created_By created_by;

	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public Lock_Created_By getCreated_by() {
		return created_by;
	}
	public void setCreated_by(Lock_Created_By created_by) {
		this.created_by = created_by;
	}
	@Override
	public String toString() {
		try {
			return  new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return "Lock_Detail{" + 
					"type='"  + type + '\'' +
					", created_by=" + created_by + '}';
	} 
}