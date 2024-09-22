import csv
import os
from question import Question
from question_master import QuestionMaster
from datetime import datetime

"""Using global variables so that it can be reused in different methods"""
student_name=None
university=None
score=0
total_questions=0

class ExamClient:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.questions = []
        

    def load_questions(self):
        """Loads questions from the CSV file."""
        try:
            with open(self.csv_file, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
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
            print("File does not exists")
            


    def register_user(self): #for registering the student taking exam
        global student_name, university
        student_name = input("Enter you name: ")
        print("\n")
        university = input("Enter your university: ")
        print("\n")
        now=datetime.now()
        date=now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Name: {student_name} \nUniversity: {university} \nToday's Date: {date} \n")
        print("Select choice 2 to start the exam")


    def start_exam(self): #starting the exam
        global student_name, university,score,total_questions
        print(f"Exam started for {student_name} from {university} University")
        try:
            questions = QuestionMaster.display_all_questions(self) #gets all the questions from the server
            total_questions=len(questions)
        except:
            print("Error in displaying the questions. 505!")
        if len(questions)==0:
            print("Test is not online yet.")
        else:
            for question in questions:
                print(f"\n{question['num']}) {question['question']}")
                print(f"  op1) {question['option1']}")
                print(f"  op2) {question['option2']}")
                print(f"  op3) {question['option3']}")
                print(f"  op4) {question['option4']}")
                answer = input("Enter your choice (op1/op2/op3/op4): ")
                if answer == question['correctoption']:
                    score += 1 #increments score by 1 if answer is correct
            print("")
            print("You have answered all the questions.")
            print("")
            print("Select Choice 3 to submit the exam.")

            


    def save_student_details(self, student_name, university_name, score, total_questions):
        """Saves student details to a separate CSV file."""
        
        student_csv_file = 'student_results.csv'
        is_new_file = not os.path.exists(student_csv_file)

        # Format the date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Open the student CSV file in append mode
        with open(student_csv_file, 'a', newline='') as file:
            fieldnames = ['Student Name', 'University Name', 'Score', 'Total Questions', 'Date Time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # If it's a new file, write the header
            if is_new_file:
                writer.writeheader()

            # Write the student details
            writer.writerow({
                'Student Name': student_name,
                'University Name': university_name,
                'Score': score,
                'Total Questions': total_questions,
                'Date Time': current_time
            })



    def submit_exam(self):
        self.save_student_details(student_name, university, score, total_questions)
        print(f"Name: {student_name} \nUniversity: {university}")
        print(f"Marks Scored : {score} correct out of {total_questions} questions")
        print("Your Exam has been submitted successfully, Thank you.\n")
        


def main():
    exam_client = ExamClient('questions.csv')
    while True:
        print("\n")
        print("1) Register Yourself")
        print("2) Start Exam")
        print("3) Submit Exam")
        print("4) Exit")
        choice = input("Enter your choice:")
        print("\n")
        if choice == '1':
            exam_client.register_user()
        elif choice == '2':
            exam_client.start_exam()
        elif choice == '3':
            exam_client.submit_exam()
            break
        elif choice=='4':
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()
