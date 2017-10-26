package View;

import Controller.InterpreterController;

public class RunExampleCommand extends Command {
    private InterpreterController controller;

    public RunExampleCommand(String key,String description,InterpreterController controller) {
        super(key,description);
        this.controller = controller;
    }

    @Override
    public void execute() {
        try {
            this.controller.executeAllSteps();
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }
    }
}
