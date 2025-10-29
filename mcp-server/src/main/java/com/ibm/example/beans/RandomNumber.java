package com.ibm.example.beans;

import java.security.SecureRandom;

public class RandomNumber {
    private int minNumber;
    private int maxNumber;
    private SecureRandom random = new SecureRandom();

    public RandomNumber(int minNumber, int maxNumber) {
        this.minNumber = minNumber;
        this.maxNumber = maxNumber;
    }

    public int generate() {
        return random.nextInt(maxNumber - minNumber) + minNumber;
    }
}
