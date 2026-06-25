package com.lfernandes.java_spring.aula2.controllers;


import com.lfernandes.java_spring.aula2.domain.Event;
import com.lfernandes.java_spring.aula2.dtos.EventRequestDTO;
import com.lfernandes.java_spring.aula2.dtos.SubscriptionRequestDTO;
import com.lfernandes.java_spring.aula2.services.EventService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/events")
public class EventController {

    @Autowired
    private EventService eventService;

    @GetMapping
    public List<Event> getAllEvents() {
        return eventService.getAllServices();
    }

    @GetMapping("/upcoming")
    public List<Event> getUpComingEvents() {
        return eventService.getUpComingEvents();
    }

    @PostMapping("/criar")
    public Event createEvent(@RequestBody EventRequestDTO event) {
        return eventService.createEvent(event);
    }

    @PostMapping("/{eventId}/register")
    public ResponseEntity<String> registerParticipant(
            @PathVariable String eventId,
            @RequestBody SubscriptionRequestDTO subscriptionRequest) {
        eventService.registerParticipant(eventId, subscriptionRequest.participantEmail());
        return ResponseEntity.ok("Subscription successful");
    }
}
