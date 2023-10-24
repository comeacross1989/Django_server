from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
monthly_chanllenges={
    "Janury":"Apply for Jobs everyday!",
    "February": "Write Medium Post every other day!",
    "March":"Apply for Jobs everyday!",
    "April": "Write Medium Post every other day!",
    "May":"Apply for Jobs everyday!",
    "June": "Write Medium Post every other day!",
    "July":"Apply for Jobs everyday!",
    "August": "Write Medium Post every other day!",
    "September":"Apply for Jobs everyday!",
    "October": "Write Medium Post every other day!",
    "November":"Apply for Jobs everyday!",
    "December": None,    
}

def index(request):
    
    months = list(monthly_chanllenges.keys())     
    return render(request, 'challenges/index.html',{
        "months": months
    })

def monthly_chanllenge_by_Number(request, month):    
    months = list(monthly_chanllenges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
    redirect_month = months[month-1]    
    redirect_path = reverse('str_month_chall',args=[redirect_month])# /challengs/'redirect_month'
    return HttpResponseRedirect(redirect_path)


def monthly_chanllenge(request, month):
    try:
        challenge_text = monthly_chanllenges[month]
        return render(request, "challenges/challenge.html",{
            "month":month,
            "text":challenge_text
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')    
    