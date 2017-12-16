package Controller;


import Model.State.ProgramState;
import Model.Statement.StatementException;
import Repository.IRepository;
import Repository.RepositoryException;
import Util.Heap.HeapException;
import Util.Tuple.Tuple;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class InterpreterController {
    private IRepository repository;
    private final ExecutorService executorService = Executors.newFixedThreadPool(2);

    public InterpreterController(IRepository repository) {
        this.repository = repository;
    }

    private void conservativeGarbageCollector() throws HeapException, RepositoryException {
        ProgramState programState = this.repository.back();

        programState.getHeap().garbageCollect(programState.getSymbolTable().values());
    }

    private void closeFile(Map.Entry<Integer, Tuple<String, BufferedReader>> entry) throws StatementException {
        try {
            entry.getValue().getSecond().close();
        } catch (IOException ex) {
            throw new StatementException("Could not close file!");
        }
    }

    private void closeFiles(List<ProgramState> programStates) {
        programStates.forEach(programState -> {
            programState.getFileTable().entrySet().forEach(e -> {
                try {
                    closeFile(e);
                } catch (StatementException e1) {
                    e1.printStackTrace();
                }
            });
            programState.getFileTable().clear();
        });
    }

    private List<ProgramState> removeCompletedPrograms(List<ProgramState> states) {
        return states.stream().filter(p-> !p.isCompleted()/*ProgramState::isNotCompleted*/).collect(Collectors.toList());
    }

    private void oneStepForAllPrograms(List<ProgramState> programStates) throws StatementException {
        try {
            this.repository.logData();

            List<Callable<ProgramState>> callList = programStates.stream()
                    .map((ProgramState p) -> (Callable<ProgramState>)(p::oneStep))
                    .collect(Collectors.toList());

            List<ProgramState> newPrgList = executorService.invokeAll(callList).stream()
                    .map(future -> {
                        try {
                            return future.get();
                        } catch (Exception e) {
                            e.printStackTrace();
                            return null;
                        }
                    }).filter(Objects::nonNull).collect(Collectors.toList());

            programStates.addAll(newPrgList);

            this.repository.logData();

            this.repository.setData(programStates);

        }catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void executeAllSteps(){
        List<ProgramState> programs = removeCompletedPrograms(this.repository.getAll());

        while(!programs.isEmpty()) {
            try {
                conservativeGarbageCollector();
                oneStepForAllPrograms(programs);
                programs = removeCompletedPrograms(this.repository.getAll());
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        executorService.shutdownNow();

        List<ProgramState> tmpList = repository.getAll();
        closeFiles(tmpList);

        repository.setData(programs);
    }
}
