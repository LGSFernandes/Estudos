package exercicios_java.exercicio8;

public class Carga {
    protected int id;
    protected double peso;
    protected String tipo;

    public Carga(int id, double valor, String tipo){
        this.id = id;
        this.peso = valor;
        this.tipo = tipo;
    }

    public int getId(){
        return id;
    }

    public double getPeso(){
        return peso;
    }

    public String getTipo(){
        return tipo;
    }
}
