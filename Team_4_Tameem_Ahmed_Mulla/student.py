class Student:
    def __init__(self, student_name, university, score, total_questions, date):
        self.student_name = student_name
        self.university = university
        self.score = score
        self.total_questions = total_questions
        self.date = date

    def to_dict(self):
        return {
            'student_name': self.student_name,
            'university': self.university,
            'score': self.score,
            'total_questions': self.total_questions,
            'date': self.date
        }