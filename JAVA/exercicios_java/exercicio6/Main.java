package exercicios_java.exercicio6;

public class Main {
    public static void main(String[] args){
        Agenda agenda = new Agenda();

        Contato c1 = new Contato("Luckas", "luckas.fernandes14@gmail.com");
        Contato c2 = new Contato("Anna", "annavitoria19@yahoo.com");
        Contato c3 = new Contato("Laura", "laura.silva@gmail.com");
        Contato c4 = new Contato("Maria", "maria.oliveira@gmail.com");

        agenda.adicionarContato(c1);
        agenda.adicionarContato(c2);
        agenda.adicionarContato(c3);
        agenda.adicionarContato(c4);
        agenda.removerContato("Luckas");

        System.out.println("Contatos na agenda:");
        for (Contato c : agenda.contatos){
            System.out.println(STR."Nome: \{c.getNome()}, Email: \{c.getEmail()}");
        }

        System.out.println("\nContatos com domínio 'gmail.com':");
        for (Contato c : agenda.buscarPorDominio("gmail.com")){
            System.out.println(STR."Nome: \{c.getNome()}, Email: \{c.getEmail()}");
        }
    }
}
