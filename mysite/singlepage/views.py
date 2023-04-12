from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, "singlepage/index.html")

texts = ["Строка 1",
        "Строка 2",
        "Строка 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("NO SUCH CONTENT!")