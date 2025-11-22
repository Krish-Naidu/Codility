import unittest
from student_class import Subject, Student


class TestSubject(unittest.TestCase):
    """Test the Subject class"""
    
    def test_subject_creation(self):
        # Test creating a subject
        math = Subject("Math", 85)
        
        # Check name and marks are stored correctly
        self.assertEqual(math.name, "Math")
        self.assertEqual(math.marks, 85)
    
    def test_subject_different_marks(self):
        # Test with different values
        science = Subject("Science", 92)
        
        self.assertEqual(science.name, "Science")
        self.assertEqual(science.marks, 92)


class TestStudent(unittest.TestCase):
    """Test the Student class"""
    
    def test_student_creation(self):
        # Test creating a student
        student = Student()
        
        # Check initial values
        self.assertIsNone(student.id)
        self.assertIsNone(student.subject1)
        self.assertIsNone(student.subject2)
        self.assertIsNone(student.subject3)
    
    def test_student_with_subjects(self):
        # Create a student
        student = Student()
        student.id = 1
        
        # Add subjects
        student.subject1 = Subject("Math", 80)
        student.subject2 = Subject("Science", 90)
        student.subject3 = Subject("English", 70)
        
        # Check subjects are assigned
        self.assertEqual(student.subject1.name, "Math")
        self.assertEqual(student.subject1.marks, 80)
        self.assertEqual(student.subject2.name, "Science")
        self.assertEqual(student.subject2.marks, 90)
        self.assertEqual(student.subject3.name, "English")
        self.assertEqual(student.subject3.marks, 70)
    
    def test_calculate_percentage(self):
        # Create a student with known marks
        student = Student()
        student.subject1 = Subject("Math", 80)
        student.subject2 = Subject("Science", 90)
        student.subject3 = Subject("English", 70)
        
        # Total = 80 + 90 + 70 = 240
        # Percentage = (240 / 300) * 100 = 80%
        percentage = student.calculate_percentage()
        
        self.assertEqual(percentage, 80.0)
    
    def test_calculate_percentage_perfect_score(self):
        # Test with perfect scores
        student = Student()
        student.subject1 = Subject("Math", 100)
        student.subject2 = Subject("Science", 100)
        student.subject3 = Subject("English", 100)
        
        # Percentage should be 100%
        percentage = student.calculate_percentage()
        
        self.assertEqual(percentage, 100.0)
    
    def test_calculate_percentage_zero_marks(self):
        # Test with zero marks
        student = Student()
        student.subject1 = Subject("Math", 0)
        student.subject2 = Subject("Science", 0)
        student.subject3 = Subject("English", 0)
        
        # Percentage should be 0%
        percentage = student.calculate_percentage()
        
        self.assertEqual(percentage, 0.0)
    
    def test_calculate_percentage_different_values(self):
        # Test with the example from the main code
        student = Student()
        student.subject1 = Subject("Math", 85)
        student.subject2 = Subject("Science", 92)
        student.subject3 = Subject("English", 78)
        
        # Total = 85 + 92 + 78 = 255
        # Percentage = (255 / 300) * 100 = 85%
        percentage = student.calculate_percentage()
        
        self.assertEqual(percentage, 85.0)


# Run the tests
if __name__ == "__main__":
    unittest.main()
