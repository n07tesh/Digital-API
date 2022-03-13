from django.shortcuts import render
from app.models import Movie
from django.http import JsonResponse

# Create your views here.
# def home(request):
#     return render(request,'home.html')
def movie_list(request):
    movies  = Movie.objects.all()
    data = {
        'movies' : list(movies.values())
    }
    return JsonResponse(data)

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name' : movie.name,
        'description' : movie.description,
        'active' : movie.active
    }
    #movie = Movie.objects.get(pk=pk)
    return JsonResponse(data) 