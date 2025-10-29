package com.ibm.example.rest;

import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import com.ibm.example.beans.RandomNumber;

@Path("/")
public class RandomNumberService {
    
    @Path("generateRandomNumber/{minNumber}/{maxNumber}")
    @POST
    @Produces(MediaType.APPLICATION_JSON) 
    public int generateRandomNumber(@PathParam ("minNumber") int minNumber, @PathParam("maxNumber") int maxNumber) {
        return new RandomNumber(minNumber, maxNumber).generate();
    }
}
