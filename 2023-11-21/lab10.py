from student import Student
import doctest

def get_students(filename:str) -> list[Student]: 
    """
    Takes a file that has the student numbers of each student and their grade
    on each line, separated by commas
    Will return a list of student objects created by the values in the file
    >>> get_students('student_data.csv')
    [Student('V00123456', '89'), Student('V00123457', '99'),\
 Student('V00123458', '30'), Student('V00123459', '78')]
    >>> get_students('empty.txt')
    []
    """
    students = []
    with open(filename, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            sid, grade = line.split(',')
            students.append(Student(sid, int(grade)))
    return students


def get_classlist(students:list[Student]) -> list[str]:
    """
    Takes a list of Students and returns the list of sids of the students
    >>> get_classlist([])
    []
    >>> get_classlist([Student('V00123456', '89'), Student('V00123457', '99'),\
      Student('V00123458', '30'), Student('V00123459', '78')])
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']
    """
    classlist = []
    for student in students:
        classlist.append(student.get_sid())
    return classlist


def count_above(students:list[Student], threshold:int) -> int:
    """
    Counts the number of instances of the student class with grades above the
    threshold
    >>> count_above([], 50)
    0
    >>> count_above([Student('V00123456', '89'), Student('V00123457', '99'),\
      Student('V00123458', '30'), Student('V00123459', '78')], 80)
    2
    >>> count_above([Student('V00123456', '89'), Student('V00123457', '99'),\
      Student('V00123458', '30'), Student('V00123459', '78')], 99)
    0
    >>> count_above([Student('V00123456', '89'), Student('V00123457', '99'),\
      Student('V00123458', '30'), Student('V00123459', '78')], 10)
    4
    """
    ppl_above_threshold = 0
    for student in students:
        if student.is_grade_above(threshold):
            ppl_above_threshold += 1
    return ppl_above_threshold


def get_average_grade(students:list[Student]) -> float:
    """
    Precondition: students == True
    Returns the average grade in a list of students
    >>> get_average_grade([Student('V00123456', '89'), Student('V00123457', '99'),\
      Student('V00123458', '30'), Student('V00123459', '78')])
    74.0
    """
    total_grade = 0
    for student in students:
        total_grade += student.get_grade()
    return total_grade / len(students)


