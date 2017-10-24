package Models;

public class Fish implements IAnimal {
    private String name;
    private int age;

    Fish(String name, int age) {
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
        return "Fish : " + this.name + " is " + this.age + " years old.";
    }

    @Override
    public boolean equals(Object obj) {
        if( obj == null) return false;
        if( this == obj) return true;

        if( obj instanceof Fish ) {
            Fish fish = (Fish)obj;

            return this.name.equals(fish.getName());
        }

        return false;
    }
}
