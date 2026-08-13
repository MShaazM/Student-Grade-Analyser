import matplotlib.pyplot as plt

def calculate_gpa(marks):
    total = sum(marks.values())
    percentage = total / len(marks)
    return percentage

def generate_chart(student_name, marks):
    subjects = list(marks.keys())
    scores = list(marks.values())

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, scores, color='skyblue', edgecolor='black')
    plt.title(f"Academic Performance - {student_name}")
    plt.xlabel("Subjects")
    plt.ylabel("Marks (Out of 100)")
    plt.ylim(0, 100)
    plt.axhline(40, color='red', linestyle='--', label='Passing Mark (40)')
    plt.legend()
    
    plt.savefig(f"{student_name}_performance.png")
    print(f"Chart saved as {student_name}_performance.png")
    plt.show()

student_data = {
    "Data Structures": 85,
    "Python Programming": 92,
    "Web Basics": 78,
    "Applied Maths": 68,
    "AI Fundamentals": 88
}

student_name = "Shaaz Memon"
gpa = calculate_gpa(student_data)

print(f"Student: {student_name}")
print(f"Average Percentage: {gpa:.2f}%")
generate_chart(student_name, student_data)import matplotlib.pyplot as plt

def calculate_gpa(marks):
    total = sum(marks.values())
    percentage = total / len(marks)
    return percentage

def generate_chart(student_name, marks):
    subjects = list(marks.keys())
    scores = list(marks.values())

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, scores, color='skyblue', edgecolor='black')
    plt.title(f"Academic Performance - {student_name}")
    plt.xlabel("Subjects")
    plt.ylabel("Marks (Out of 100)")
    plt.ylim(0, 100)
    plt.axhline(40, color='red', linestyle='--', label='Passing Mark (40)')
    plt.legend()
    
    # Save chart as image
    plt.savefig(f"{student_name}_performance.png")
    print(f"Chart saved as {student_name}_performance.png")
    plt.show()

student_data = {
    "Data Structures": 85,
    "Python Programming": 92,
    "Web Basics": 78,
    "Applied Maths": 68,
    "AI Fundamentals": 88
}

student_name = "Shaaz Memon"
gpa = calculate_gpa(student_data)

print(f"Student: {student_name}")
print(f"Average Percentage: {gpa:.2f}%")
generate_chart(student_name, student_data)