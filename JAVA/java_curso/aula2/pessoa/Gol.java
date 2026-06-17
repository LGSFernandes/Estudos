package java_curso.aula2.pessoa;
import java_curso.aula2.carro.Carro;

public class Gol extends Carro {
    public Gol(String modelo, String cor, int ano, String placa){
        super(modelo, cor, ano, placa);
        this.modelo = modelo;
    }

    @Override
    public void ligar(){
        System.out.println("Gol Ligado");
    }

    @Override
    public void desligar(){
        System.out.println("Gol Desligado");
    }
}
