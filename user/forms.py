from django import forms
from .models import User
from django.contrib.auth.hashers import check_password, make_password


class RegisterForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required':'please enter the userid'
        },
        max_length=128, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': 'please enter the password'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': 'please enter the re_password'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )
    nickname = forms.CharField(
        error_messages={
            'required': 'please enter the nickname'
        },
        max_length=64, label='닉네임'
    )
    def clean(self):    #유효성 검사
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('re_password')
        nickname = cleaned_data.get('nickname')

        if password and repassword:
            if password != repassword:
                self.add_error('password', 'password, repassword incorrect')
                self.add_error('repassword', 'password, repassword incorrect')




class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': 'please enter the userid'
        },
        max_length=128, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': 'please enter the password'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

#사용자가 맞는지 확인

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('usreid')
        password = cleaned_data.get('password')

        if userid and password:#userid와 password가 입력되었을때
            try:
                user = User.objects.get(userid=userid)
            except User.DoesNotExist:
                self.add_error('userid', 'userid not existed')
                return

            if not check_password(password, user.password):
                self.add_error('password', 'password Wrong')
