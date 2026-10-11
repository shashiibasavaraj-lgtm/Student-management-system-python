# Student Management - Mobile Version
students = []

while True:
    print("\n1. Add Student\n2. View All\n3. Search\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        marks = input("Enter Marks: ")
        students.append({"name":name, "roll":roll, "marks":marks})
        print("Student Added!")
    
    elif choice == '2':
        for s in students:
            print(f"{s['roll']} - {s['name']} - {s['marks']}")
    
    elif choice == '3':
        r = input("Enter Roll to Search: ")
        for s in students:
            if s['roll'] == r:
                print(f"Found: {s}")
    
    elif choice == '4':
        break
