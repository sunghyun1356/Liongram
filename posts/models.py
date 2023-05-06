from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    image = models.ImageField(verbose_name = '이미지', null=True, blank=True)
    #verbose는 자세한 설명, null값 허용, blank도 허용
    content = models.TextField(verbose_name ='내용')
    created_at = models.DateTimeField(verbose_name ='작성일', auto_now_add=True)
    #auto_now_add 자동으로 추가
    view_count = models.IntegerField(verbose_name ='조회수', default =0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    #on_delete=models.CASCADE 삭제되면 관련된것들 삭제하기
    

class Comment(models.Model):
    content = models.TextField(verbose_name ='내용')
    created_at = models.DateTimeField(verbose_name = '작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
