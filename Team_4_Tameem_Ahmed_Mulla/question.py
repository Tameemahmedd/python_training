class Question:
    def __init__(self, num, question='', option1='', option2='', option3='', option4='', correctoption=''):
        self.num = num
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctoption = correctoption

    def to_dict(self):
        return {
            'num': self.num,
            'question': self.question,
            'option1': self.option1,
            'option2': self.option2,
            'option3': self.option3,
            'option4': self.option4,
            'correctoption': self.correctoption
        }