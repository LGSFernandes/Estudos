package com.lfernandes.java_spring.exercicios_spring.exercicio3.exceptions;

public class VeiculoNaoEncontradoException extends RuntimeException {
    public VeiculoNaoEncontradoException(String message) {
        super(message);
    }
}
