package Repository;

class EntityNotFoundException extends RepositoryException {
    EntityNotFoundException(String message) {
        super(message);
    }
}
