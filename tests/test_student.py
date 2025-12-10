import unittest
from app import Student

class TestStudent(unittest.TestCase):

    def test_update_info(self):
        s = Student("1", "test@test.com", "123", "Ali", "20", "3A", "01000000000")
        s.update_info("Omar", "01111111111")

        self.assertEqual(s.name, "Omar")
        self.assertEqual(s.phone, "01111111111")

if __name__ == "__main__":
    unittest.main()
