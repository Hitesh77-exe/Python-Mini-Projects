Class = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88
}

def add_student(name, score):
    Class[name] = score
    print(f"{name}'s grade updated to {score}")

def print_scores():
    for student, score in Class.items():
        print(f"{student}: {score}")
    print("-------------------")

while True:
    print("\n1. Add/Update Student  2. Print Grades  3. Quit")
    choice = input("Choose any one option to proceed: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        score = int(input("Enter score: "))
        add_student(name, score)
    elif choice == '2':
        print_scores()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")