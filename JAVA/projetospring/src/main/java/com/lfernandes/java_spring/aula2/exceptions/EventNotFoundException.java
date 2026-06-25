package com.lfernandes.java_spring.aula2.exceptions;

public class EventNotFoundException extends RuntimeException {

     public EventNotFoundException() {
        super("Evento Não Encontrado!");
    }

    public EventNotFoundException(String message) {
        super(message);
    }
}
