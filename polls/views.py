import json
import urllib.request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie_search, Book_search # Movie_info,


def search(request):

    if request.method == 'GET':

        client_id = "DshukL7WQcANLYUiQTsY"
        client_secret = "p5RxLlzjyJ"

        q = request.GET.get('q')

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
            print(result)

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

        context = {
                'items':items
        }

        return render(request, 'search/searchbook.html', context=context)




