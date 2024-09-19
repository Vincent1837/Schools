import csv

# File paths for the CSVs
student_file = 'students.csv'
course_file = 'courses.csv'
grade_file = 'grades.csv'

# Function to add student basic information
def add_student(name, student_id):
    with open(student_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, student_id])
    print(f"Student {name} with ID {student_id} added.")

# Function to add course basic information
def add_course(course_name, course_id):
    with open(course_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([course_name, course_id])
    print(f"Course {course_name} with ID {course_id} added.")

# Function to add student grades
def add_grade(student_id, course_id, grade):
    with open(grade_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, course_id, grade])
    print(f"Grade {grade} for student ID {student_id} in course {course_id} added.")

# Function to display all grades for a given student name
def display_grades(student_name):
    student_id = None
    with open(student_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_name:
                student_id = row[1]
                break
    
    if student_id:
        print(f"Grades for {student_name} (ID: {student_id}):")
        with open(grade_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    print(f"Course ID: {row[1]}, Grade: {row[2]}")
    else:
        print(f"Student {student_name} not found.")

# Main function to interact with the user
def main():
    while True:
        print("\nMenu:")
        print("1. Add student basic information")
        print("2. Add course basic information")
        print("3. Add student grade")
        print("4. Display student grades")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == 'A':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            add_student(name, student_id)
        elif choice == 'B':
            course_name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            add_course(course_name, course_id)
        elif choice == 'C':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = input("Enter grade: ")
            add_grade(student_id, course_id, grade)
        elif choice == 'D':
            student_name = input("Enter student name: ")
            display_grades(student_name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
