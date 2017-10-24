package Models;

public class Tortoise implements IAnimal {
    private String name;
    private int age;

    Tortoise(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Tortoise : " + this.name + " is " + this.age + " years old.";
    }

    @Override
    public boolean equals(Object obj) {
        if( obj == null) return false;

        if( this == obj) return true;

        if( obj instanceof Tortoise) {
            Tortoise tortoise = (Tortoise) obj;

            return this.name.equals(tortoise.getName());
        }

        return false;
    }
}
