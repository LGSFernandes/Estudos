package exercicios_java.exercicio7;

public class Main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria(100.0, 200.0);

        try {
            conta.sacar(400.0);
        } catch (SaldoInsuficienteException e) {
            System.out.println(STR."Aviso do sistema: \{e.getMessage()}");
        }
    }
}
