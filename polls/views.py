import json
import urllib.request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie_search, Book_search, Product_search, User # Movie_info,


def search(request):

    if request.method == 'GET':

        client_id = "DshukL7WQcANLYUiQTsY"
        client_secret = "p5RxLlzjyJ"

        q = request.GET.get('q')

        userid=request.session['userid']
        if userid is True:
            userdata = User.objects.filter(email=userid)
            userdata.update(Lastproject=q)

            movie_search = Movie_search(
                keyword = q,
                age = userdata.age,
                sex = userdata.sex,
            )
        else:
            movie_search = Movie_search(
                keyword = q,
            )
        movie_search.save()

        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText #json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            #print(result)

            #movie_info = Movie_info(
            #    title = items[0]['title'],
            #    image_urls = items[0]['image'],
            #    pub_date = items[0]['pubDate'],
            #    director = items[0]['director'],
            #    actor = items[0]['actor'],
            #    userRating = items[0]['userRating'],)

            #movie_info.save()

            context = {
                'items':items
            }

            return render(request, 'search/index.html', context=context)

def searchbook(request):

    if request.method == 'GET':
        client_id = "DshukL7WQcANLYUiQTsY"
        client_secret = "p5RxLlzjyJ"

        q = request.GET.get('q')

        if userid is True:

            userid=request.session['userid']
            userdata = User.objects.filter(email=userid)
            userdata.update(Lastproject=q)
          
            book_search = Book_search(
                    keyword = q,
                    age = userdata.age,
                    sex = userdata.sex,
                )

        else:
            book_search = Book_search(
                keyword = q,
            )

        book_search.save()

        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/book?query=" + encText #json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            #print(result)
            context = {
                    'items':items
            }

            return render(request, 'search/searchbook.html', context=context)


def searchproduct(request):

    if request.method == 'GET':
        client_id = "DshukL7WQcANLYUiQTsY"
        client_secret = "p5RxLlzjyJ"

        q = request.GET.get('q')

        if userid is True:

            userid=request.session['userid']
            userdata = User.objects.filter(email=userid)
            userdata.update(Lastproject=q)

            product_search = Product_search(
                keyword = q,
                age = userdata.age,
                sex = userdata.sex,
                )
        else:
            product_search = Product_search(
                keyword = q,
            )
        product_search.save()

        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/shop?query=" + encText #json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            #print(result)

            context = {
                    'items':items
            }

            return render(request, 'search/searchproduct.html', context=context)

def opensigninpage(request):
    return render(request,'search/LoginPage.html')

def opensignuppage(request):
    return render(request,'search/SignUpPage.html')

def signup(request) :
    name=request.POST['name']
    email=request.POST['email']
    age = request.POST['age']
    sex = request.POST['sex']
    password=request.POST['password']
    #signuppage.html 에서 POST 방식으로 입력 받은 값을 전송 해주고, 받아오는 코드 
    userdata=User(name = name,email = email, age = age, sex = sex, password = password)
    #userdata에 User 클래스 필드에 값을 초기화 시켜 놓습니다
    if User.objects.filter(email=email).exists() is True : #입력받은 이메일이 DB에 존재 한다면! (이메일중복검사)
        messages.error(request,"이미 존재하는 이메일 입니다.") #error 타입으로 message를 보내줍니다.
        return render(request,'search/SignUpPage.html') 
    else : # 이메일이 중복되지 않은 경우 
        userdata.save() 
    
    userdatas=User.objects.all()
    userdatas={'userdatas':userdatas}
    return render(request,'search/index.html',userdatas)


def signin(request):
    input_email = request.POST.get('email',None)
    input_password=request.POST.get('password',None)
    #signin.html에서 받은 값을 체크하고, 없는경우 None 으로 설정 해줍니다.
    check_email=User.objects.filter(email=input_email).exists()
    #DB에 입력받은 email 이 있는지 체크하고 Ture False 로 return 받은 값을 check_email 에 초기화 시킵니다.
    if check_email is True : # email 은 일치 
        check_password=User.objects.filter(email=input_email,password=input_password).exists()
    
        if check_password is True : # password 도 일치
            
            projects = Project.objects.all()
            request.session['userid']=input_email
            request.session['flag'] = 0
            #request.session.set_expiry(0)
            #로그인한 유저를 저장하기 위해 session 에 저장을 해줍니다. 
            # ex ) {'userid' : input_email } 
            try :
                last_pjname=User.objects.filter(email=input_email).values('Lastsearch')
            except : 
                last_pjname=None

            context = {
                'check_email' : check_email
            }
            return render(request,'search/index.html',context)
        
        elif check_password is False : # email 은 일치, password는 불일치
            messages.error(request,"비밀번호가 일치하지 않습니다.")
            
    elif check_email is False:# email이 불일치 , password는 체크 X 
        messages.error(request,"존재하지 않는 이메일 입니다.")
    
    userdatas={'email' :input_email,'password':input_password}   
    return render(request,'search/index.html',userdatas)

