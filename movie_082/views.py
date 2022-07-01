from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieCreateForm, MovieUpdateForm
from django.contrib import messages
# Create your views here.
def home(request):
    movies=Movie.objects.all()
    return render(request,'movie_082/home.html',{'movies':movies})

def movieadd(request):
    if request.method == 'POST':
        print("here")
        form = MovieCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie has been added successfully')  
            return redirect('home')
    else:
        form = MovieCreateForm()
    return render(request, 'movie_082/movieadd.html',{'form':form})

def movieupdate(request,pk):
    movie = Movie.objects.get(pk=pk)
    form =MovieUpdateForm(instance=movie)
    if request.method =='POST':
        form =MovieUpdateForm(request.POST,instance=movie)
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Movie rating updated successfully')  
        return redirect('home')
  
    # else:  
    #     form = MovieUpdateForm()  
    movie_name = movie.name
    
    return render(request,'movie_082/movieupdate.html',{'form':form, 'name':movie_name})

