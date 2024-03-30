# Write your solution after the class ExamSubmission
# Do not make changes to the class!
class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):
    passed_list = []
    for exam in submissions:
        if exam.points >= lowest_passing:
            passed_list.append(exam)
    return passed_list