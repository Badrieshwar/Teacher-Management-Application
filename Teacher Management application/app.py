import json

class TeacherManagementApp:
    def __init__(self):
        self.teachers = []
        self.load_data()

    def load_data(self):
        try:
            with open('teachers_data.json', 'r') as file:
                self.teachers = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with an empty list
            self.teachers = []

    def save_data(self):
        with open('teachers_data.json', 'w') as file:
            json.dump(self.teachers, file, indent=2)

    def show_all_teachers(self):
        for teacher in self.teachers:
            print(teacher)

    def add_teacher(self, teacher_data):
        self.teachers.append(teacher_data)
        self.save_data()

    def filter_teachers_by_age(self, age):
        filtered_teachers = [teacher for teacher in self.teachers if teacher['age'] == age]
        for teacher in filtered_teachers:
            print(teacher)

    def filter_teachers_by_classes(self, num_classes):
        filtered_teachers = [teacher for teacher in self.teachers if teacher['num_classes'] == num_classes]
        for teacher in filtered_teachers:
            print(teacher)

    def search_teacher(self, full_name):
        for teacher in self.teachers:
            if teacher['full_name'].lower() == full_name.lower():
                print(teacher)
                return
        print("Teacher not found.")

    def update_teacher(self, full_name, updated_data):
        for teacher in self.teachers:
            if teacher['full_name'].lower() == full_name.lower():
                teacher.update(updated_data)
                self.save_data()
                print("Teacher record updated.")
                return
        print("Teacher not found.")

    def delete_teacher(self, full_name):
        for teacher in self.teachers:
            if teacher['full_name'].lower() == full_name.lower():
                self.teachers.remove(teacher)
                self.save_data()
                print("Teacher record deleted.")
                return
        print("Teacher not found.")


# Example of using the TeacherManagementApp class:

app = TeacherManagementApp()

while True:
    print("\nTeacher Management Application")
    print("1. Show all teachers")
    print("2. Add a teacher")
    print("3. Filter teachers by age")
    print("4. Filter teachers by number of classes")
    print("5. Search for a teacher")
    print("6. Update a teacher's record")
    print("7. Delete a teacher")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        app.show_all_teachers()
    elif choice == '2':
        teacher_data = {
            'full_name': input("Enter full name: "),
            'age': int(input("Enter age: ")),
            'dob': input("Enter date of birth: "),
            'num_classes': int(input("Enter number of classes: "))
        }
        app.add_teacher(teacher_data)
    elif choice == '3':
        age = int(input("Enter age to filter teachers: "))
        app.filter_teachers_by_age(age)
    elif choice == '4':
        num_classes = int(input("Enter number of classes to filter teachers: "))
        app.filter_teachers_by_classes(num_classes)
    elif choice == '5':
        full_name = input("Enter full name to search for: ")
        app.search_teacher(full_name)
    elif choice == '6':
        full_name = input("Enter full name to update: ")
        updated_data = {
            'age': int(input("Enter updated age: ")),
            'dob': input("Enter updated date of birth: "),
            'num_classes': int(input("Enter updated number of classes: "))
        }
        app.update_teacher(full_name, updated_data)
    elif choice == '7':
        full_name = input("Enter full name to delete: ")
        app.delete_teacher(full_name)
    elif choice == '8':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
