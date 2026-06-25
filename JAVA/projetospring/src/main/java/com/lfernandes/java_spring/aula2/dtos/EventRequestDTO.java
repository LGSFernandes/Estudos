package com.lfernandes.java_spring.aula2.dtos;

import java.time.LocalDateTime;

public record EventRequestDTO(String name, LocalDateTime date) {}