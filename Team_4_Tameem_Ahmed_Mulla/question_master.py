import csv
import os
import logging
from question import Question
from student import Student

logger=logging.getLogger(__name__)

class QuestionMaster:
    def __init__(self):
        self.questions = []

    def save_questions(self):

        """Saves all questions 
        (existing and new) 
        to the CSV file."""

        with open('questions.csv', 'w', newline='') as file:
            fieldnames = ['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for question in self.questions:
                writer.writerow(question.to_dict())


    def load_questions(self):
        """Loads existing questions from the CSV file if it exists."""
        self.questions = []
        try:
            if os.path.exists('questions.csv'):  # Checking if the CSV file exists
                with open('questions.csv', 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        question = Question(
                            int(row['num']),
                            row['question'],
                            row['option1'],
                            row['option2'],
                            row['option3'],
                            row['option4'],
                            row['correctoption']
                        )
                        self.questions.append(question)
        except IOError:
            print("File does not Exists.")
        
    def load_students(self):
        self.students = []
        if os.path.exists('student_results.csv'):  # Checking if the CSV file exists
            try:
                with open('student_results.csv', 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if 'Student Name' in row and 'University Name' in row and 'Score' in row and 'Total Questions' in row and 'Date Time' in row:
                            student = Student(
                                student_name=row['Student Name'],
                                university=row['University Name'],
                                score=row['Score'],
                                total_questions=row['Total Questions'],
                                date=row['Date Time']
                            )
                            self.students.append(student)
                        else:
                            print("CSV file is missing required columns.")
            except IOError:
                print("File does not exist.")

 
    def add_question(self, question, option1, option2, option3, option4, correctoption):
        """Adds a new question to the list and then saves all questions."""
        # Load existing questions first (to avoid overwriting)
        self.load_questions()
        
        # Get the next question number
        num = max([q.num for q in self.questions], default=0) + 1
        
        new_question = Question(num, question, option1, option2, option3, option4, correctoption)

        logger.info(f"New Question : {new_question}")
        
        # Add the new question to the list
        try:
            self.questions.append(new_question)
        except TypeError:
            return "Trying adding the question again!"

        # Save all questions (old and new) to the CSV file
        self.save_questions()
        logger.info("Added the questions successfully.")


    def display_all_questions(self):
        """Displays all questions."""

        try:
            self.load_questions() # Ensure we load any existing questions
        except IOError:
            return "Error while reading the questions!" 
        try:
            return [q.to_dict() for q in self.questions]
        except AttributeError:
            print("Server Error!")
    
    #Get question by question number
    def search_question_by_num(self, num):

        for question in self.questions:
            if question.num == num:
                return question
            
        return None

    
    #delete question by number
    def delete_question_by_num(self, num):
        self.questions = [q for q in self.questions if q.num != num]
        logger.info(f"Questions List: {self.questions} ")
        self.save_questions()


    #delete all the questions
    def delete_all(self):
        self.questions = []
        self.save_questions()
        
    #update the question
    def update_question(self, num, question, option1, option2, option3, option4, correctoption):

        q = self.search_question_by_num(num)
        logger.info(q)
        if q:
            q.question = question
            q.option1 = option1
            q.option2 = option2
            q.option3 = option3
            q.option4 = option4
            q.correctoption = correctoption
            self.save_questions()
    
    def display_all_students(self):
        """Displays all students."""

        try:
            self.load_students() # Ensure we load any existing students
        except IOError:
            return "Error while reading the questions!" 
        try: # for solving the error "object has no attributes" error
            return [student.to_dict() for student in self.students]
        except AttributeError:
            print("Server Error, 505!")

    

def main():
    question_master = QuestionMaster()
    while True:
        print("\n")
        print("1) Add a question")

        print("2) Search for a Question based on quest num")

        print("3) Delete question based on question num")

        print("4) Delete all the questions")

        print("5) Modify the question based on question num")

        print("6) Display all the questions")

        print("7) Display all the Students who have taken the exam")

        print("8) Exit menu")
        print("\n")
        choice = input("Enter your choice: ")


        if choice == '1':
            try:
                print("\n")
                question = input("Enter the question: ")
                option1 = input("Enter option 1: ")
                option2 = input("Enter option 2: ")
                option3 = input("Enter option 3: ")
                option4 = input("Enter option 4: ")
                correctoption = input("Enter the correct option: ")
                question_master.add_question(question, option1, option2, option3, option4, correctoption)
                question_master.save_questions()

                print("\n Question is added Successfully.")
            except:
                print("Question was not added.")


        elif choice == '2':
            print("\n")
            num = int(input("Enter the question number: "))
            q = question_master.search_question_by_num(num)
            if q:
                print(q.to_dict())
            else:
                print("Question not found.")


        elif choice == '3':
            print("\n")
            num = int(input("Enter the question number: "))
            q = question_master.search_question_by_num(num)
            if q:
                question_master.delete_question_by_num(num)
                print("Question deleted successfully.")
            else:
                print("Question not found.")

        elif choice == '4':
            print("\n")
            question_master.delete_all()
            print("Questions are deleted")
            
        elif choice == '5':
            print("\n")
            num = int(input("Enter the question number: "))
            q = question_master.search_question_by_num(num)
            if q:
                question = input("Enter the question: ")
                option1 = input("Enter option 1: ")
                option2 = input("Enter option 2: ")
                option3 = input("Enter option 3: ")
                option4 = input("Enter option 4: ")
                correctoption = input("Enter the correct option: ")
                question_master.update_question(num, question, option1, option2, option3, option4, correctoption)
            else:
                print("Question not found!")

            
        elif choice== '6':
            questions = question_master.display_all_questions()
            if questions:
                for question in questions:
                    print("\n")
                    print(question)
            else:
                print("No questions found!")

        elif choice== '7':
            students = question_master.display_all_students()
            logger.info(f"students : {students}")
            if students:
                for student in students:
                    print("")
                    print(student)
            else:
                print("No students found.")

        elif choice == '8':
            break


if __name__ == "__main__":
    main()

