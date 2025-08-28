import os
import shutil
from datetime import datetime, timedelta
from src.models import Thesis
from src.functions import write_to_json, theses_file, save_users, save_courses, save_theses


def upload_file(message, frmt, destination_dir):
    
    while True:
        source_dir = input(message)
        
        if not os.path.exists(source_dir):
            print("The path didn't find :( Please check the path and try again :)")
            continue
        
        if not source_dir.lower().endswith(frmt):
            print(f"Invalid file format!!! The file format should {frmt}")
            continue
        
        try:
            shutil.copy(source_dir, destination_dir)
            print("File uploaded successfully :)")
            return destination_dir
        except Exception as e:
            print(f"An error occured while doing the process of copying: {e}")
            return None
        
        
        

def request_thesis(student, all_courses, all_theses, all_users):

    for thesis in all_theses:
        if thesis.student_id == student.user_id and thesis.status in ["pending_approval", "approved"]:
            print("You have already have a thesis!!!!")
            return
    
    rejected_courses = []
    for thesis in all_theses:
        if thesis.student_id == student.user_id and thesis.status == "rejected":
            rejected_courses.append(thesis.course_id)
    
    available_courses = []
    for course in all_courses:
        course_professor = None
        for user in all_users:
            if user.user_id == course.professor_id:
                course_professor = user
                break
        
        if course.capacity > 0 and course.course_id not in rejected_courses and course_professor.major == student.major:
            available_courses.append(course)

    if len(available_courses) == 0:
        print("There is no available course with enough capacity :(")
        return

    print("Courses list:")
    for i, course in enumerate(available_courses):
        print(f"{i+1}) {course.title} (Professor ID: {course.professor_id})")

    while True:
        try:
            choice = int(input("Please enter the course id: "))
            if 1 <= choice <= len(available_courses):
                valid_course_id = choice
                print("Your request submitted :)")
                break
            else:
                print(f"Please enter a number between 1 and {len(available_courses)}")
        except ValueError:
            print("Please enter a valid course id!!!")

    selected_course = available_courses[valid_course_id - 1]

    if all_theses:
        new_thesis_id = max(t.thesis_id for t in all_theses) + 1
    else:
        new_thesis_id = 1

    request_time = datetime.now().isoformat()

    new_thesis = Thesis(new_thesis_id, student.user_id, selected_course.course_id, request_time, "pending_approval")

    all_theses.append(new_thesis)
    save_theses(all_theses)


def view_thesis_status(student, all_theses):

    for thesis in all_theses:
        if thesis.student_id == student.user_id:
            print(f"The status of your thesis is {thesis.status}")
            return

    print("You don't have any thesis in database!")


def request_defense(student, all_theses):

    student_thesis = None

    for thesis in all_theses:
        if thesis.student_id == student.user_id:
            student_thesis = thesis
            break

    if student_thesis:
        if student_thesis.status == "approved":

            approval_date = datetime.fromisoformat(student_thesis.approval_date).date()
            today_date = datetime.now().date()

            if today_date >= approval_date + timedelta(days=90):
                print("You can request for a defense :)")
                
                pdf_destination = "files/pdfs"
                image_destination = "files/images"
                
                pdf_path = upload_file("Please enter the path of your pdf file: ", ".pdf", pdf_destination)
                if not pdf_path:
                    return
                
                first_image_path = upload_file("Please enter the path of your first image: ", ".jpeg", image_destination)
                if not first_image_path:
                    return
                
                second_image_path = upload_file("Please enter the path of your last image: ", ".jpeg", image_destination)
                if not second_image_path:
                    return
                
                print("Please fill the other parts as well :)")

                
                title = input("Please enter your title: ")
                abstract = input("Please enter the abstract of your thesis: ")
                keywords_list = input("Please enter the keywords (seprate them with comma): ")
                
                student_thesis.title = title
                student_thesis.abstract = abstract
                student_thesis.keywords = keywords_list.split(",")
                student_thesis.pdf_path = pdf_path
                student_thesis.first_page_path = first_image_path
                student_thesis.last_page_path = second_image_path
                student_thesis.status = "defense_approval"
                
                save_theses(all_theses)
                
                print("Your request for defense submitted successfully :)")
                
            else:
                print("You have to wait 3 months after approval date in order to request for a defense!")
        else:
            print(f"You can not request a defense! the status of your request is: {student_thesis.status}")
    else:
        print("You don't have thesis to request defense for it!!!")
        
        
        
