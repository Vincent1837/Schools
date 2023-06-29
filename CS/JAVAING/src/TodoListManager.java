import java.util.*;

public class TodoListManager {
    public static void main(String[] args) {
        System.out.println("Hello user! This is a todo list manager.");
        TodoList list = new TodoList("Todo list");
        while (true) {
            list.printList();
            printWelcomeMsg();
            String input = getUserInput();
            switch (input.charAt(0)) {
                case 'a' -> list.addTask(new Task(input.substring(2)));
                case 'r' -> list.removeTask(Integer.parseInt(input.substring(2)) - 1);
                case 'm' -> list.changeTaskMark(Integer.parseInt(input.substring(2)) - 1);
                case 'x' -> System.exit(0);
            }

        }
    }
    
    static void printWelcomeMsg() {
        System.out.println("----------------------------------------------------------------------------");
        System.out.println("| To add a new task, please enter: a {task description}.                   |");
        System.out.println("| To remove a task, please enter: r {task index}.                          |");
        System.out.println("| To mark a task as completed or incompleted, please enter: m {task index}.|");
        System.out.println("| To exit the program, please enter: x.                                    |");
        System.out.println("----------------------------------------------------------------------------");
    }

    static String getUserInput() {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();
        return s;
    }

}

class TodoList {
    private String listName;
    private final ArrayList<Task> list = new ArrayList<Task> ();

    public TodoList (String listName) {
        this.listName = listName;
    }

    public String getListName () {
        return this.listName;
    }

    public ArrayList<Task> getList () {
        return this.list;
    }

    public void setListName (String listName) {
        this.listName = listName;
    }

    public void addTask (Task task) {
        list.add(task);
    }

    public void removeTask (int index) {
        list.remove(index);
    }

    public void changeTaskMark (int index) {
        Task t = list.get(index);
        t.setIsCompleted(!t.getIsCompleted());
    }

    public void printList () {
        System.out.println(this.listName);
        int counter = 1;
        for (Task task : this.list) {
            if (task.getIsCompleted()) {
                System.out.println("[ ]" + counter + ". " + task.getDescription()); 
            } else {
                System.out.println("[v]" + counter + ". " + task.getDescription());
            }
            counter += 1;
        }
        if (counter == 1) {
            System.out.println("The list is currently empty.");
        }
    }
}

class Task {
    private String description; 
    private boolean isCompleted;

    public Task (String description) {
        this.description = description;
        this.isCompleted = false;
    } 

    public String getDescription () {
        return this.description;
    }

    public boolean getIsCompleted () {
        return this.isCompleted;
    }

    public void setDescription (String description) {
        this.description = description;
    }
    
    public void setIsCompleted (boolean b) {
       this.isCompleted = b;
    }
}