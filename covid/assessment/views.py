from django.shortcuts import render
from . import ScoreCalculate
from .models import UserData
from datetime import date as dt

def user_info(request):
    context = {}
    
    return render(request, "takeuserinfo.html", context)

def assessment_page(request):

    return render(request, "assessment.html")

def result(request):

    data = {}
    symptom = {}
    add_symptom = {}
    
    data['name'] = request.POST.get('user_name')
    data['age'] = request.POST.get('age')
    data['sex'] = request.POST.get('sex')
    data['temp'] = request.POST.get('temp')

    symptom['breathing'] = request.POST.get('breathing')
    symptom['cough'] = request.POST.get('cough')
    symptom['soar'] = request.POST.get('soar')
    symptom['weakness'] = request.POST.get('weakness')
    symptom['nose'] = request.POST.get('nose')
    
    add_symptom['abdominal'] = request.POST.get('abdominal')
    add_symptom['vomit'] = request.POST.get('vomit')
    add_symptom['diarrhoea'] = request.POST.get('diarrhoea')
    add_symptom['chest_pain'] = request.POST.get('chest_pain')
    add_symptom['muscle'] = request.POST.get('muscle')
    add_symptom['loss_taste'] = request.POST.get('loss_taste')
    add_symptom['rash'] = request.POST.get('rash')
    add_symptom['loss_speech'] = request.POST.get('loss_speech')

    obj = ScoreCalculate.ScoreCalculate(data, symptom, add_symptom)
    score = obj.calculate()

    if score == "TemperatureError":
        return render(request, "assessment.html")

    final_score = {'score' : score}
    score_result = ""

    if(score < 5):
        score_result = "Negative"
    else:
        score_result = "Positive"

    inser_data = UserData(  name=data['name'],
                            age= str(data['age']),
                            sex= data['sex'],
                            temp=data['temp'],
                            date=str(dt.today()),
                            score=score,
                            result=score_result)
    
    inser_data.save()


    return render(request, "result.html", final_score)


def participants(request):

    all_participant_list = UserData.objects.all()
    
    datalists = {}
    datalists['participant_list'] =  all_participant_list
    

    return render(request, "participants.html", datalists)