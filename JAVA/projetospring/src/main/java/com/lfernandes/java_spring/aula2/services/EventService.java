package com.lfernandes.java_spring.aula2.services;

import com.lfernandes.java_spring.aula2.dtos.EventRequestDTO;
import com.lfernandes.java_spring.aula2.domain.Event;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class EventService {
    private final List<Event> eventRepository = new ArrayList<>();

    public List<Event> getAllServices() {
        return eventRepository;
    }

    public List<Event> getUpComingEvents() {
        return eventRepository.stream()
                .filter(e -> e.getDate().isAfter(LocalDateTime.now()))
                .collect(Collectors.toList());
    }

    public Event createEvent(EventRequestDTO data) {
        Event newEvent = new Event(UUID.randomUUID().toString(), data.name(), data.date());
        eventRepository.add(newEvent);
        return newEvent;
    }

    public void registerParticipant(String eventId, String email) {
        System.out.println("Registrando " + email + " no evento " + eventId);
    }
}