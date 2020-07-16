from django.shortcuts import render

#index view 처리요청이 들어오면 index.html이라는 페이지로 처리를 함
def index(req):
    context= {

    }
    return render(req, "index.html", context=context)

def single(req):
    context={

    }
    return render(req, "single.html", context=context)