import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class LibraryManagementSystem {

    // HashMap to store Book ID and Book Name
    private static HashMap<Integer, String> libraryBooks = new HashMap<>();

    // ArrayList to store borrowed Book IDs
    private static ArrayList<Integer> borrowedBooks = new ArrayList<>();

    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int choice;

        // Menu-driven program
        do {
            System.out.println("\n===== Library Management System =====");
            System.out.println("1. Add Book");
            System.out.println("2. Borrow Book");
            System.out.println("3. View Available Books");
            System.out.println("4. View Borrowed Books");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            // Validate integer input
            while (!scanner.hasNextInt()) {
                System.out.print("Invalid input! Enter a number: ");
                scanner.next();
            }

            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addBook();
                    break;

                case 2:
                    borrowBook();
                    break;

                case 3:
                    displayAvailableBooks();
                    break;

                case 4:
                    displayBorrowedBooks();
                    break;

                case 5:
                    System.out.println("Exiting Library Management System...");
                    break;

                default:
                    System.out.println("Invalid choice! Please select again.");
            }

        } while (choice != 5);

        scanner.close();
    }

    // Method to add a new book
    private static void addBook() {
        System.out.print("Enter Book ID: ");
        int bookId = scanner.nextInt();
        scanner.nextLine(); // consume newline

        // Prevent duplicate Book IDs
        if (libraryBooks.containsKey(bookId)) {
            System.out.println("Book ID already exists! Cannot add duplicate.");
            return;
        }

        System.out.print("Enter Book Name: ");
        String bookName = scanner.nextLine();

        libraryBooks.put(bookId, bookName);
        System.out.println("Book added successfully!");
    }

    // Method to borrow a book
    private static void borrowBook() {
        System.out.print("Enter Book ID to borrow: ");
        int bookId = scanner.nextInt();

        // Check if book exists
        if (!libraryBooks.containsKey(bookId)) {
            System.out.println("Book not found in library!");
            return;
        }

        // Check if book is already borrowed
        if (borrowedBooks.contains(bookId)) {
            System.out.println("Book is already borrowed!");
            return;
        }

        borrowedBooks.add(bookId);
        System.out.println("Book borrowed successfully!");
    }

    // Method to display available books
    private static void displayAvailableBooks() {
        System.out.println("\nAvailable Books:");

        boolean found = false;

        for (int bookId : libraryBooks.keySet()) {
            if (!borrowedBooks.contains(bookId)) {
                System.out.println("Book ID: " + bookId +
                        ", Book Name: " + libraryBooks.get(bookId));
                found = true;
            }
        }

        if (!found) {
            System.out.println("No available books at the moment.");
        }
    }

    // Method to display borrowed books
    private static void displayBorrowedBooks() {
        System.out.println("\nBorrowed Books:");

        if (borrowedBooks.isEmpty()) {
            System.out.println("No books have been borrowed.");
            return;
        }

        for (int bookId : borrowedBooks) {
            System.out.println("Book ID: " + bookId +
                    ", Book Name: " + libraryBooks.get(bookId));
        }
    }
}
