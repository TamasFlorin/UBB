package View;
import java.util.InputMismatchException;
import java.util.Scanner;
import Controller.Controller;
import Models.FactoryException;
import Models.IAnimal;
import Repository.RepositoryException;

public class View {
    enum State {
        E_RUNNING,
        E_STOP
    }

    private static Scanner scanner;
    private Controller controller;
    private State state;

    public View(Controller controller) {
        this.controller = controller;
        this.state = State.E_STOP;

        scanner = new Scanner(System.in);
    }

    private void addAnimal() {
        System.out.println("Type: ");
        String type = scanner.next();
        System.out.println("Name: ");
        String name = scanner.next();
        System.out.println("Age: ");

        try {
            int age = scanner.nextInt();
            this.controller.add(type, name, age);

        }catch (RepositoryException | FactoryException ex) {
            System.out.println(ex.getMessage());
        } catch(InputMismatchException ex) {
            System.out.println("Invalid input provided!");
        }
    }

    private void removeAnimal() {
        System.out.println("Type: ");
        String type = scanner.next();
        System.out.println("Name: ");
        String name = scanner.next();

        try {
            this.controller.remove(type, name);
        }
        catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }

    private void printAnimals() {
        System.out.println("All animals: ");

        try {
            for(IAnimal animal : this.controller.getAll())
                System.out.println(animal);
        }
        catch(RepositoryException ex) {
            System.out.println("An unexpected error has occurred: " + ex.getMessage());
        }

        System.out.println();
    }

    private void printFiltered() {
        System.out.println("Animals older than one year: ");

        try {
            for (IAnimal animal : this.controller.filterByAge(1))
                System.out.println(animal);
        }
        catch (RepositoryException ex) {
            System.out.println("An unexpected error has occurred: " + ex.getMessage());
        }

        System.out.println();
    }

    private void printMenu() {
        System.out.println("1.Add animal\n2.Remove animal\n3.Print animals\n4.Filter by age of 1\n5.Exit");
    }

    private String readCommand() {
        return scanner.next();
    }

    private void executeCommand(String command) {
        if("1".equals(command)) {
            this.addAnimal();
        }
        else if("2".equals(command)){
            this.removeAnimal();
        }
        else if("3".equals(command)){
            this.printAnimals();
        }
        else if("4".equals(command)){
            this.printFiltered();
        }
        else if("5".equals(command)){
            this.setState(State.E_STOP);
        }
    }

    private void setState(State state) {
        this.state = state;
    }

    public void run() {
        this.setState(State.E_RUNNING);

        while(state == State.E_RUNNING) {
            this.printMenu();
            String command = this.readCommand();
            this.executeCommand(command);
        }
    }
}
