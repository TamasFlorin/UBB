package View;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TextView {
    //private InterpreterController controller;
    private Map<String,Command> commands;

    public TextView() {
        this.commands = new HashMap<>();
    }

    public void addCommand(Command command) {
        this.commands.put(command.getKey(),command);
    }

    private void printMenu(){
        for(Command command : this.commands.values()) {
            String line = String.format("%4s: %s",command.getKey(),command.getDescription());
            System.out.println(line);
        }
    }

    public void show() {
        Scanner scanner = new Scanner(System.in);

        while(true) {
            printMenu();
            System.out.println("command name: ");
            String key = scanner.nextLine();

            Command command = commands.get(key);

            if( command == null) {
                System.out.println("Invalid option!");
            }
            else {
                command.execute();
            }
        }
    }
}
