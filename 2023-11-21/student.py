import doctest

class Student:
    """ Student with unique id (sid) and current grade (grade)"""

    def __init__(self, sid: str, grade: int) -> None:
        """ initializes an instance of a Student with sid and grade
        >>> stdnt = Student('V00123456', 89)
        """
        self.__sid = sid
        self.__grade = grade

    def __str__(self) -> str:
        """ return a formatted string with sid and grade of self Student
        >>> stdnt = Student('V00123456', 89)
        >>> str(stdnt)
        'V00123456: 89/100'
        """
        return f'{self.__sid}: {self.__grade}/100'

    def __repr__(self) -> str:
        """ return a formatted string  with student attributes
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt
        Student('V00123456', 89)
        """        
        return f'Student({repr(self.__sid)}, {repr(self.__grade)})'
    
    def __eq__(self, other: 'Student') -> str:
        """ returns True if sid of self and other are equal
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1_eq = Student('V00123456', 89)
        >>> stdnt1_noteq = Student('V00123457', 89)
        >>> stdnt1 == stdnt1
        True
        >>> stdnt1 == stdnt1_eq
        True
        >>> stdnt1 == stdnt1_noteq
        False
        """
        return self.__sid == other.__sid
    
    def get_sid(self) -> str:
        """
        Returns the SID of the instance of the Student class
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1.get_sid()
        'V00123456'
        """
        return self.__sid

    def get_grade(self) -> int:      
        """
        Returns the grade of the instance of the Student class
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1.get_grade()
        89
        """
        return int(self.__grade)

    def set_grade(self, grade) -> None:
        """
        Sets the Grade of the instance of the Student class to the given grade
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1.get_grade()
        89
        >>> stdnt1.set_grade(92)
        >>> stdnt1.get_grade()
        92
        """
        self.__grade = grade

    def is_grade_above(self, threshold:int) -> bool:
        """
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1.is_grade_above(89)
        False
        >>> stdnt1.is_grade_above(88)
        True
        """
        return self.get_grade() > threshold
