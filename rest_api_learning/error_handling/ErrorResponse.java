package com.spindices.box.integration.rest.errors;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@JsonIgnoreProperties(ignoreUnknown = true)
public class ErrorResponse {
	
	private String type;
	private int status;
	private String code;
	private String help_url;
	private String message;
	private String request_id;
	private ContextInfo context_info;
	
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public int getStatus() {
		return status;
	}
	public void setStatus(int status) {
		this.status = status;
	}
	public String getCode() {
		return code;
	}
	public void setCode(String code) {
		this.code = code;
	}
	public String getHelp_url() {
		return help_url;
	}
	public void setHelp_url(String help_url) {
		this.help_url = help_url;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	public String getRequest_id() {
		return request_id;
	}
	public void setRequest_id(String request_id) {
		this.request_id = request_id;
	}
	public ContextInfo getContext_info() {
		return context_info;
	}
	public void setContext_info(ContextInfo context_info) {
		this.context_info = context_info;
	}
	@Override
	public String toString() {
		try {
			return new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return "BoxAPIExceptionCode{ " + 
					"type='"  + type + '\'' +
					", status='" + status + '\'' +
					", code='" + code + '\'' +
					", context_info='" + context_info + '\'' +
					", help_url='" + help_url + '\'' +
					", message='" + message + '\'' +
					", request_id='" + request_id + '}';
	} 
}
