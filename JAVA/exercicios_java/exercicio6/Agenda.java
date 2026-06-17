package exercicios_java.exercicio6;
import java.util.ArrayList;

public class Agenda {
    protected ArrayList<Contato> contatos;

    public Agenda() {
        this.contatos = new ArrayList<>();
    }

    public void adicionarContato(Contato c) {
        this.contatos.add(c);
    }

    public void removerContato(String nome) {
        this.contatos.removeIf(c -> c.getNome().equals(nome));
    }

    public ArrayList<Contato> buscarPorDominio(String dominio) {
        ArrayList<Contato> resultados = new ArrayList<>();

        for (Contato c : contatos) {
            if (c.getEmail().endsWith(dominio)) {
                resultados.add(c);
            }
        }
        return resultados;
    }
}
