// Employee.java
// This class represents an Employee entity and stores employee details

public class Employee {

    // Private variables to enforce encapsulation
    private int empId;
    private String empName;
    private double empSalary;

    // Constructor to initialize employee object
    public Employee(int empId, String empName, double empSalary) {
        this.empId = empId;
        this.empName = empName;
        this.empSalary = empSalary;
    }

    // Getter methods to access private variables
    public int getEmpId() {
        return empId;
    }

    public String getEmpName() {
        return empName;
    }

    public double getEmpSalary() {
        return empSalary;
    }
}



// EmployeeOperations.java
// Abstract class that defines rules for employee management

public abstract class EmployeeOperations {

    // Abstract method to add employee
    public abstract void addEmployee();

    // Abstract method to display employees
    public abstract void displayEmployees();
}


// EmployeeService.java
// This class extends the abstract class and implements its methods

import java.util.Scanner;

public class EmployeeService extends EmployeeOperations {

    // Array to store Employee objects
    private Employee[] employees = new Employee[100];
    private int count = 0;

    // Scanner object for user input
    Scanner sc = new Scanner(System.in);

    // Implementation of addEmployee()
    @Override
    public void addEmployee() {

        System.out.print("Enter Employee ID: ");
        int id = sc.nextInt();
        sc.nextLine(); // consume newline

        System.out.print("Enter Employee Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Employee Salary: ");
        double salary = sc.nextDouble();

        // Creating Employee object
        employees[count] = new Employee(id, name, salary);
        count++;

        System.out.println("Employee Added Successfully\n");
    }

    // Implementation of displayEmployees()
    @Override
    public void displayEmployees() {

        if (count == 0) {
            System.out.println("No Employee Records Found\n");
            return;
        }

        System.out.println("ID\tName\tSalary");
        System.out.println("---------------------------");

        // Loop to display all employee details
        for (int i = 0; i < count; i++) {
            System.out.println(
                    employees[i].getEmpId() + "\t" +
                    employees[i].getEmpName() + "\t" +
                    employees[i].getEmpSalary()
            );
        }
        System.out.println();
    }
}


// MainApp.java
// Main class that contains menu-driven logic

import java.util.Scanner;

public class MainApp {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Polymorphism: abstract class reference
        EmployeeOperations service = new EmployeeService();

        int choice;

        // Program runs continuously until user selects Exit
        do {
            System.out.println("1. Add Employee");
            System.out.println("2. Display Employee");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();

            // Switch case for menu operations
            switch (choice) {
                case 1:
                    service.addEmployee();
                    break;

                case 2:
                    service.displayEmployees();
                    break;

                case 3:
                    System.out.println("Exiting Program...");
                    break;

                default:
                    System.out.println("Invalid Choice! Please try again.\n");
            }

        } while (choice != 3);

        sc.close();
    }
}
