package java_curso.aula1;

public class Sandero implements Carro {

    final int limiteDeVelocidade = 150;
    public int velocidadeAtual = 0;

    @Override
    public void acelerar() {
        if (this.velocidadeAtual < this.limiteDeVelocidade){
            this.velocidadeAtual += 10;
            System.out.println("Acelerando");
        }
        System.out.println(STR."Velocidade Atual: \{this.velocidadeAtual}Km/h");
    }

    @Override
    public void freiar() {

    }

    @Override
    public void parar() {

    }
}
