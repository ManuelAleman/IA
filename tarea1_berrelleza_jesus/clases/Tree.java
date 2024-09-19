package tarea1_berrelleza_jesus.clases;

public class Tree {
    private Node start;

    public Tree() {
        this.start = null;
    }

    public Node getStart() {
        return start;
    }
    public void setStart(Node start) {
        this.start = start;
    }

    public boolean isEmpty(){
        return start == null;
    }

    public Node searchNode(String name){
        return searchNodeCurrent(start, name);
    }

    private Node searchNodeCurrent(Node current, String name){
        if(current == null){
            return null;
        }
        if(name.equals(current.getName())){
            return current;
        }
        if(name.compareTo(current.getName()) < 0){
            return searchNodeCurrent(current.getLeft(), name);
        }else {
            return searchNodeCurrent(current.getRight(), name);
        }
    }

    public void insertNode(String name){
        start = insertNodeRecursive(start, name);
    }

    public Node insertNodeRecursive(Node current, String name){
        if (current == null) {
            return new Node(name);
        }
        if (name.compareTo(current.getName()) < 0) {
            current.setLeft(insertNodeRecursive(current.getLeft(), name));
        } else if (name.compareTo(current.getName()) > 0) {
            current.setRight(insertNodeRecursive(current.getRight(), name));
        }
        return current;
    }

    public void printRecursive() {
        printRecursive(start);
    }

    private void printRecursive(Node current) {
        if(current == null){
            return;
        }

        printRecursive(current.getLeft());
        printRecursive(current.getRight());
        System.out.println(current.getName());

    }

}
