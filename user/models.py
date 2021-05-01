from django.db import models

# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=128, verbose_name='아이디')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    nickname = models.CharField(max_length=64, verbose_name='닉네임', null=True)


    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'Trello_Clone_User'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'