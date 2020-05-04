from django.shortcuts import render
from .forms import Question_form

# Create your views here.

def home(request):
    return render(request,'guess/home.html')

def start(request):
    
    filled_form=Question_form(request.POST)
    new_form=Question_form()
    note="Do you like playing badminton?"
    result=""
   
    
    if filled_form.is_valid() :
        
        result=filled_form.cleaned_data['answer']
        if result == "Yes":
            note="Are you from CSE?"
            filled_form=Question_form(request.POST)
            new_form=Question_form()
            result=filled_form.cleaned_data['answer']
            if result == "Yes":
                note = "Are you one of the three keyholders of 401?"
                filled_form=Question_form(request.POST)
                new_form=Question_form()
                result=filled_form.cleaned_data['answer']
                if result == "Yes":
                    note="Aryan"
                else:
                    note="Amritansh"

            else:
                note = "Sourabh"
            
        else:
            note="Do you like playing Chess?"
            
            new_form=Question_form()
            return render(request,'guess/start.html',{'question_form':new_form,'note':note})
            filled_form=Question_form(request.POST)
            result=filled_form.cleaned_data['answer']
            if result == 'No':
                note="Anurag"
            else:
                note="Tanay"

       
        new_form=Question_form()
    return render(request,'guess/start.html',{'question_form':new_form,'note':note})


