package Models;

public class AnimalFactory {
    public static IAnimal create(String type,String name,int age) throws FactoryException {
        if( type == null || name == null)
            return null;

        if( type.equalsIgnoreCase("tortoise"))
            return new Tortoise(name,age);

        else if(type.equalsIgnoreCase("fish"))
            return new Fish(name,age);

        throw new FactoryException("Invalid type provided!");
    }
}
