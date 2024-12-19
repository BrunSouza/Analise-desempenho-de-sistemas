import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.File;

public class Automatizar_Teste_Memoria {

    public static void main(String[] args) {
        String classpath = "bin/;lib/*";
        String mainClass = "BenchmarkAcessoMemoria";
        String workingDirectory = "C:\\Users\\bruns\\Downloads\\ADS-Lab1"; // Diretório de trabalho

        int firstLimit = 102400;
        int finalLimit = 1048576;
        int initialIncrement = 10240;
        int finalIncrement = 102400;

        // Executando os testes com incremento de 10240 até 102400
        for (int startValue = 10240; startValue <= firstLimit; startValue += initialIncrement) {
            executeCommand(classpath, mainClass, workingDirectory, startValue);
        }

        // Executando os testes com incremento de 102400 até 1048576
        for (int startValue = 102400; startValue <= finalLimit; startValue += finalIncrement) {
            executeCommand(classpath, mainClass, workingDirectory, startValue);
        }
    }

    private static void executeCommand(String classpath, String mainClass, String workingDirectory, int startValue) {
        try {
            // Limite fixo
            int endValue = 110000000;

            // Construindo o comando
            String command = String.format(
                    "java -cp \"%s\" %s %d %d",
                    classpath, mainClass, startValue, endValue
            );

            System.out.println("Executando comando: " + command);

            // Criando o ProcessBuilder
            ProcessBuilder pb = new ProcessBuilder(command.split(" "));
            pb.directory(new File(workingDirectory)); // Configurando o diretório de trabalho
            Process process = pb.start();

            // Lendo a saída do programa
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream())
            );
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Esperando o processo terminar
            int exitCode = process.waitFor();
            System.out.println("Comando terminou com código de saída: " + exitCode);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

