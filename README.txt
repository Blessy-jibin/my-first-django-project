Python>=3

1. Create virtualenv with python3

   virtualenv -p python3 envname
   source envname/bin/activate


2. Install Django

    pip install django

3. Runserver

    cd vgym
    python manage.py runserver


API END Points

1. plan list > http://127.0.0.1:8000/plan (HTTP GET Method)
2. create plan > http://127.0.0.1:8000/plan (HTTP POST Method)
    eg. data = {'title':'', users:[id, id, id]}
3. update plan > http://127.0.0.1:8000/plan/id/ (HTTP PUT Method)
   eg. data = {'title':'', users:[id, id, id]}
4. delete plan > http://127.0.0.1:8000/plan/id/ (HTTP DELETE Method)



1. user list > http://127.0.0.1:8000/user (HTTP GET Method)
2. create user > http://127.0.0.1:8000/user (HTTP POST Method)
    eg. data = {'email':'', 'first_name': '','last_name': '', 'password': '', 'plans': [id, id ..]}
3. update user > http://127.0.0.1:8000/user/id/ (HTTP PUT Method)
   eg. data = {'email':'', 'first_name': '','last_name': '', 'password': '', 'plans': [id, id ..]}
4. delete user > http://127.0.0.1:8000/user/id/ (HTTP DELETE Method)


1. day list > http://127.0.0.1:8000/day (HTTP GET Method)
2. create day > http://127.0.0.1:8000/day (HTTP POST Method)
    eg. data = {'day_number':'', plans:[id, id, id]}
3. update day > http://127.0.0.1:8000/day/id/ (HTTP PUT Method)
   eg. data = {'day_number':'', plans:[id, id, id]}
4. delete day > http://127.0.0.1:8000/day/id/ (HTTP DELETE Method)


1. exrcise list > http://127.0.0.1:8000/exrcise (HTTP GET Method)
2. create exrcise > http://127.0.0.1:8000/exrcise (HTTP POST Method)
    eg. data = {'title':'', days:[id, id, id]}
3. update exrcise > http://127.0.0.1:8000/exrcise/id/ (HTTP PUT Method)
   eg. data = {'title':'', days:[id, id, id]}
4. delete exrcise > http://127.0.0.1:8000/exrcise/id/ (HTTP DELETE Method)



