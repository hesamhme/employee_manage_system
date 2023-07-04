from django.urls import path
from .views import EmpListView, NewEmp, DelEmp, EditEmp, PenaltyEmployee, RewardEmployee

urlpatterns = [
    path('',EmpListView.as_view(), name='home'),
    path('new/', NewEmp.as_view(), name='new'),
    path('<int:pk>/delete/', DelEmp.as_view(), name='del'),
    path('<int:pk>/edit/', EditEmp.as_view(), name='edit'),
    # path('<int:pk>/dislike/', dislike_employee, name='dislike'),
    path('penalty/<int:pk>/', PenaltyEmployee.as_view(), name='penalty'),
    path('reward/<int:pk>/', RewardEmployee.as_view(), name='reward'),
]





                                       