'''Project 1:This project produces reusable byline for a buisness'''

""" Import dpendencies from the Python Library"""
import statistics
import math

def main():
    #define variables
    company_name: str = 'ACT NOW: ACT Preperation Services'
    company_description: str = 'Guaranteed to get you a perfect 36 or your money back!'
    number_of_students: int = 9
    student_scores_before: list = [18, 19, 20, 21, 22, 23, 24, 25, 26]
    student_scores_after: list = [36, 36, 36, 36, 36, 36, 36, 36, 36]
    are_students_always_satisfied: bool = True
    cost_per_student: float = 1499.99
    score_change=list(map(lambda a, b: a-b, student_scores_after, student_scores_before))
    
   #Multiline string company overview using f-string
    company_summary_byline: str = f"""
    Number of student: {number_of_students}
    Student Before Class Scores: {student_scores_before}
    Student After Class Scores: {student_scores_after}
    Are Students Satisfied?: {are_students_always_satisfied}
    Cost per Student: {cost_per_student}
    Score Change: {score_change}
    """
    #Descriptive Statistics for byline written using Multiline string format
    stats_summary: str = f"""
    Smallest Score Increase: {min(score_change)}
    Largest Score Increase: {max(score_change)}
    Average Score Before Class: {statistics.mean(student_scores_before)}
    Average Score After Class: {statistics.mean(student_scores_after)}
    Standard Deviation After Class: {statistics.stdev(student_scores_after)}
    """
    
    byline: str = f"""
    {company_summary_byline}
    {stats_summary}
    """
    print(byline)
    
    if __name__=='__main__':
        main()
