package View;

public abstract class Command {
    private String key,description;

    public Command(String key,String description) {
        this.key = key;
        this.description = description;
    }

    public abstract void execute();
    public String getKey() { return this.key; }
    public String getDescription() { return this.description; }
}