def change_password(user, all_users):
    
    while True:
        new_password = input("Please enter your new password: ")
        confirm_new_password = input("Please enter your new password again: ")
        
        if new_password == confirm_new_password:
            user.password = new_password
            save_users(all_users)
            break
        else:
            print("The passwords you entered are not the same :(   Try again...")
        
    print("The password changed successfully :)")
        
    
        

def search_theses(all_theses, all_users, all_courses):
    
    finished_theses = []
    for thesis in all_theses:
        if thesis.status == "finished":
            finished_theses.append(thesis)
            
    if not finished_theses:
        print("There is no finished thesis yet :(")
        return
    
    print("Please select your search filter:")
    print("1) By Title")
    print("2) By Author's Name")
    print("3) By Mentor's Name")
    print("4) By Keyword")
    print("5) By Year of Defense")
    print("6) By Examiner Name")
    
    choice = int(input("Please enter your choice: "))
    
    search_char = input("Please enter your search character: ").lower()
    
    results = []
    
    for thesis in finished_theses:
        
        if choice == 1:
            if search_char in thesis.title.lower():
                results.append(thesis)
                
        elif choice == 2:
            for user in all_users:
                if user.user_id == thesis.student_id and search_char in user.name.lower():
                    results.append(thesis)
                    break
                
        elif choice == 3:
            
            mentor_id = None
            for course in all_courses:
                if course.course_id == thesis.course_id:
                    mentor_id = course.professor_id
                    break
            
            if mentor_id:
                for user in all_users:
                    if user.user_id == mentor_id and search_char in user.name.lower():
                        results.append(thesis)
                        break
                    
        elif choice == 4:
            for keyword in thesis.keywords:
                if search_char in keyword.lower():
                    results.append(thesis)
                    break
        
        elif choice == 5:
            if search_char in thesis.defense_date:
                results.append(thesis)
                
        elif choice == 6:
            examiner_ids = thesis.examiners.values()
            
            for user in all_users:
                if user.user_id in examiner_ids:
                    if search_char in user.name.lower():
                        results.append(thesis)
                        break
                    
    if not results:
        print("No thesis found :(")
    else:
        print(f"I found {len(results)} results for you :)")
        for thesis in results:
            author_name = None
            for user in all_users:
                if user.user_id == thesis.student_id:
                    author_name = user.name
                    break
                
            course_info = None
            for course in all_courses:
                if course.course_id == thesis.course_id:
                    course_info = course
                    break
                
            mentor_name = None
            for user in all_users:
                if user.user_id == course_info.professor_id:
                    mentor_name = user.name
                    break
                
            examiners_names = []
            for examiner in thesis.examiners.values():
                examiner_name = None
                for user in all_users:
                    if user.user_id == examiner:
                        examiner_name = user.name
                        break
                examiners_names.append(examiner_name)


            print("-------------------------------")
            print(f"Title: {thesis.title}")
            print(f"Abstract: {thesis.abstract}")
            print(f"Keywords: {', '.join(thesis.keywords)}")
            print(f"Author: {author_name}")
            print(f"Year/Semester: {course_info.year}/{course_info.semester}")
            print(f"Examiners: {', '.join(examiners_names)}")
            print(f"Mentor: {mentor_name}")
            print(f"PDF File: {thesis.pdf_path}")
            print(f"Grade: {thesis.final_grade}")
            

    
            
            
