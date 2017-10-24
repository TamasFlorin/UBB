package Controller;

import Models.AnimalFactory;
import Models.FactoryException;
import Models.IAnimal;
import Repository.IRepository;
import Repository.RepositoryException;

import java.util.ArrayList;
import java.util.List;

public class Controller {
    private IRepository<IAnimal> repository;

    public Controller(IRepository<IAnimal> repository){
        this.repository = repository;
    }

    public void add(String type,String name,int age) throws FactoryException,RepositoryException{
        IAnimal animal = AnimalFactory.create(type,name,age);

        this.repository.add(animal);
    }

    public void remove(String type,String name) throws FactoryException,RepositoryException{
        IAnimal animal = AnimalFactory.create(type, name, 0);

        this.repository.remove(animal);
    }

    public List<IAnimal> filterByAge(int minimumAge) throws RepositoryException {
        List<IAnimal> filtered = new ArrayList<>();

        for(int i = 0; i < this.repository.size(); i++){
            IAnimal animal = repository.get(i);
            if( animal.getAge() > minimumAge ) {
                filtered.add(animal);
            }
        }

        return filtered;
    }

    public List<IAnimal> getAll() throws RepositoryException {
        List<IAnimal> animals = new ArrayList<>();

        for(int i = 0; i < this.repository.size(); i++)
            animals.add(repository.get(i));

        return animals;
    }
}
