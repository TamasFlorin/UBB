package Repository;

class DuplicateEntityException extends RepositoryException {
    DuplicateEntityException(String message){
        super(message);
    }
}
