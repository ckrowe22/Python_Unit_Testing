import unittest
from Assignment3 import Employee


class EasyTestCase01(unittest.TestCase):

    def setUp(self):
        self.emplObj = Employee('Chelsea', 'Rowe', 'Full', 35)

    def test_easy_input01(self):
        self.assertEqual(self.emplObj.empyName(), "Chelsea Rowe is a Full-time employee.")

    def test_easy_input02(self):
        self.assertEqual(self.emplObj.yearSalary(), 72800)

    def test_easy_input03(self):
        self.emplObj.category = "half"
        self.assertEqual(self.emplObj.yearSalary(), 36400)

    # testing an int input for first name
    def test_med_input01(self):
        with self.assertRaises(TypeError):
            Employee(40, 'Rowe', 'Full', 100)

    # testing an incorrect category
    def test_med_input02(self):
        with self.assertRaises(ValueError):
            Employee('Chelsea', 'Rowe', 'unknown', 50).yearSalary()

    # testing a negative number for salary
    def test_hard_input01(self):
        with self.assertRaises(ValueError):
            Employee('Chelsea', 'Rowe', 'Full', -50).yearSalary()


if __name__ == '__main__':
    unittest.main()
