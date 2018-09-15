from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE) # 속성을 정의하기위해, 필드마다 어떤 종류의 데이터 타입을 가지는지를 정하는 것
    title=models.CharField(max_length=200) # CharField는 글자 수가 제한된 텍스트를 정의 제목같이 짧은 문자열 정보를 저장할 때 사용
    text=models.TextField() # TextFiled는 글자수에 제한이 없는 긴 텍스트를 위한 속성
    created_date=models.DateTimeField(default=timezone.now) # 날짜와 시간
    published_date=models.DateTimeField(blank=True, null=True) # 다른 모델에 대한 링클를 의미

    def publish(self):
        self.published_date= timezone.now()
        self.save()

    def __str__(self):
        return self.title

