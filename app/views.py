from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("Hello World!")
    # return render(request, "index.html")
    # return redirect('/shows')
