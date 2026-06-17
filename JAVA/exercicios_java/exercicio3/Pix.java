package exercicios_java.exercicio3;
import java.util.UUID;

public class Pix extends Pagamento {
    String chavePix;

    public Pix() {
        this.chavePix = UUID.randomUUID().toString();
    }

    @Override
    public void processarPagamento() {
        System.out.println(STR."Sua Chave PIX é \{this.chavePix}");
    }
}
