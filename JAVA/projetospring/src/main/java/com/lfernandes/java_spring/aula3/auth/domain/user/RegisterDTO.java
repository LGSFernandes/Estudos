package com.lfernandes.java_spring.aula3.auth.domain.user;

public record RegisterDTO(String login, String password, UserRole role) {
}
