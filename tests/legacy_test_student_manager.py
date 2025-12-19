import unittest
import os
from app import StudentManager, Student

class TestStudentManager(unittest.TestCase):

    def setUp(self):
        # Create a temporary test file
        self.filename = "test_students.txt"
        with open(self.filename, "w") as f:
            f.write("1,test@gmail.com,1234,Ahmed,20,3A,01011111111\n")

        self.manager = StudentManager(self.filename)

    def tearDown(self):
        # Delete the temporary file
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_login_student(self):
        s = self.manager.login_student("test@gmail.com", "1234")
        self.assertIsNotNone(s)
        self.assertEqual(s.name, "Ahmed")

    def test_save_students(self):
        s = self.manager.get_student_by_id("1")
        s.update_info("Ali", "01222222222")
        self.manager.save_students()

        with open(self.filename, "r") as f:
            line = f.read().strip()
        self.assertIn("Ali", line)
        self.assertIn("01222222222", line)

if __name__ == "__main__":
    unittest.main()
