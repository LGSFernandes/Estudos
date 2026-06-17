package exercicios_java.exercicio3;

public class CartaoCredito extends Pagamento {

    private String numeroCartao;

    public CartaoCredito(String numeroCartao) {
        this.numeroCartao = numeroCartao;
    }

    @Override
    public void processarPagamento() {
        if (this.numeroCartao.length() < 16) {
            throw new PagamentoInvalidoException("Erro: O número do cartão deve ter 16 dígitos.");
        }

        System.out.println("Pagamento com cartão " + numeroCartao + " processado com sucesso!");
    }
}
