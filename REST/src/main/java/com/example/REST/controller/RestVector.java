package com.example.REST.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.example.REST.model.Vector;
import com.example.REST.model.VectorReponse;
import com.example.REST.service.VectorService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

@RestController

public class RestVector {
	
    @Autowired
    private VectorService vecSer;
	
    
    @RequestMapping("/")
    @ResponseBody
    public String welcome() {
        return "Welcome to RestTemplate Example.";
    }
    
	@RequestMapping(value = "/vector", //
            method = RequestMethod.POST, //
            produces = { MediaType.APPLICATION_JSON_VALUE })
    @ResponseBody
    public ResponseEntity<VectorReponse> addEmployee(@RequestBody Vector vec) {
        
		VectorReponse vecr = new VectorReponse();
		vecr.setListvector(this.vecSer.getResultVector(vec.getUrl()));
        return ResponseEntity.status(HttpStatus.OK).body(vecr);
    }
}
