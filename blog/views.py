from django.shortcuts import render
from blog.models import Category, Post #카테고리, 게시글 관리
from django.views import generic #글의 세부 내용 작성
from django.contrib.auth.mixins import LoginRequiredMixin #로그인한 사람들
from django.views.generic.edit import CreateView

#index view 처리요청이 들어오면 index.html이라는 페이지로 처리를 함
def index(req):
    #데이터를 최근에 작성된 순서로 가지고 올 수 있도록
    post_latest = Post.objects.order_by("-createDate")[:6]
    context= {
        "post_latest": post_latest
    }
    return render(req, "index.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView): #로그인하고, 장고에서제공하는 뷰기능사용
    model = Post
    fields = ["title", "title_image", "content", "category"]