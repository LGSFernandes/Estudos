package exercicios_java.exercicio9;

public class Administrador implements Autenticavel{

    protected String senha;

    public Administrador(String senha) {
        this.senha = senha;
    }

    @Override
    public boolean logar() {
        if(this.senha.equals("Admin@2026")) {
            System.out.println(STR."Administrador logado com sucesso com senha: \{this.senha}!");
            return true;
        }
        else {
            System.out.println(STR."Falha ao logar administrador com senha: \{this.senha}!");
            return false;
        }
    }
}
