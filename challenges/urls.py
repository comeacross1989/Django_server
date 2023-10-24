from django.urls import path
from . import views


urlpatterns =[    
    path('',views.index, name= 'index'),
    path('<int:month>',views.monthly_chanllenge_by_Number),
    path('<str:month>',views.monthly_chanllenge, name='str_month_chall'),
]