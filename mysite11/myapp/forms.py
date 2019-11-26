from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from .models import TokenList, tokensell, Company_info


User = get_user_model()
#User.objects.all()
class SignupForm(ModelForm): #회원가입을 제공하는 class이다.
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
#아쉽게도 User 모델에서는 password_check 필드를 제공해주지 않는다.
#따라서 따로 password_check 필드를 직접 정의해줄 필요가 있다.
#입력 양식은 type은 기본이 text이다. 따라서 다르게 지정해주고 싶을 경우 widget을 이용한다.
#widget=forms.PasswordInput()은 입력 양식을 password로 지정해주겠다는 뜻이다.

    field_order=['username','password','password_check','last_name','first_name','email']
#field_order는 만들어지는 입력양식의 순서를 정해준다.
#여기서 사용한 이유는 password 바로 밑에 password_check 입력양식을 추가시키고 싶어서이다.
#만약 따로 field_order를 지정해주지않았다면, password_check는 맨 밑에 생성된다.

    class Meta:
        model=User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password','last_name','first_name','email']
#User model에 정의된 username, passwordm last_name, first_name, email을 입력양식으로



class SigninForm(forms.ModelForm): #로그인을 제공하는 class이다.
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password']

class uploadForm(forms.Form): # 이미지 업로드를 위한 form
        compname = forms.CharField(label = "회사명")
        introduce = forms.CharField(label = "회사소개", help_text="회사 소개를 5000자 이내로 입력해주세요", widget = forms.TextInput(attrs ={'class':"introduce"} ))
        preemail = forms.EmailField(label = "이메일주소")
        image = forms.ImageField(label= "이미지")

        # 토큰 등록하기#
        tokenname = forms.CharField(label = "토큰명")
        initial = forms.CharField(label = "토큰이니셜")
        quota = forms.FloatField(label = "발행 개수")
        divide = forms.ChoiceField(label = "분할 자릿수", help_text="토큰을 분할할 최대 자릿수를 입력해주세요", choices = ([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'), ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18')]))
        price = forms.FloatField(label = "토큰 가격(개/원)")


