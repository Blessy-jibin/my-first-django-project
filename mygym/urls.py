from .views import (PlanView,
                     UserView,PlanView,signup,home,ExercisesView,
                    DaysView,AuthenticateView)
from django.urls import path

from mygym import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('plan', PlanView.as_view(), name='plan_details'),
    # url(r'^home/(?P<uid>\d+)/$',views.home,name=home),
    path('signin',views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('home/<int:pk>',views.home,name='home'),
    path('home',views.signin,name='signin'),
    path('',views.signin,name='signin'),

    path('user/', UserView.as_view(), name='show-user-section'),
    path('user/<int:pk>/plan/', PlanView.as_view(), name='show-plan'),
    path('user/<int:pk>/plan/<int:planid>',PlanView.as_view(), name='show-plan'),
    path('exercises', ExercisesView.as_view(),name='get-exercises'),
    path('days', DaysView.as_view(), name='get-days'),
    path('authenticate',AuthenticateView.as_view(), name='authenticate'),


]


