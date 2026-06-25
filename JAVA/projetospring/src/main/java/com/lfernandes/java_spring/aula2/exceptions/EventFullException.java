package com.lfernandes.java_spring.aula2.exceptions;

public class EventFullException extends RuntimeException {

    public EventFullException() {
        super("Evento Está Lotado!");
    }

    public EventFullException(String message) {
        super(message);
    }
}
