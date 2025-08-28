from src.functions import load_users, load_courses, load_theses
from src.services import request_thesis, view_thesis_status, request_defense, change_password, search_theses, review_thesis_requests, manage_defense_requests, submit_score


all_users = load_users()
all_courses = load_courses()
all_theses = load_theses()

def login(user_id, password, all_users):
    for user in all_users:
        if user.user_id == user_id and user.password == password:
            return user
    return None

def student_menu(student, all_courses, all_theses, all_users):
    print("welcome to the student panel")

    while True:
        print("Choose your option:")
        print("1) Request for a thesis course")
        print("2) View thesis status")
        print("3) Submit a request for defense")
        print("4) Search among theses")
        print("5) Change password")
        print("6) Exit")

        while True:
            try:
                user_input = int(input("Please enter your choice: "))
                if 1 <= user_input <= 6:
                    choice = user_input
                    break
                else:
                    print("Please enter a number between 1 and 6 !")
            except ValueError:
                print("Please enter a valid number!!!")

        if choice == 1:
            request_thesis(student, all_courses, all_theses, all_users)
        elif choice == 2:
            view_thesis_status(student, all_theses)
        elif choice == 3:
            request_defense(student, all_theses)
        elif choice == 4:
            search_theses(all_theses, all_users, all_courses)
        elif choice == 5:
            change_password(student, all_users)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Please enter a valid choice!")

def professor_menu(professor, all_courses, all_theses, all_users):
    print("Welcome to professor menu")

    while True:
        print("Please choose an option")
        print("1) View Thesis Applications")
        print("2) Managing Defense Requests")
        print("3) Submit Score")
        print("4) Search among theses")
        print("5) Change password")
        print("6) Exit")

        while True:
            try:
                user_input = int(input("Please enter your choice: "))
                if 1 <= user_input <= 6:
                    choice = user_input
                    break
                else:
                    print("Please enter a number between 1 and 6 !")
            except ValueError:
                print("Please enter a valid number!!!")

        if choice == 1:
            review_thesis_requests(professor, all_users, all_courses, all_theses)
        elif choice == 2:
            manage_defense_requests(professor, all_users, all_courses, all_theses)
        elif choice == 3:
            submit_score(professor, all_users, all_courses, all_theses)
        elif choice == 4:
            search_theses(all_theses, all_users, all_courses)
        elif choice == 5:
            change_password(professor, all_users)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Please enter a valid choice!")
        
def main():

    print("Welcome")

    while True:
        user_id = input("Please enter your user id: ")
        password = input("Please enter your password: ")

        user = login(user_id, password, all_users)

        if user:
            if user.role == "student":
                student_menu(user, all_courses, all_theses, all_users)
            elif user.role == "professor":
                professor_menu(user, all_courses, all_theses, all_users)
            break
        else:
            print("Try again...")



if __name__ == "__main__":
    main()