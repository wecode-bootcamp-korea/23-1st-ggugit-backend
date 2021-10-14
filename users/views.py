import json, re, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings  import SECRET_KEY

class SignupView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

            #이메일 양식
            if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$', data['email']):
                return JsonResponse({'message':'NOT_EMAIL_FORMAT'}, status = 400)
            #패스워드 양식
            if not re.search(r'^(?=(.*[A-Za-z]))(?=(.*[0-9]))(?=(.*[@#$%^!&+=.\-_*]))([a-zA-Z0-9@#$%^!&+=*.\-_]){8,}$', data['password']):
                return JsonResponse({'message':'NOT_PASSWORD_FORMAT'}, status = 400)
            #핸드폰번호 양식
            if not re.search(r'^\d{3}-\d{3,4}-\d{4}$',data['phone_number']):
                return JsonResponse({'message':'INVALID_PHONE_NUMBER'}, status = 400)
            #이메일 중복확인
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'INVALID_EMAIL'}, status = 400)

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password,
                phone_number = data['phone_number'],
                birthday     = data['birthday'],
            )   
            return JsonResponse({'message':'SUCCESS'}, status = 201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)

class LoginView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            #가입된이메일 확인
            if not User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message':'INVALID_EMAIL'}, status = 401)

            #가입된 이메일과 패스워드가 맞는지 확인
            user = User.objects.get(email= data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status = 401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm= 'HS256')

            return JsonResponse({'token': access_token}, status = 200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)       