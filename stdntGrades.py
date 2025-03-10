
# NOTE 
# THAT DUE TO SOME ISSUES RELATED TO FLUSH POINTS, THIS CODE IS CURRENTLY NOT RUNNING IN VS-CODE, PLEASE TRY ONLINE CO,PILERS LIKE Programiz OR ANY TOHER OF YOUR CHOICE.

# Imports upto date time and date
import datetime

# Function to capture student details and calculate final mark
def calculate_final_mark():
    print("\n===== STUDENT GRADING SYSTEM =====\n")

    # Capture student details
    student = get_student_details()

    print("\n--- Enter Student Marks ---\n")
    test1 = get_valid_marks("Enter Test 1 marks (out of 100): ", 100)
    test2 = get_valid_marks("Enter Test 2 marks (out of 100): ", 100)
    coursework = get_valid_marks("Enter Coursework marks (out of 100): ", 100)
    final_exam = get_valid_marks("Enter Final Exam marks (out of 100): ", 100)

    # Pick the best two scores from test1, test2, and coursework
    best_two = sorted([test1, test2, coursework], reverse=True)[:2]

    # Compute total final marks
    total_marks = (sum(best_two)/2 * 0.4) + (final_exam * 0.6)

    # Determine grade
    grade = get_grade(total_marks)

    # Display result
    display_result(student, total_marks, grade)

# Function to capture student details
def get_student_details():

    # The .script method used bellow removes any leading (spaces at the start) and trailing (spaces at the end) whitespace from the input.
    # Example:
    # text = "   Allan James   "
    # print(text.strip())  /// Output: "Allan James"

    # .title() capitalizes the first letter of each word in a string while converting the rest to lowercase.
    # Example:
    # text = "aLLan jaMes"
    # print(text.title())  # Output: "Allan James"

    name = input("Enter student name: ").strip().title()
    age = get_valid_integer("Enter age: ", min_value=10, max_value=100)
    gender = get_valid_gender("Enter gender (Male/Female): ")
    program = input("Enter program: ").strip().title()
    year = get_valid_integer("Enter year of study: ", min_value=1)
    faculty = input("Enter faculty: ").strip().title()
    dob = get_valid_date("Enter date of birth (YYYY-MM-DD): ")

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "program": program,
        "year": year,
        "faculty": faculty,
        "dob": dob,
    }

# Function to display the final result
def display_result(student, total_marks, grade):
    print("\n===== FINAL RESULT =====")
    print(f"📌 Student: {student['name']} ({student['gender']}, Age: {student['age']})")
    print(f"🎓 Program: {student['program']} ({student['faculty']})")
    print(f"📅 Year: {student['year']}")
    print(f"📊 Final Mark: {total_marks}/100")
    print(f"🏅 Grade: {grade}")
    print("========================\n")

# Function to get a valid integer input
def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            else:
                print(f"⚠ Please enter a valid number between {min_value} and {max_value}.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Function to get a valid date input
def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format! Please enter in YYYY-MM-DD format.")

# Function to get valid marks input
def get_valid_marks(prompt, max_marks):
    while True:
        try:
            marks = float(input(prompt))
            if 0 <= marks <= max_marks:
                return marks
            else:
                print(f"⚠ Invalid marks! Enter a value between 0 and {max_marks}.")
        except ValueError:
            print("❌ Invalid input! Enter a numeric value.")

# Function to get a valid gender input
def get_valid_gender(prompt):
    while True:

        # .capitalize() converts the first letter of the entire string to uppercase and makes all other letters lowercase.
        # Example:
        # text = "aLlaN JAmes"
        # print(text.capitalize())  # Output: "Allan james"

        gender = input(prompt).strip().capitalize()
        if gender in ["Male", "Female"]:
            return gender
        print("❌ Invalid input! Please enter 'Male' or 'Female'.")

# Function to determine grade
def get_grade(marks):
    if marks >= 80:
        return "A (Excellent) 🎖"
    elif marks >= 70:
        return "B (Good) 👍"
    elif marks >= 60:
        return "C (Satisfactory) ✅"
    elif marks >= 50:
        return "D (Pass) ⚠"
    else:
        return "F (Fail) ❌"
        
# Run the program
calculate_final_mark()


