from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from OCS.models import Question
from OCS.models import User
import random


def newQuestion(request):
    try:
        if request.session['username']=='Admin':
            pass
        else:
            return HttpResponseRedirect('http://localhost:8000/OCS/login') 
    except:
        return HttpResponseRedirect('http://localhost:8000/OCS/login')
    res=render(request,'OCS/new_question.html')
    return res
def saveQuestion(request):
    question=Question()
    question.que=request.POST['question']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OCS/view-question')

def viewQuestion(request):
    try:
        if request.session['username']=='Admin':
            pass
        else:
            return HttpResponseRedirect('http://localhost:8000/OCS/login') 
    except:
        return HttpResponseRedirect('http://localhost:8000/OCS/login')
    questions=Question.objects.all()
    res=render(request,'OCS/view_question.html',{'questions':questions})
    return res

def editQuestion(request):
    try:
        if request.session['username']=='Admin':
            pass
        else:
            return HttpResponseRedirect('http://localhost:8000/OCS/login') 
    except:
        return HttpResponseRedirect('http://localhost:8000/OCS/login')
    q=request.GET['qno']
    question=Question.objects.get(qno=int(q))
    res=render(request,'OCS/edit_question.html',{'question':question})
    return res

def editSaveQuestion(request):
    questions=Question()
    questions.qno=request.POST['qno']
    questions.que=request.POST['question']
    questions.optiona=request.POST['optiona']
    questions.optionb=request.POST['optionb']
    questions.optionc=request.POST['optionc']
    questions.optiond=request.POST['optiond']
    questions.answer=request.POST['answer']
    questions.save()
    return  HttpResponseRedirect('http://localhost:8000/OCS/view-question')

def deleteQuestion(request):
    try:
        if request.session['username']=='Admin':
            pass
        else:
            return HttpResponseRedirect('http://localhost:8000/OCS/login') 
    except:
        return HttpResponseRedirect('http://localhost:8000/OCS/login')
    q=request.GET['qno']
    question=Question.objects.filter(qno=int(q))
    question.delete()
    return HttpResponseRedirect('http://localhost:8000/OCS/view-question')

def signup(request):
    d={}
    try:
        if request.GET['error']==str(1):
            d['errmsg']='User name already taken'
    except:
            d['errmsg']=''
    res=render(request,'OCS/signup.html',d)
    return res

def saveUser(request):
    user=User()
    u=User.objects.filter(username=request.POST['username'])
    if not u:
        user.username=request.POST['username']
        user.password=request.POST['password']
        user.fullname=request.POST['fullname']
        user.save()
        url='http://localhost:8000/OCS/login/'
    else :
        url='http://localhost:8000/OCS/singup/?error=1'
    return HttpResponseRedirect(url)
    
def creatAdmin():
    user=User()
    user.username="admin"
    user.password="password"
    user.fullname="SuperUser"
    user.save()

def login(request):
    user=User.objects.filter(username='admin')
    if not user:
        creatAdmin()
    res=render(request,'OCS/login.html')
    return res

def loginValidation(request):
    try:
        user=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        user.username
        request.session['username']=user.username
        request.session['fullname']=user.fullname
        url='http://localhost:8000/OCS/home/'
    except:
        url='http://localhost:8000/OCS/login/'
    return HttpResponseRedirect(url)

def home(request):
    try:
        fullname=request.session['fullname']
    except: 
        HttpResponseRedirect('http://localhost:8000/OCS/longin')
    res=render(request,'OCS/home.html')
    return res

def startTest(request):
    try:
        if request.session['username']=='Admin':
            return HttpResponseRedirect('http://localhost:8000/OCS/home') 
        else:
            pass 
    except:
        return HttpResponseRedirect('http://localhost:8000/OCS/login')
    no_of_question=5
    all_question=list(Question.objects.all())
    random.shuffle(all_question)
    question_list=all_question[:no_of_question]
    res=render(request,'OCS/start_test.html',{'questions':question_list})
    return res

def testResult(request):
    try:
        if request.session['username']=='Admin':
            return HttpResponseRedirect('http://localhost:8000/OCS/home') 
        else:
            pass 
    except:
        return HttpResponseRedirect('http://localhost:8000/OCS/login')
    total_attempt=0
    tot_r=0
    tot_w=0
    qno_list=[]
    for k in request.POST:
        if k.startswith('qno'):
            qno_list.append(int(request.POST[k]))
    for n in qno_list:
        question=Question.objects.get(qno=n)
        try:
            if question.answer==request.POST['q'+str(n)]:
                tot_r+=1
            else:
                tot_w-=1
            total_attempt+=1
        except:
            pass
    d={
            'total_attempt':total_attempt,
            'tot_r':tot_r,
            'tot_w':tot_w
    }
    res=render(request,'OCS/test_result.html',d)
    return res

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('http://localhost:8000/OCS/login/')