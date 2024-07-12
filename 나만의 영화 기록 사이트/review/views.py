from django.shortcuts import render, redirect
from .models import Review
# Create your views here.
def review_list(request):
    reviews=Review.objects.all()
    context={
        'reviews':reviews,
    }
    return render(request, 'review_list.html', context)

def review_create(request):
    if request.method == 'POST':
        Review.objects.create(
            title=request.POST['title'],
            year=request.POST['year'],
            genre=request.POST['genre'],
            rating=request.POST['rating'],
            running_time=request.POST['running_time'],
            content=request.POST['content'],
            director=request.POST['director'],
            actors=request.POST['actors'],
        )
        return redirect("/review")
    return render(request, 'review_create.html')

def review_detail(request, pk) :
    review = Review.objects.get(id=pk)

    context={
        'review' : review,
    }
    return render(request, 'review_detail.html', context)

def review_update(request, pk):
    review=Review.objects.get(id=pk)
    if request.method=="POST":
        review.title=request.POST["title"]
        review.year=request.POST["year"]
        review.genre=request.POST["genre"]
        review.rating=request.POST['rating']
        review.running_time=request.POST['running_time']
        review.content=request.POST['content']
        review.director=request.POST['director']
        review.actors=request.POST['actors']
        
        review.save()
        
        return redirect(f"/review/{pk}")
        
    context={
        "review":review
    }
    return render(request, 'review_update.html', context)

def review_delete(request,pk):
    if request.method == 'POST':
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect('/review')