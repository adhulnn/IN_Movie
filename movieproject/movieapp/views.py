from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def view_movie(req):
    movie = Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(req,'index.html',context)

def details(req,movie_id):
    movie = Movie.objects.get(id=movie_id)
    context={
        'movies':movie
    }
    return render(req,'details.html',context)

def add_movie(req):
    if req.method == "POST":
        movie = MovieForm(req.POST, req.FILES)
        if movie.is_valid():
            movie.save()
            messages.success(req,'Movie Added Successfully')
            return redirect('/') 
        else:
            return render(req,'add_movie.html',{'form':movie})
    else:
        movie_form=MovieForm()
        return render(req,'add_movie.html',{'form':movie_form})

def update_movie(req,id):
    movie=Movie.objects.get(id=id)
    if req.method == "POST":
        movie = MovieForm(req.POST, req.FILES, instance=movie)
        if movie.is_valid():
            movie.save()
            messages.success(req,'Movie Updated Successfully')
            return redirect('/')
    else:
        movie_form=MovieForm(instance=movie)
        return render(req,'update_movie.html',{'form':movie_form})


def del_movie(req, id):
    movie=Movie.objects.get(id=id)
    movie.delete()
    messages.success(req,'Movie Deleted Successfully')
    return redirect('/')