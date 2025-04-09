import matplotlib.pyplot as plt
import os

# Define quadrant labels
quadrant_labels = {
    (True, True): "Do First\n(Important & Urgent)",
    (True, False): "Do Later\n(Important but Not Urgent)",
    (False, True): "Delegate\n(Not Important but Urgent)",
    (False, False): "Eliminate\n(Not Important & Not Urgent)"
}

# Define quadrant positions
quadrant_positions = {
    (True, True): (0.5, 1.7),   # Moved UP (Y position) from 1.5 to 1.7 (Upper header)
    (True, False): (1.5, 1.7),
    (False, True): (0.5, 0.7),
    (False, False): (1.5, 0.7)
}

# Colors for each quadrant
colors = ["#ff6666", "#ffcc66", "#66b3ff", "#99e699"]

# Initialize task dictionary
tasks = {key: [] for key in quadrant_labels.keys()}

# Function to get user input for tasks with error checking
def get_user_tasks():
    while True:
        # Task input with validation
        task = input("\nEnter a task (or type 'done' to finish): ")
        if task.lower() == "done":
            break
        elif not task.strip():
            print("Error: Task cannot be empty. Please enter a valid task.")
            continue

        # Importance input with validation
        while True:
            important = input("Is it important? (yes/no): ").strip().lower()
            if important in ["yes", "no"]:
                important = important == "yes"
                break
            else:
                print("Error: Please enter 'yes' or 'no' for importance.")
        
        # Urgency input with validation
        while True:
            urgent = input("Is it urgent? (yes/no): ").strip().lower()
            if urgent in ["yes", "no"]:
                urgent = urgent == "yes"
                break
            else:
                print("Error: Please enter 'yes' or 'no' for urgency.")

        # Assign task to the correct quadrant
        tasks[(important, urgent)].append(task)

# Function to save tasks to a text file
def save_tasks_to_file(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for quadrant, task_list in tasks.items():
            file.write(f"Quadrant: {quadrant_labels[quadrant]}\n")
            for task in task_list:
                file.write(f"- {task}\n")
            file.write("\n")

# Function to load tasks from a text file
def load_tasks_from_file(filename="tasks.txt"):
    tasks = {key: [] for key in quadrant_labels.keys()}
    try:
        if os.path.exists(filename):
            print(f"Loading tasks from {filename}...")
            with open(filename, "r") as file:
                lines = file.readlines()
                current_quadrant = None
                for line in lines:
                    line = line.strip()
                    if line.startswith("Quadrant:"):
                        # Extract the quadrant label from the file
                        file_quadrant_label = line[len("Quadrant: "):].strip()
                        # Match the file quadrant label with the quadrant_labels dictionary
                        for key, label in quadrant_labels.items():
                            if file_quadrant_label == label.replace("\n", " ").strip():
                                current_quadrant = key
                                break
                    elif line.startswith("-"):
                        # Task line
                        task = line[2:].strip()
                        if current_quadrant:
                            tasks[current_quadrant].append(task)
        else:
            print(f"{filename} not found. Creating a new one.")
    except Exception as e:
        print(f"Error loading tasks: {e}")

    return tasks

# Function to remove a task from the list
def remove_task(tasks, filename="tasks.txt"):
    # Display current tasks in the matrix
    print("\nCurrent tasks in the Prioritization Matrix:")
    task_counter = {}
    for idx, (key, task_list) in enumerate(tasks.items(), start=1):
        print(f"\n{quadrant_labels[key]}:")
        if task_list:
            for i, task in enumerate(task_list, start=1):
                print(f"{i}. {task}")
                task_counter[(key, i)] = task  # Track task number
        else:
            print("No tasks in this quadrant.")

    # Ask the user to select a task to remove
    while True:
        quadrant_input = input("\nWhich quadrant would you like to remove a task from? (Enter the quadrant number: 1-4 or 'done' to cancel): ").strip()
        if quadrant_input.lower() == "done":
            print("Task removal cancelled.")
            return

        try:
            quadrant_input = int(quadrant_input)
            if quadrant_input < 1 or quadrant_input > 4:
                print("Please enter a valid quadrant number (1-4).")
                continue
        except ValueError:
            print("Invalid input. Please enter a number (1-4) or 'done'.")
            continue

        quadrant_key = list(quadrant_labels.keys())[quadrant_input - 1]
        task_list = tasks[quadrant_key]

        if not task_list:
            print("No tasks in this quadrant to remove.")
            continue

        # Ask the user to select a task number to remove
        task_input = input(f"\nWhich task would you like to remove from {quadrant_labels[quadrant_key]}? (Enter the task number): ").strip()
        try:
            task_input = int(task_input)
            if task_input < 1 or task_input > len(task_list):
                print("Invalid task number. Please choose a valid task.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
            continue

        # Remove the selected task
        removed_task = task_list.pop(task_input - 1)
        print(f"\n'{removed_task}' has been removed from the list.")

        # Break out of the loop after removing the task
        break

    # Re-display the matrix after task removal and update the text file
    save_tasks_to_file(tasks, filename)
    print("\nUpdated Prioritization Matrix:")
    display_prioritization_matrix(tasks)

# Function to display the updated prioritization matrix
def display_prioritization_matrix(tasks):
    # Create figure and axis for the updated matrix
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the quadrants
    ax.fill_between([0, 1], 1, 2, color=colors[0], alpha=0.7)
    ax.fill_between([1, 2], 1, 2, color=colors[1], alpha=0.7)
    ax.fill_between([0, 1], 0, 1, color=colors[2], alpha=0.7)
    ax.fill_between([1, 2], 0, 1, color=colors[3], alpha=0.7)

    # Add quadrant labels and tasks
    for key, pos in quadrant_positions.items():
        text = quadrant_labels[key] + "\n\n" + "\n".join(tasks[key])  # Combine label with tasks
        ax.text(pos[0], pos[1], text, ha='center', va='center', fontsize=10, fontweight='bold', color="black")

    # Set tick positions and labels
    ax.set_xticks([0.5, 1.5])
    ax.set_xticklabels(["Urgent", "Not Urgent"], fontsize=12, fontweight='bold')

    ax.set_yticks([0.5, 1.5])
    ax.set_yticklabels(["Important", "Not Important"], fontsize=12, fontweight='bold')

    # Set limits
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)

    # Set title
    ax.set_title("Prioritization Matrix", fontsize=14, fontweight='bold')

    # Hide spines and ticks
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(left=False, bottom=False)

    # Show the grid for reference
    ax.grid(True, linestyle="--", alpha=0.5)

    # Display the plot
    plt.show()

# Main menu for user interaction
def main_menu():
    global tasks
    tasks = load_tasks_from_file()  # Load tasks from file at the start
    while True:
        print("\n--- Prioritization Matrix Menu ---")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display the prioritization matrix")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ").strip()
        
        if choice == "1":
            get_user_tasks()  # Add a new task
            save_tasks_to_file(tasks)  # Save after adding task
        elif choice == "2":
            remove_task(tasks)  # Remove a task
        elif choice == "3":
            display_prioritization_matrix(tasks)  # Display the prioritization matrix
        elif choice == "4":
            save_tasks_to_file(tasks)  # Save and exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1-4.")

# Run the program
if __name__ == "__main__":
    # Start the main menu
    main_menu()