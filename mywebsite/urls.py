"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#블로그를 만들기 위해 필요한 라이브러리 추가
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# blog주소로 들어오면 블로그앱(blog밑에 만들어둔 urls.py)이 처리하게 해주고
# 기본 사이트 주소로 들어오면 블로그로 넘겨주게 구현
# http://localhost:9000/blog/
urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", RedirectView.as_view(url="blog/", permanent=True)),
]
# 자바스크립트,css 같은 정적파일들을 처리할 수 있도록 셋팅
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