def review_thesis_requests(professor, all_users, all_courses, all_theses):
    
    pending_approval_requests = []
    
    for thesis in all_theses:
        if thesis.status == "pending_approval":
            for course in all_courses:
                if course.course_id == thesis.course_id and course.professor_id == professor.user_id:
                    pending_approval_requests.append(thesis)
                    break
    
    if not pending_approval_requests:
        print("You don't have any pending request to approve :)")
        return
    
    print("List of pending requests to approve:")
    
    for i, thesis in enumerate(pending_approval_requests):
        
        course_title = None
        for course in all_courses:
            if course.course_id == thesis.course_id:
                course_title = course.title
                break
            
        print(f"{i+1}) Student ID: {thesis.student_id} |  Title: {course_title}")
     
    while True:
        try:
            choice = int(input("Please enter the number of request to review (enter 0 to exit): "))
            if choice == 0:
                return
            if 1 <= choice <= len(pending_approval_requests):
                selected = pending_approval_requests[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(pending_approval_requests)}")
        except ValueError:
            print("Please enter a valid choice!!")
            
    action = int(input("Please enter 1 to approve and 2 to reject: "))
    
    if action == 1:
        if professor.mentoring_capacity > 0:
            selected.status = "approved"
            selected.approval_date = datetime.now().isoformat()
            professor.mentoring_capacity -= 1
            
            for course in all_courses:
                if course.course_id == selected.course_id:
                    course.capacity -= 1
                    break
            
            save_theses(all_theses)
            save_users(all_users)
            save_courses(all_courses)
            
            print("The request successfully approved :)")
        else:
            print("Your mentoring capacity is full :(")
    
    elif action == 2:
        selected.status = "rejected"
        save_theses(all_theses)
        print("Request successfully rejected :)")
    else:
        print("Invalid Choice :(")
        

