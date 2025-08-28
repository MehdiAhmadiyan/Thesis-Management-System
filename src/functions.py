import json
from src.models import User, Student, Professor, Course, Thesis

users_file = "data/users.json"
courses_file = "data/courses.json"
theses_file = "data/theses.json"

def read_from_json(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def write_to_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_users():
    users_data = read_from_json(users_file)
    users =[]

    for user in users_data:
        if user["role"] == "student":
            users.append(Student(user["id"], user["name"], user["password"], user["major"]))
        elif user["role"] == "professor":
            users.append(Professor(user["id"], user["name"], user["password"], user["mentoring_capacity"], user["examination_capacity"], user["major"]))
    return users

def load_courses():
    courses_data = read_from_json(courses_file)
    courses_list = []

    for course in courses_data:
        courses_list.append(Course(course["id"], course["title"], course["professor_id"], course["year"], \
        course["semester"], course["capacity"], course["resources"], course["session_numbers"], course["units"]))
    return courses_list

def load_theses():
    theses_data = read_from_json(theses_file)

    theses_list = []

    for thesis_item in theses_data:
        thesis = Thesis(thesis_item["thesis_id"], thesis_item["student_id"], thesis_item["course_id"], thesis_item["request_date"], thesis_item["status"])

        thesis.approval_date = thesis_item.get("approval_date")
        thesis.defense_date = thesis_item.get("defense_date")
        thesis.title = thesis_item.get("title")
        thesis.abstract = thesis_item.get("abstract")
        thesis.keywords = thesis_item.get("keywords")
        thesis.pdf_path = thesis_item.get("pdf_path")
        thesis.first_page_path = thesis_item.get("first_page_path")
        thesis.last_page_path = thesis_item.get("last_page_path")
        thesis.examiners = thesis_item.get("examiners")
        thesis.grades = thesis_item.get("grades")
        thesis.final_grade = thesis_item.get("final_grade")
        thesis.final_result = thesis_item.get("final_result")

        theses_list.append(thesis)

    return theses_list

def save_users(users_list):
    users_data_list = []
    for user in users_list:
        user_dict = {
                "id": user.user_id,
                "name": user.name,
                "password": user.password,
                "role": user.role,
                "major": user.major,
            }
        if user.role == "professor":
            user_dict["mentoring_capacity"] = user.mentoring_capacity
            user_dict["examination_capacity"] = user.examination_capacity
            
        users_data_list.append(user_dict)
        
    write_to_json(users_file, users_data_list)
    


def save_theses(theses_list):
    
    theses_list_prime = []

    for thesis in theses_list:
        thesis_dict = {
            "thesis_id": thesis.thesis_id,
            "student_id": thesis.student_id,
            "course_id": thesis.course_id,
            "request_date": thesis.request_date,
            "status": thesis.status,
            "approval_date": thesis.approval_date,
            "defense_date": thesis.defense_date,
            "title": thesis.title,
            "abstract": thesis.abstract,
            "keywords": thesis.keywords,
            "pdf_path": thesis.pdf_path,
            "first_page_path": thesis.first_page_path,
            "last_page_path": thesis.last_page_path,
            "examiners": thesis.examiners,
            "grades": thesis.grades,
            "final_grade": thesis.final_grade,
            "final_result": thesis.final_result
        }
        theses_list_prime.append(thesis_dict)

    write_to_json(theses_file, theses_list_prime)
    
    
def save_courses(courses_list):
    courses_list_prime = []
    
    for course in courses_list:
        course_dict = {
                "id": course.course_id,
                "title": course.title,
                "professor_id": course.professor_id,
                "capacity": course.capacity,
                "year": course.year,
                "semester": course.semester,
                "units": course.units,
                "session_numbers": course.session_numbers,
                "resources": course.resources
            }
        courses_list_prime.append(course_dict)
            
    write_to_json(courses_file, courses_list_prime)
    
    
