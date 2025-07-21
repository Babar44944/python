Name = input("Enter Your Name: ")
father = input("Enter Your Father's Name: ")

marks = int(input("Enter Marks (0-100): "))

selected_group = ""
subjects = ""

if marks >= 70:
    print("\nYou are Able:")
    print("1. Pre-Engineering\n2. Pre-Medical")

    Student_group = int(input("Enter your Group (1 or 2): "))

    if Student_group == 1:
        selected_group = "Pre-Engineering"
        print("\nSelect your Subjects:")
        print("1. Math, English, Physics, Urdu, Pakistan Study")
        print("2. Math, English, Chemistry, Urdu, Pakistan Study")

        sub_1 = int(input("Select Your Option (1 or 2): "))

        if sub_1 == 1:
            subjects = "Math, English, Physics, Urdu, Pakistan Study"
        elif sub_1 == 2:
            subjects = "Math, English, Chemistry, Urdu, Pakistan Study"
        else:
            print("ERROR in subject selection.")
            subjects = "Invalid Selection"

    elif Student_group == 2:
        selected_group = "Pre-Medical"
        print("\nSelect your Subjects:")
        print("1. Biology, Zoology, English, Urdu, Pakistan Study, Chemistry")
        print("2. Biology, Zoology, English, Urdu, Botany, Physics")

        sub_2 = int(input("Select Your Option (1 or 2): "))

        if sub_2 == 1:
            subjects = "Biology, Zoology, English, Urdu, Pakistan Study, Chemistry"
        elif sub_2 == 2:
            subjects = "Biology, Zoology, English, Urdu, Botany, Physics"
        else:
            print("ERROR in subject selection.")
            subjects = "Invalid Selection"
    else:
        print("Invalid group selected.")
        selected_group = "None"
        subjects = "None"

else:
    print("You are not Able for Pre-Medical or Pre-Engineering.")
    selected_group = "None"
    subjects = "None"

# Shift Selection
print("\n==> NOW TIMING SHIFT <==")
print("1. Morning\n2. Evening\n3. Night")
shift = int(input("Select Shift (1, 2, or 3): "))

if shift == 1:
    shift_name = "Morning"
elif shift == 2:
    shift_name = "Evening"
elif shift == 3:
    shift_name = "Night"
else:
    shift_name = "Invalid Shift"
    
print("\nYour Admission Slip")
print("------------------------")
print("Name           :", Name)
print("Father Name    :", father)
print("Marks          :", marks)
print("Selected Group :", selected_group)
print("Subjects       :", subjects)
print("Shift          :", shift_name)
print("Status         : Admission Confirmed" if selected_group != "None" else "Status         : Not Eligible")
print("------------------------")
