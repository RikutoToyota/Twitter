# app/models.py

from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)

    def __str__(self):
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)  # スレッド作成者の名前を追加
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)  # コメント投稿者の名前
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.comment}"

class Tweet(models.Model):
    message = models.CharField(max_length=200)
    come_name = models.CharField(max_length=200)
    come_email = models.CharField(max_length=200)

# 追加した関連付け
# related_nameを使って、Threadから関連するコメント(Post)にアクセスできるようにしています
Thread.posts = property(lambda self: Post.objects.filter(thread=self))


