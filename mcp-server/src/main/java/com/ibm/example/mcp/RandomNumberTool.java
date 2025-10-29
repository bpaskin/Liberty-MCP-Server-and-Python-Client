package com.ibm.example.mcp;

import com.ibm.example.beans.RandomNumber;

import io.openliberty.mcp.annotations.Tool;
import io.openliberty.mcp.annotations.ToolArg;
import jakarta.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class RandomNumberTool {
    
    @Tool(name="Random Number Generator", description = "Will generate a random number based on numbers provided", title="Magical Random Number Generator")
    public String generateRandomNumber(@ToolArg(name = "minNumber", description = "Minimum random number") int minNumber,
                                    @ToolArg(name = "maxNumber", description = "Maxmimum random number") int maxNumber) {
                                
        return String.valueOf(new RandomNumber(minNumber, maxNumber).generate());
    }
}
