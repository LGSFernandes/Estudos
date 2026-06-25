package com.lfernandes.java_spring.exercicios_spring.exercicio3.infra;

import com.lfernandes.java_spring.exercicios_spring.exercicio3.exceptions.VeiculoNaoEncontradoException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(VeiculoNaoEncontradoException.class)
    public ResponseEntity<String> handleVeiculoNaoEncontrado(VeiculoNaoEncontradoException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(ex.getMessage());
    }
}