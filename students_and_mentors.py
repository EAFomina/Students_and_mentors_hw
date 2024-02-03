class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

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
        return round(sum(all_grades) / len(all_grades), 2)
    
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
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)
    
    def _average_grade(self):
        all_grades = []
        for value in self.grades.values():
            all_grades.extend(value)
        return round(sum(all_grades) / len(all_grades), 2)
    
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
        
def course_average_grade(student_or_lecturer_list, course_name):
    all_course_grades = []
    for member in student_or_lecturer_list:
        if course_name in member.grades:
            course_grades = member.grades.get(course_name)
            all_course_grades.extend(course_grades)
    print(round(sum(all_course_grades) / len(all_course_grades), 2))

student_1 = Student('Emma', 'Bunny', 'f')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Steven', 'Smith', 'm')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']
 
py_reviewer = Reviewer('Samuel', 'Jackson')
py_reviewer.courses_attached += ['Python']

git_reviewer = Reviewer('Amanda', 'Kirk')
git_reviewer.courses_attached += ['Git']

py_lecturer_1 = Lecturer('Frank', 'Bowie')
py_lecturer_1.courses_attached += ['Python'] 

py_lecturer_2 = Lecturer('Eton', 'Young')
py_lecturer_2.courses_attached += ['Python']

student_1.rate_lect(py_lecturer_1, 'Python', 10)
student_1.rate_lect(py_lecturer_2, 'Python', 7)
student_1.rate_lect(py_lecturer_1, 'Python', 10)
student_1.rate_lect(py_lecturer_2, 'Python', 8)
 
student_2.rate_lect(py_lecturer_1, 'Python', 8)
student_2.rate_lect(py_lecturer_2, 'Python', 9)
student_2.rate_lect(py_lecturer_1, 'Python', 7)
student_2.rate_lect(py_lecturer_2, 'Python', 10)

py_reviewer.rate_hw(student_1, 'Python', 6)
py_reviewer.rate_hw(student_2, 'Python', 9)
py_reviewer.rate_hw(student_1, 'Python', 10)
py_reviewer.rate_hw(student_2, 'Python', 8)
py_reviewer.rate_hw(student_1, 'Python', 9)
py_reviewer.rate_hw(student_2, 'Python', 9)

git_reviewer.rate_hw(student_1, 'Git', 10)
git_reviewer.rate_hw(student_2, 'Git', 10)
git_reviewer.rate_hw(student_1, 'Git', 9)
git_reviewer.rate_hw(student_2, 'Git', 7)
git_reviewer.rate_hw(student_1, 'Git', 10)
git_reviewer.rate_hw(student_2, 'Git', 4)

print(student_1)
print(student_2)
print(py_reviewer)
print(git_reviewer)
print(py_lecturer_1)
print(py_lecturer_2)

print(student_1 == student_2)
print(py_lecturer_1 > py_lecturer_2)

course_average_grade(Student.student_list, 'Python')
course_average_grade(Lecturer.lecturer_list, 'Python')