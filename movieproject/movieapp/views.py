
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Movies
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import MovieForm
# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,'index.html',context)

def AllMovies(request):
    category = request.GET.get('i')

    if category == None:
        movies = Movies.objects.all()
    else:
        movies = Movies.objects.filter(category__name=category)

    paginator = Paginator(movies, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except(EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    context = {
        'movies': movies,
        'categories': categories,

    }

    return render(request, 'moviegrid.html', context)

def movieDetail(request, id):
    categories = Category.objects.all()
    movie = Movies.objects.get(id=id)
    context = {
        'movie': movie,
        'categories': categories
    }
    return render(request, 'moviesingle.html', context)

def addmovie(request):
   categories = Category.objects.all()
   form=MovieForm()
   if request.method == 'POST':
       form=MovieForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('movieapp:allmovie')
   context={
      "form":form,
      'categories': categories
   }
   return render(request,'add.html',context)

def updatemovie(request,id):
    categories = Category.objects.all()
    movie = Movies.objects.get(id=id)

    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movieapp:allmovie')

    context = {
        "form":form,
        'categories': categories

    }

    return render(request, 'update.html', context)

def deletemovie(request, id):
    movie = Movies.objects.get(id=id)
    movie.delete()
    return redirect('movieapp:allmovie')
