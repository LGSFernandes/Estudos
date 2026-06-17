package exercicios_java.exercicio9;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Autenticavel> autenticavels = new ArrayList<>();

        UsuarioComum user = new UsuarioComum("555");
        UsuarioComum user2 = new UsuarioComum("123");
        UsuarioComum user3 = new UsuarioComum("000");
        autenticavels.add(user);
        autenticavels.add(user2);
        autenticavels.add(user3);

        Administrador admin = new Administrador("Admin@2026");
        Administrador admin2 = new Administrador("Admin");
        Administrador admin3 = new Administrador("ADM");
        autenticavels.add(admin);
        autenticavels.add(admin2);
        autenticavels.add(admin3);

        for (Autenticavel auth : autenticavels){
            auth.logar();
        }
    }
}
