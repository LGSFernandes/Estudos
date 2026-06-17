package exercicios_java.exercicio7;

public class ContaBancaria {
    protected double saldo;
    protected double limite;

    public ContaBancaria(double saldo, double limite){
        this.saldo = saldo;
        this.limite = limite;
    }

    public void sacar(double valor) throws SaldoInsuficienteException {
        if (valor > (this.saldo + this.limite)) {
            throw new SaldoInsuficienteException(STR."Saldo insuficiente. Disponível: R$\{this.saldo + this.limite}");
        }
        this.saldo -= valor;
        System.out.println(STR."Saque de R$\{valor} realizado. Saldo atual: R$\{this.saldo}");
    }
}
