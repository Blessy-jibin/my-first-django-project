import json
from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404

from django.views.generic import View
from .models import Plan, Day, Exercise,UserData
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate
from django.http import QueryDict
# class PlanView(View):

#     def get(self, request):
#         plans = Plan.objects.all()
#         data = []

#         for obj in plans:
#             dic = {}
#             #day_lis = list(obj.day.values())
#             day_lis = list(obj.day)
#             #user_lis = list(obj.user.values('username', 'first_name', 'last_name'))
#             dic['name'] = obj.title
#             dic['day'] = day_lis
#             data.append(dic)
#         return HttpResponse(json.dumps(data))

  

class PlanView(View):

    def get(self, request,pk):
        user = UserData.objects.get(pk = pk)
        plans = user.plan.all()
        plan_lis = []
        for plan in plans:
            days = plan.day.all()
            day_lis = []
            for day in days:
                exercises = day.exercise.all()
                exercise_lis = []
                for exercise in exercises:
                    exercise_lis.append(exercise.title) 
                day_dic = {}
                day_dic['day_number']= day.day_number
                day_dic['exercises'] = exercise_lis
                day_lis.append(day_dic)
            plan_dic = {}
            plan_dic['planid'] = plan.id
            plan_dic['title'] = plan.title
            plan_dic['days'] = day_lis
            plan_lis.append(plan_dic)        

        return HttpResponse(json.dumps(plan_lis))

    def post(self, request,pk):
        user = UserData.objects.get(pk=pk)
        plan = request.POST.get('plan');
        print(plan);
        plans=json.loads(plan)
        title=plans['title'];
        days=plans['day'];
        plan_obj=Plan.objects.create(title=title)
        for day in days:
            day_number = day['day_number']
            day_obj = Day.objects.get(day_number=day_number)
            exercises = day['exercises']
            for exercise in exercises:
                title=exercise
                exercise_obj = Exercise.objects.get(title=exercise)
                day_obj.exercise.add(exercise_obj)
            plan_obj.day.add(day_obj)
        user.plan.add(plan_obj);
        user.save();
        send_update_email(user.user.email,"You have created a plan")

        return HttpResponse(json.dumps({'status': 201, 'message': 'OK'}))

    def put(self, request,pk,planid):
        user = UserData.objects.get(pk=pk)
        put_params = QueryDict(request.body)
        plans_json = put_params.get('plan')
        plans=json.loads(plans_json)
        title=plans['title']
        days=plans['day']
        print(title,days)
        plan_obj=Plan.objects.create(title=title)
        for day in days:
            day_number = day['day_number']
            day_obj = Day.objects.get(day_number=day_number)
            exercises = day['exercises']
            for exercise in exercises:
                title=exercise
                exercise_obj = Exercise.objects.get(title=exercise)
                day_obj.exercise.add(exercise_obj)
            plan_obj.day.add(day_obj)
        user.plan.add(plan_obj);
        user.save();
        plan = Plan.objects.get(id=planid)
        plan.delete()
        send_update_email(user.user.email,"Updated your plan")
        return HttpResponse(json.dumps({'status': 201, 'message': 'OK'}))

    def delete(self,request,pk,planid):
        try:
            user = UserData.objects.get(pk=pk)
            plan = Plan.objects.get(id=planid)
            plan.delete()
            send_update_email(user.user.email,"You have deleted a plan")
            return HttpResponse(json.dumps({'status': 201, 'message': 'OK'}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': 201, 'message': e}))
        return HttpResponse(0);


class UserView(View):
     
    def get(self, request):
        user = list(User.objects.values('first_name', 'last_name','email','pk'))
        return HttpResponse(json.dumps(user))


    def post(self, request):
        print(request)
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        username = request.POST.get('email')
       
        if email and first_name and last_name and password:
            try:
                dictToSave = {
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'password':password,
                    'username':email
                 }

                new_user=User.objects.create_user(**dictToSave)               
                new_userdata=UserData.objects.create(user=new_user)
                send_update_email(email,"Thanks for sigining up");
                return HttpResponse(json.dumps({'status': 200, 'message': 'success','uid':new_userdata.id}))
            except Exception as e:
                return HttpResponse(json.dumps({'status': 500, 'message': e}))
        return HttpResponse(json.dumps({'status': 500, 'message': 'params is missing'}))

class UpdatePlanUserView(View):


    def post(self, request,pk):
        user=UserData.objects.get(pk=pk)
        plan_lis = request.POST.getlist('plan[]');
        if plan_lis:
            try:
                user_data=UserData.objects.get(pk=pk)
                for plan in plan_lis:
                    eachplan=Plan.objects.get(title=plan)
                    user_data.plan.add(eachplan)
                    user_data.save()
                    
            except Exception as e:
                
                return HttpResponse(json.dumps({'status': 500, 'message': e}))
            return HttpResponse(json.dumps({'status': 200, 'message': 'OK'}))
        return HttpResponse(json.dumps({'status': 500, 'message': 'params is missing'}))      

    def delete(self, request, pk):
        try:
            userdata=UserData.objects.get(pk=pk)
            data=request.body.decode("utf-8")
            return HttpResponse(json.dumps({'status': 201, 'message': 'OK'}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': 201, 'message': e}))
class DaysView(View):

    def get(self, request):
        #each_exercise = Exercise.objects.get(id=pk)
        days = Day.objects.all()
        day_lis=[]
        for day in days:
            day_lis.append(day.day_number)
        return HttpResponse(json.dumps(day_lis))

class ExercisesView(View):

    def get(self, request):
        #each_exercise = Exercise.objects.get(id=pk)
        exercises = Exercise.objects.all()
        exercise_lis = []
        for exercise in exercises:
            exercise_lis.append(exercise.title)
        return HttpResponse(json.dumps(exercise_lis))


class AuthenticateView(View):

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=User.objects.get(email=email)

        u_id=user.pk
        user_id=UserData.objects.get(user=user).pk
        print(user_id)
       
        if user.check_password(password):
            return HttpResponse(json.dumps({'value':1,'user_id':user_id}))
        else:
            return HttpResponse(json.dumps({'value':0}))
        
        
def send_update_email(to_email,msg):
    from_email = "blessy.xavier31@gmail.com"
    if msg is None :
        msg = "Thanks for using Virtu gym" 
    try:
        send_mail(
            'GYM Notification',
            msg,
            from_email,
            ['to_email'],
            fail_silently=True,
        )
    except Exception as e:
        print(e)

def signup(request):
    #boards = Board.objects.all()
    return render(request, 'signup.html')
def signin(request):
    #boards = Board.objects.all()
    return render(request, 'signin.html')
def home(request,pk):
    userdata = UserData.objects.get(pk=pk)
    userdata.plan.all()
    print(userdata.plan.all())
    user_plan=userdata.plan.all()
    plans=Plan.objects.all()
    print(pk)
    return render(request, 'home.html', {'userdata':userdata,'user_plan':user_plan,'plans':plans,'pk':pk})

