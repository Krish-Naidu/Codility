# Subject class - holds subject name and marks
class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


# Student class - holds 3 subject objects
class Student:
    
    def __init__(self):
        # Store 3 subject objects
        self.id = None
        self.subject1 = None
        self.subject2 = None
        self.subject3 = None
    
    def calculate_percentage(self):
        # Add all marks together from the 3 subject objects
        total_marks = self.subject1.marks + self.subject2.marks + self.subject3.marks
        
        # 3 subjects, each out of 100
        total_possible = 300
        
        # Calculate percentage
        percentage = (total_marks / total_possible) * 100
        
        return percentage


# Create student 1
student1 = Student()
student1.id = 1

# Create 3 subject objects for student 1
math = Subject("Math", 85)
science = Subject("Science", 92)
english = Subject("English", 78)

# Assign subjects to student 1
student1.subject1 = math
student1.subject2 = science
student1.subject3 = english


# Create student 2
student2 = Student()
student2.id = 2

# Create 3 subject objects for student 2
math = Subject("Math", 45)
science = Subject("Science", 42)
english = Subject("English", 90)

# Assign subjects to student 2
student2.subject1 = math
student2.subject2 = science
student2.subject3 = english


# Display percentages
print(student1.calculate_percentage())
print(student2.calculate_percentage())