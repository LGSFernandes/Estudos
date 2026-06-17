package java_curso.aula1;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // Variáveis e Tipos Primitivos
        String meuNome = "Luckas";
        int minhaIdade = 20;

        var numeroReal = 0.5;

        // byte => 8 bits => -128 a 127
        // short => 16 bits => -32.768 a 32.767
        // int => 32 bits => -2.147.483.648 a 2.147.483.647
        // long => 64 bits => -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807

        // float => 32 bits => Precisão Simples
        // double => 64 bits => Precisão Dupla

        // String => Representa Palavras e Frases
        // char => Representa um Único Caractér

        char meuChar = 'a';

        // boolean => true ou false

        boolean meuBool = true;

        byte b = 100;
        short s = 10000;
        int i = 100000;
        long l = 100000L;
        float f = 10.5f;
        double d = 20.5;
        char c = 'A';
        String str = "Luckas";
        boolean bool = true;


        // Condicionais (If, Else If, Else)
        if (bool) {
            System.out.println("Verdadeiro");
        } else {
            System.out.println("False");
        }

        if (str.isBlank()) {
            System.out.println("Vazio");
        } else if (str.equals("Luckas")){
            System.out.println("Verdadeiro");
        } else {
            System.out.println("Falso");
        }

        int dia = 1;
        String nomeDia;

        switch (dia) {
            case 1 -> nomeDia = "Segunda";
            case 2 -> nomeDia = "Terça";
            default -> nomeDia = "Dia inválido";
        };

        System.out.println(nomeDia);

        // Vetores
        int[] colecaoDeInteiros = {1, 2, 3, 4, 5, 6};

        int[] meusNumeros = new int[4];


        // ArrayLists
        ArrayList<String> nomes = new ArrayList<>();
        nomes.add("Luckas");
        nomes.add("Anna");

        System.out.println(nomes.get(0)); // Existe também 'getFirst()'

        nomes.remove(0); // Existe também 'removeFirst()'

            // Remover o Índice 0, fará com que o 1 passe a ser o 0
            // e assim por diante. Removerá 'Luckas' e 'Anna'
            // passará ser o Índice 0

            // Pode remover tanto por Índice como pelo Valor:
                // nomes.remove("Luckas");

            // Para ArrayLists, usa-se .size() para acessar o tamanho,
            // ao invés de lenght

        System.out.println(nomes.get(0));


        // Loops (For, While e Do While)
        for(int j = 0; j < nomes.size(); j++) {
            System.out.println(nomes.get(j));
        }

        for(int k = 0; k < colecaoDeInteiros.length; k++) {
            System.out.println(colecaoDeInteiros[k]);
        }

        for(String nome: nomes) {
            System.out.println(nome);
        }

        int cont = 0;
        while(cont <= 10) {
            System.out.println("Estou no While");
            cont++;
        }

        do {
            System.out.println("Estou no While");
            cont++;
        } while (cont <= 10);


        // Castings (Mudança de Tipos)
        double resultado = 0.0;
        int resultadoInt = (int) resultado;

        int meuInt = 10;
        double meuDouble = meuInt;

        String meuString = "10";
        int meuInt2 = Integer.parseInt(meuString);

        String minhaString = String.valueOf(meuInt2);


        // POO


        // Visibilidade
        // public => Acessível de Todo Lugar
        // default => Quando Não Definido, Segue Este Padrão
        // private => Acessível Somente Dentro da Classe Que Foi Definido
        // protected => Acessível Por Todos Que Estão no Mesmo Pacote


        // Interfaces / Classes Abstratas / Heranças / Polimorfismos
        Carro Sandero = new Sandero();
        for (int pedal = 0; pedal <= 20; pedal++) {
            Sandero.acelerar();
        }

        Carro meuCarro = new Civic();
        meuCarro.acelerar();

        SerVivo meuSer = new Humano();
        meuSer.respirar();


        // Tratamento de Exceções
        Carro meuCarroFurado = null;

        try {
            meuCarroFurado.acelerar();
        } catch (NullPointerException exception) {
            System.out.println("Vende Carro Furado");
        }

            // Principais Tipos de Erros:

                // NullPointerException
                // ArrayIndexOutOfBoundsException
                // RunTimeException
                // IOException
                // ArithmeticException

    }
}


