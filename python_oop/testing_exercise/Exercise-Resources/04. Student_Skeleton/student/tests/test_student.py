from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Kiko')

    def test_if_init_works_with_no_courses_added_upon_initialisation(self):
        self.assertEqual('Kiko', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_if_init_works_with_courses_added_upon_initialisation(self):
        using = Student('Gogo', {'Python_basics': 'Abc'})
        self.assertEqual('Gogo', using.name)
        self.assertEqual({'Python_basics': 'Abc'}, using.courses)

    def test_enroll_method_if_course_already_added(self):
        self.student.enroll('Python_fundamentals', 'ABC', 'B')
        result = self.student.enroll('Python_fundamentals', 'SOLID')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'Python_fundamentals': ['S', 'O', 'L', 'I', "D"]}, self.student.courses)

    def test_enroll_method_if_notes_equal_to_empty_string(self):
        result = self.student.enroll('Python_fundamentals', 'SOLID', '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'Python_fundamentals': 'SOLID'}, self.student.courses)

    def test_enroll_method_if_notes_equal_to_y_string(self):
        result = self.student.enroll('Python_fundamentals', 'SOLID', 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'Python_fundamentals': 'SOLID'}, self.student.courses)

    def test_enroll_method_if_adding_new_course(self):
        result = self.student.enroll('Python_fundamentals', 'SOLID', 'B')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({'Python_fundamentals': []}, self.student.courses)

    def test_add_notes_works_with_correct_data_provided(self):
        self.student.enroll('Python_fundamentals', 'SOLID', 'B')
        result = self.student.add_notes('Python_fundamentals', 'ABC')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'Python_fundamentals': ['ABC']}, self.student.courses)

    def test_add_notes_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python_fundamentals', 'ABC')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_if_leave_course_method_works_with_correct_data_provided(self):
        self.student.enroll('Python_fundamentals', 'SOLID', 'B')
        result = self.student.leave_course('Python_fundamentals')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_if_leave_course_method_raises_with_incorrect_data_provided(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python_fundamentals')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
