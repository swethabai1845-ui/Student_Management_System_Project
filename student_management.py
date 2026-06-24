import csv

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        name = input("Enter Student Name:")
        roll = input("Enter Roll Number:")
        course = input("Enter Course:")
        
        with open("students.csv","a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name,roll, course])

            print("Student Added Successfully!")
    elif choice == "2":
        try:
            with open("students.csv",'r') as file:
                reader = csv.reader(file)
                print("\nStudents List")
                for row in reader:print(row)
        except FileNotFoundError:print("No Student records found")
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid Choice")
             


