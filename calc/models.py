from django.db import models

import requests
import random
courses_list=[{
    'id':1,
    'course':'Quiz1'
},
{
    'id':2,
    'course':'Quiz2'
},
{
    'id':3,
    'course':'Quiz3'
} 
]

json_question = requests.get('https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=multiple')
all_questions = json_question.json()['results']



class datas():
    def __init__(self,question,correct_answer,wrong_answers):
        self.question=question
        self.answer=correct_answer
        wrong_answers.append(correct_answer)
        random.shuffle(wrong_answers)
        self.option1=wrong_answers[0]
        self.option2=wrong_answers[1]
        self.option3=wrong_answers[2]
        self.option4=wrong_answers[3]
        
Quiz=[]
for questions in all_questions:
    ques=questions['question']
    ans=questions['correct_answer']
    options=questions['incorrect_answers']
    set_of_questions=datas(ques,ans,options)
    Quiz.append(set_of_questions)
    