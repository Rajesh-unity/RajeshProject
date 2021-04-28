from django.shortcuts import render
from django.http import JsonResponse
from .models import courses_list
from .models import Quiz
import requests
# Create your views here.
def api_ques(request,id):
    ques=[]
    k=1
    for i in Quiz:
        a={}
        a["id"]=k
        a['question']=i.question
        a["correct_answer"]=i.answer
        c={}
        c[0]=i.option1
        c[1]=i.option2
        c[2]=i.option3
        c[3]=i.option4
        a['options']=c
        ques.append(a)
        k+=1
    return JsonResponse(ques,safe=False)
lst=[]
def take_test(request,id):
    return render(request,"home.html",{"id":id})
def index(request):
    context={"courses":courses_list}
    return render(request,"base.html",{"question":context})

