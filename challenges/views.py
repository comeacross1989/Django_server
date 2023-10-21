from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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
    "December": "Write Medium Post every other day!",    
}

def index(request):
    list_items = ''
    months = list(monthly_chanllenges.keys())
    
    for month in months:
        capialized_month = month.capitalize()
        list_items += f"<li><a href ='{month}'>{capialized_month}</li>"
    response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)

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
        response_data = f'<h1>{challenge_text}</h1>'
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')    
    return HttpResponse(response_data)