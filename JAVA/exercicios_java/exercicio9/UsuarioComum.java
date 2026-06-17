package exercicios_java.exercicio9;

public class UsuarioComum implements Autenticavel {

    protected String senha;

    public UsuarioComum(String senha){
        this.senha = senha;
    }

    @Override
    public boolean logar() {
        if(this.senha.equals("123")) {
            System.out.println(STR."Usuário comum logado com sucesso com senha: \{this.senha}!");
            return true;
        }
        else {
            System.out.println(STR."Falha ao logar usuário comum com senha: \{this.senha}!");
            return false;
        }
    }
}
