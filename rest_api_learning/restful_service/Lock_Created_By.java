package com.spindices.box.integration.rest;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Lock_Created_By {
	
	private String name;
	private String login;

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getLogin() {
		return login;
	}
	public void setLogin(String login) {
		this.login = login;
	}
	@Override
	public String toString() {
		try {
			return  new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);                                                                                                                                                               
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return "created_by{" + 
      	      	   "name='"   + name  + '\'' +
		      	   ", login=" + login + '}';
	}
}