def manage_defense_requests(professor, all_users, all_courses, all_theses):
    
    defense_requests = []
    for thesis in all_theses:
        if thesis.status == "defense_approval":
            for course in all_courses:
                if course.course_id == thesis.course_id and course.professor_id == professor.user_id:
                    defense_requests.append(thesis)
                    break
                
    if not defense_requests:
        print("You don't have any request for defense to manage :)")
        return
        
    print("List of pending defense requests:")
    
    for i,thesis in enumerate(defense_requests):
        print(f"{i+1}) Student: {thesis.student_id}   |   Title: {thesis.title}")
        
    while True:
        try:
            choice = int(input("Please enter the thesis id to manage (enter 0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(defense_requests):
                valid_thesis_id = choice
                break
            else:
                print(f"Please enter a number between 1 and {len(defense_requests)}")
        except ValueError:
            print("Invalid choice! Try again...")
            
    selected = defense_requests[valid_thesis_id - 1]
    
    action = int(input("Enter 1 to approve and 2 to reject: "))
    
    if action == 1:
        defense_date = input("Please enter the defense date (example: 2025-08-16): ")
        
        internal_examiners = []
        for user in all_users:
            if user.role == "professor" and user.major == professor.major and user.user_id != professor.user_id and user.examination_capacity > 0:
                internal_examiners.append(user)
                
        external_examiners = []
        for user in all_users:
            if user.role == "professor" and user.major != professor.major and user.examination_capacity > 0:
                external_examiners.append(user)
                
        if not internal_examiners or not external_examiners:
            print("There is no internal or external examiner to choose :(   Try again later :)")
            return
                
        print("Selcet internal examiner:")
        
        for i, examiner in enumerate(internal_examiners):
            print(f"{i+1}) {examiner.name}  |  {examiner.major}")
            
        internal_examiner_choice = int(input("Please enter the id of internal examiner: "))
        internal_examiner_id = internal_examiners[internal_examiner_choice - 1]
         
            
        print("Selcet external examiner:")
         
        for i, examiner in enumerate(external_examiners):
            print(f"{i+1}) {examiner.name}  |  {examiner.major}")
            
        external_examiner_choice = int(input("Please enter the id of external examiner: "))
        external_examiner_id = external_examiners[external_examiner_choice - 1]
            
        
        selected.status = "defense_scheduled"
        selected.defense_date = defense_date
        selected.examiners = {
                "internal": internal_examiner_id.user_id,
                "external": external_examiner_id.user_id
            }          
        
        save_theses(all_theses)
        print("Defense has been scheduled successfully :)")
        
    elif action == 2:
        selected.status = "approved"
        selected.title = None
        selected.abstract = None
        selected.keywords = None
        selected.pdf_path = None
        selected.first_page_path = None
        selected.last_page_path = None
        
        save_theses(all_theses)
        print("Defense Rejected. You can tell the student to work more on his/her thesis :)")
    else:
        print("Invalid Choice :(")
        


def submit_score(professor, all_users, all_courses, all_theses):
    
    theses_to_grade = []
    for thesis in all_theses:
        if thesis.status == "defense_scheduled":
            defense_date = datetime.fromisoformat(thesis.defense_date).date()
            if datetime.now().date() >= defense_date:
                role_for_scoring = ""
                for course in all_courses:
                    if course.course_id == thesis.course_id and course.professor_id == professor.user_id:
                        role_for_scoring = "mentor"
                        break
                if not role_for_scoring:
                    for role, examiner_id in thesis.examiners.items():
                        if examiner_id == professor.user_id:
                            role_for_scoring = role
                            break
                        
                if role_for_scoring and role_for_scoring not in thesis.grades:
                    theses_to_grade.append(thesis)
                    
    if not theses_to_grade:
        print("There is no thesis to submit grade for :(")
        return
    
    print("Theses to submit grade for them:")
    for i, thesis in enumerate(theses_to_grade):
        print(f"{i+1}) Student ID: {thesis.student_id}  |  Title: {thesis.title}")
        
    while True:
        try:
            choice = int(input("Please enter a thesis to submit a grade for it (enter 0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(theses_to_grade):
                selected = theses_to_grade[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(theses_to_grade)}")
        except ValueError:
            print("Try Again...")
            
    while True:
        try:
            user_input = float(input("Please enter your grade (0-20): "))
            if 0 <= user_input <= 20:
                grade = user_input
                break
            else:
                print("The grade must be between 0-20!")
        except ValueError:
            print("Try Again...")
            
    role_for_scoring = ""
    for course in all_courses:
        if course.course_id == selected.course_id and course.professor_id == professor.user_id:
            role_for_scoring = "mentor"
            break
    if not role_for_scoring:
        for role, examiner_id in selected.examiners.items():
            if examiner_id == professor.user_id:
                role_for_scoring = role
                break
            
    selected.grades[role_for_scoring] = grade
    print("Your score submitted successfully :)")
    
    if len(selected.grades) == 3:
        print("All the grades for thesis has submitted. let's calculate the final grade :)))")
        
        average = sum(selected.grades.values()) / 3
        
        if 17 <= average <= 20:
            final_grade = "A"
        elif 13 <= average < 17:
            final_grade = "B"
        elif 10 <= average < 13:
            final_grade = "C"
        else:
            final_grade = "D"
            
        selected.final_grade = final_grade
        
        if average >= 10:
            selected.final_result = "defense_succeeded"
            selected.status = "finished"
        else:
            selected.final_result = "defense_again"
            selected.status = "approved"
            
        print(f"Final Score: {average} | Final Grade: {final_grade} | Result: {selected.final_result}")
        
        mentor_id = None
        for course in all_courses:
            if course.course_id == selected.course_id:
                mentor_id = course.professor_id
                break
            
        examiner_ids = selected.examiners.values()
        
        for user in all_users:
            if user.user_id == mentor_id:
                user.mentoring_capacity += 1
            if user.user_id in examiner_ids:
                user.examination_capacity += 1
                
        save_users(all_users)
        
    save_theses(all_theses)
                
        
            