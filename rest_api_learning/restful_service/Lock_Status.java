package com.spindices.box.integration.rest;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Lock_Status {

	private String type;
	private String id;
	private String etag;
	private Lock_Detail lock_detail;
	
	public String getType() {
		return type;
	}
	public void setDetail(String type) {
		this.type = type;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getEtag() {
		return etag;
	}
	public void setEtag(String etag) {
		this.etag = etag;
	}
	public Lock_Detail getLock() {
		return lock_detail;
	}
	public void setLock(Lock_Detail lock_detail) {
		this.lock_detail = lock_detail;
	}
	@Override
	public String toString() {
		try {
			return  new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return "Lock{"   + 
			   "type='"  + type + '\'' +
			   ", id='"  + id   + '\'' +
			   ", etag='"+ etag + '\'' +
			   ", lock=" + lock_detail + "}";
	} 	
}