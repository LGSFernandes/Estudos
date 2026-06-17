package java_curso.aula2.pintura;


import java.util.List;

public class Pintura <E>{
    private List<E> coisasQueVouPintar;
    private String tipo;
    private String marca;
    private double preco;

    public Pintura(String tipo, String marca, double preco){
        this.tipo = tipo;
        this.marca = marca;
        this.preco = preco;
    }

    public void pintar(E coisa){
        this.coisasQueVouPintar.add(coisa);
        this.coisasQueVouPintar.get(0);
    }
}
