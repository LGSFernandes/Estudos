package exercicios_java.exercicio3;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Pagamento> pagamentos = new ArrayList<>();
        pagamentos.add(new CartaoCredito("123"));
        pagamentos.add(new Pix());

        for (Pagamento p : pagamentos) {
            try {
                p.processarPagamento();
            } catch (PagamentoInvalidoException e) {
                System.out.println("Aviso: Falha ao processar pagamento. " + e.getMessage());
            }
        }
    }
}
