package java_curso.aula2.carro;

import java_curso.aula2.pintura.Pintavel;

public class Carro implements Pintavel {
    protected String modelo;
    String cor;
    int ano;
    String placa;

    public Carro(String modelo, String cor, int ano, String placa){
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        this.placa = placa;
    }

    public void ligar(){
        System.out.println(STR."Carro \{this.modelo} ligado");
    }

    public void desligar(){
        System.out.println(STR."Carro \{this.modelo} desligado");
    }

    protected void teste(){
        System.out.println("Testando");
    }

    @Override
    public void aplicarTinta() {

    }

    @Override
    public String getCor() {
        return "";
    }

    @Override
    public void setCor(String cor) {

    }

    @Override
    public String getTipo() {
        return "";
    }

    @Override
    public void setTipo(String tipo) {

    }

    @Override
    public String getMarca() {
        return "";
    }

    @Override
    public void setMarca(String marca) {

    }

    @Override
    public double getPreco() {
        return 0;
    }

    @Override
    public void SetPreco(double preco) {

    }
}
