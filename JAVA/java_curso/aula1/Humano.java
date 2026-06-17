package java_curso.aula1;

public class Humano extends SerVivo {

    public String nome;

    public Humano() {
        super(20);
        this.nome = "Luckas";
    }

    @Override
    public void respirar() {
        System.out.println(this.idade);
        System.out.println("Respirando como Humano");
    }
}
