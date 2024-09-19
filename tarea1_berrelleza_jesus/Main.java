package tarea1_berrelleza_jesus;

import tarea1_berrelleza_jesus.clases.Tree;

public class Main {
    public static void main(String[] args) {

        Tree tree = new Tree();

        System.out.println("PRUEBA ESTA VACIO?");
        System.out.println(tree.isEmpty());

        System.out.println("\n\nINSERTANDO NODOS...");
        tree.insertNode("Federico");
        tree.insertNode("Bachata");
        tree.insertNode("Garcia");
        tree.insertNode("Antonio");
        tree.insertNode("Diego");
        tree.insertNode("Ignacio");
        tree.insertNode("Carlos");
        tree.insertNode("Eskar");

        System.out.println("\n\nIMPRESO:");
        tree.printRecursive();

        System.out.println("\n\nBUSCANDO NODOS: ");
        System.out.println("Buscando la cadena: 'Federico': " + (tree.searchNode("Federico") != null ? "ENCONTRADO" : "NO ENCONTRADO"));
        System.out.println("Buscando la cadena 'X': " + (tree.searchNode("X") != null ? "ENCONTRADO" : "NO ENCONTRADO"));


    }
}
