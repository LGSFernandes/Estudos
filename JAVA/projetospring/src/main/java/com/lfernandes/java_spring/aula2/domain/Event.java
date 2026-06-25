package com.lfernandes.java_spring.aula2.domain;

import java.time.LocalDateTime;

public class Event {
    private String id;
    private String name;
    private LocalDateTime date;

    public Event(String id, String name, LocalDateTime date) {
        this.id = id;
        this.name = name;
        this.date = date;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public LocalDateTime getDate() { return date; }
}