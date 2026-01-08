// MainApp.java
// Entry point of the application

import java.util.Scanner;

public class MainApp {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Polymorphism: abstract reference
        EmployeeOperations service = new EmployeeService(sc);

        int choice;

        do {
            System.out.println("1. Add Employee");
            System.out.println("2. Display Employee");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();

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
                    System.out.println("Invalid Choice\n");
            }

        } while (choice != 3);

        // Optional in small programs
        sc.close();
    }
}


// Employee.java
// Stores employee details using encapsulation

public class Employee {

    private int empId;
    private String empName;
    private double empSalary;

    public Employee(int empId, String empName, double empSalary) {
        this.empId = empId;
        this.empName = empName;
        this.empSalary = empSalary;
    }

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
// Abstract class defining employee-related rules

public abstract class EmployeeOperations {

    public abstract void addEmployee();

    public abstract void displayEmployees();
}


// EmployeeService.java
// Implements abstract methods and manages employee data

import java.util.Scanner;

public class EmployeeService extends EmployeeOperations {

    private Employee[] employees = new Employee[100];
    private int count = 0;

    // Shared Scanner reference
    private Scanner sc;

    // Constructor receives Scanner from main
    public EmployeeService(Scanner sc) {
        this.sc = sc;
    }

    @Override
    public void addEmployee() {

        System.out.print("Enter Employee ID: ");
        int id = sc.nextInt();
        sc.nextLine(); // clear buffer

        System.out.print("Enter Employee Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Employee Salary: ");
        double salary = sc.nextDouble();

        employees[count++] = new Employee(id, name, salary);

        System.out.println("Employee Added Successfully\n");
    }

    @Override
    public void displayEmployees() {

        if (count == 0) {
            System.out.println("No Employees Found\n");
            return;
        }

        System.out.println("ID\tName\tSalary");
        System.out.println("-------------------------");

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
