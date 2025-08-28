class User:
    def __init__(self, user_id, name, password, role, major):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.role = role
        self.major = major

class Student(User):
    def __init__(self, user_id, name, password, major):
        super().__init__(user_id, name, password, role="student", major=major)

class Professor(User):
    def __init__(self, user_id, name, password, mentoring_capacity, examination_capacity, major):
        super().__init__(user_id, name, password, role="professor", major=major)
        self.mentoring_capacity = mentoring_capacity
        self.examination_capacity = examination_capacity

class Course:
    def __init__(self, course_id, title, professor_id, year, semester, capacity, resources, session_numbers, units):
        self.course_id = course_id
        self.title = title
        self.professor_id = professor_id
        self.year = year
        self.semester = semester
        self.capacity = capacity
        self.resources = resources
        self.session_numbers = session_numbers
        self.units = units

class Thesis:
    def __init__(self, thesis_id, student_id, course_id, request_date, status="pending_approval"):
        self.thesis_id = thesis_id
        self.student_id = student_id
        self.course_id = course_id
        self.request_date = request_date
        self.status = status

        self.approval_date = None
        self.defense_date = None
        self.title = None
        self.abstract = None
        self.keywords = None
        self.pdf_path = None
        self.first_page_path = None
        self.last_page_path = None
        self.examiners = {}
        self.grades = {}
        self.final_grade = None
        self.final_result = None

