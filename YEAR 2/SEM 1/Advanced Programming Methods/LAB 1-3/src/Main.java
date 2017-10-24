import Controller.Controller;
import Models.IAnimal;
import View.View;
import Repository.MemoryRepository;

public class Main {
    public static void main(String[] args) {
        MemoryRepository<IAnimal> repository = new MemoryRepository<>();
        Controller controller = new Controller(repository);
        View view = new View(controller);
        view.run();
    }
}
