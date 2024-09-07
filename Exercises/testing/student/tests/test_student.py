from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Test")
        self.s = Student("Test", {"course": []})

    def test_init_with_no_courses(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertIsInstance(self.student.courses, dict)

    def test_init_with_course(self):
        self.assertEqual("Test", self.s.name)
        self.assertEqual({"course": []}, self.s.courses)
        self.assertIsInstance(self.s.courses, dict)

    def test_enroll_with_existing_course_name(self):
        result = self.s.enroll("course", ["note1", "note2"])
        self.assertEqual({"course": ["note1", "note2"]}, self.s.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

        result = self.s.enroll("course", ["note3", "note4"], "N")
        self.assertEqual({"course": ["note1", "note2", "note3", "note4"]}, self.s.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_with_add_course_notes_Y_or_empty_and_no_existing_course(self):
        result = self.student.enroll("course_2", ["note1", "note2"], "Y")
        self.assertEqual({"course_2": ["note1", "note2"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_add_course_notes_empty_and_no_existing_course(self):
        result = self.student.enroll("course_3", ["note1", "note2"], "")
        self.assertEqual({"course_3": ["note1", "note2"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_no_existing_course_name(self):
        result = self.student.enroll("course_4", [], "no")
        self.assertEqual({"course_4": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_enroll_with_non_standard_add_course_notes(self):
        result = self.student.enroll("course_5", ["note1"], "some_value")
        self.assertEqual({"course_5": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_with_existing_course_name(self):
        result = self.s.add_notes("course", "Note_1")
        self.assertEqual({"course": ["Note_1"]}, self.s.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_with_empty_note(self):
        self.s.enroll("course_6", [])
        result = self.s.add_notes("course_6", "")
        self.assertEqual({"course_6": [""]}, self.s.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_with_no_existing_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.s.add_notes("course_1", "Note_1")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course_name(self):
        result = self.s.leave_course("course")
        self.assertEqual({}, self.s.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_multiple_courses(self):
        self.student.enroll("course_7", ["note1"])
        self.student.enroll("course_8", ["note2"])
        result = self.student.leave_course("course_7")
        self.assertEqual({"course_8": ["note2"]}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_no_existing_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("test_course")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
