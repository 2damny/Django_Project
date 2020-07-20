from django.db import models
# 모델 정의
from django.urls import reverse

# Create your models here.
# 글의 분류(일상, 유머, 종류)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")
    #def __str__은 자기를 어떻게 표현할것인지 정의
    def __str__(self):
        return self.name

# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    #대표이미지(빈칸일수도있음)
    title_image = models.ImageField(blank=True)
    #글의내용
    content = models.TextField()
    #글의작성일
    createDate = models.DateTimeField(auto_now_add=True)
    #글의수정일
    updateDate = models.DateTimeField(auto_now_add=True)
    #글의분류(하나의 글을 여러가지의 분류에 해당 될 수 있다.(ex:정보, 유머), 하나의 분류에는 여러가지 글이 포함될 수 있다.(ex:정보 카테고리에 글 10개))
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")
    
    def __str__(self):
        return self.title
        
    #1번글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    
    # 내용이 300자가 넘는지
    def is_content_more300(self):
        return len(self.content) > 300

    # 내용이 300자까지만 내용 받기
    def get_content_under300(self):
        return self.content[:300]