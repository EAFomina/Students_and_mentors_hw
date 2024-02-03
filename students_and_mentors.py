class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def _average_grade(self):
        all_grades = []
        for value in self.grades.values():
            all_grades.extend(value)
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname}" 
                f"\nСредняя оценка за домашние задания: {self._average_grade()}"
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")
    
    def __eq__(self, other):
        return self._average_grade() == other._average_grade()
    
    def __lt__(self, other):
        return self._average_grade() < other._average_grade()
    
    def __gt__(self, other):
        return self._average_grade() > other._average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def _average_grade(self):
        all_grades = []
        for value in self.grades.values():
            all_grades.extend(value)
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname}" 
                f"\nСредняя оценка за лекции: {self._average_grade()}")
    
    def __eq__(self, other):
        return self._average_grade() == other._average_grade()
    
    def __lt__(self, other):
        return self._average_grade() < other._average_grade()
    
    def __gt__(self, other):
        return self._average_grade() > other._average_grade()

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
