package java_curso.aula2;
import java_curso.aula2.*;
import java_curso.aula2.carro.CarroRecord;

import java.util.*;
import java.util.stream.Collectors;

import static java.lang.StringTemplate.STR;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Luckas Fernandes");
        list.add("Luckas Souza");
        list.add("Luckas Guedes");
        list.add("Anna Vitória");

        System.out.println(STR."Primeiro Nome da Lista \{list.get(0)}");
        System.out.println(STR."Lista: \{list}");


        Set<String> setStrings = new HashSet<>();
        setStrings.add("Luckas");
        setStrings.add("Anna");
        setStrings.add("Laura");
        setStrings.add("Luckas");

        System.out.println(STR."Set: \{setStrings.contains("Anna")}");
        System.out.println(STR."SetStrings: \{setStrings}");


        Map<String, String> map = new HashMap<>();

        map.put("nome", "Luckas");
        map.put("sobrenome", "Fernandes");

        System.out.println(STR."Nome: \{map.get("nome")}");
        System.out.println(STR."Sobrenome: \{map.get("sobrenome")}");
        System.out.println(STR."Map: \{map}");


        Queue<String> queue = new LinkedList<>();

        queue.add("Luckas");
        queue.add("Anna");

        System.out.println(STR."Queue: \{queue}");
        System.out.println(STR."Queue poll: \{queue.poll()}");
        System.out.println(STR."Queue poll: \{queue.poll()}");
        System.out.println(STR."Queue poll: \{queue.poll()}");
        System.out.println(STR."Queue: \{queue}");

        // Diferença entre poll e remove: Remove lança uma exceção caso a lista esteja vazia, poll não.


        LinkedList<String> linked = new LinkedList<>();
        linked.add("Luckas");
        linked.add("Anna");
        linked.addFirst("Laura");
        linked.addLast("Erica");

        System.out.println(STR."Linked \{linked}");
        System.out.println(STR."Primeiro Nome no Linked: \{linked.get(0)}");


        // DTOs: Data Transfer Object, são usados para transportar dados entre camadas de uma aplicação.
        // Record: é uma classe imutável que tem como objetivo representar um conjunto de dados
        CarroRecord sandero = new CarroRecord("Sandero", "Branco", 2010, "ABC-1234");
        System.out.println(STR."Ano do Sandero: \{sandero.ano()}");

        // Stream API:
         // Realizar Operações Funcionais nas Collections
         // filter, map, reduce, agregações
         // filter - Filtrar os Elementos de Uma Coleção
         // map - Transformar os Elementos de Uma Coleção
         // reduce - Reduzir os Elementos de Uma Coleção
         // agregações - Soma, Média, Contagem, etc...
        List<String> luckas = list
                .stream()
                .filter(nome -> nome.startsWith("Luckas"))
                .map(String::toUpperCase)
                .toList();
        System.out.println(STR."Luckas: \{luckas}");

        String luckasConcatenado = list
                .stream()
                .filter(nome -> nome.startsWith("Luckas"))
                .map(String::toUpperCase)
                .map(nome -> nome.replaceAll(" ", ""))
                .reduce("", (a, b) -> a + b);
        System.out.println(STR."Luckas Concatenado: \{luckasConcatenado}");

        Set<String> luckasSet = list
                .stream()
                .filter(nome -> nome.startsWith("Luckas"))
                .map(String::toUpperCase)
                .map(nome -> nome.replaceAll(" ", ""))
                .collect(Collectors.toSet());
        System.out.println(STR."Luckas Set: \{luckasSet}");

    }
}
