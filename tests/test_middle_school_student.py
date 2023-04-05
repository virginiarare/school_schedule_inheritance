from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    name = "Timmy"
    grade = "Ninth"
    classes = ["Math", "Science", "Chemistry", "Art"]

    timmy = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)

    assert timmy.name == name
    assert timmy.grade == grade
    assert timmy.classes == classes
    assert len(timmy.classes) == 4
    assert timmy.gets_transportation


# def test_middle_school_student_summary_with_transportation():
#     pass

# def test_middle_school_student_summary_without_transportation():
#     pass
