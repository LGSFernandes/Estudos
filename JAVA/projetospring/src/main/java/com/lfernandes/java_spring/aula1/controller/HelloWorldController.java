package com.lfernandes.java_spring.aula1.controller;

import com.lfernandes.java_spring.aula1.domain.User;
import com.lfernandes.java_spring.aula1.service.HelloWorldService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/hello-world")
public class HelloWorldController {

    @Autowired
    private HelloWorldService helloWorldService;

    // Método GET (/hello-world)
    // Pode-se adicionar mais parâmetros no endpoint (@GetMapping(/get) -> /hello-world/get)
    @GetMapping
    public String HelloWorld(){
        return helloWorldService.HelloWorld("LFernandes");
    }

    @PostMapping("/{id}")
    public String HelloWorldPost(@PathVariable("id") String id, @RequestParam(value = "filter", defaultValue = "none") String filter, @RequestBody User body){
        return "Hello World Post! " + filter;
    }
}
