package com.spindices.box.integration.rest.errors;

import java.util.ArrayList;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@JsonIgnoreProperties(ignoreUnknown = true)
public class ContextInfo {
	
	private ArrayList<ContextInfoErrors> errors;

	public ArrayList<ContextInfoErrors> getErrors() {
		return errors;
	}
	public void setErrors(ArrayList<ContextInfoErrors> errors) {
		this.errors = errors;
	}
	@Override
	public String toString() {
		try {				
			return new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return "ContextInfo{" + 
					"errors="  + errors + "}";
	}
}
