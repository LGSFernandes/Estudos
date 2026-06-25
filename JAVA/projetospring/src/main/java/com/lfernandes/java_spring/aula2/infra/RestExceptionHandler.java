package com.lfernandes.java_spring.aula2.infra;

import com.lfernandes.java_spring.aula2.exceptions.EventFullException;
import com.lfernandes.java_spring.aula2.exceptions.EventNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
public class RestExceptionHandler extends ResponseEntityExceptionHandler {
    @ExceptionHandler(EventNotFoundException.class)
    private ResponseEntity<RestErrorMessage> eventNotFoundHandler(EventNotFoundException exception){
        RestErrorMessage threatedResponse = new RestErrorMessage(HttpStatus.NOT_FOUND, exception.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(threatedResponse);
    }

    @ExceptionHandler(EventFullException.class)
    private ResponseEntity<RestErrorMessage> eventFullHandler(EventFullException exception){
        RestErrorMessage threatedResponse = new RestErrorMessage(HttpStatus.INTERNAL_SERVER_ERROR, exception.getMessage());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(threatedResponse);
    }
}







