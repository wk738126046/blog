from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # CharField：普通的文本
    # TextField：长文本
    # DateTimeField：日期时间类型
    # ForeignKey：外键类型

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


