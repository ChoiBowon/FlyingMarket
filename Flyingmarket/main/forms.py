# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
###############################

# User = get_user_model()
#
# class SignupForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class':'form-control',
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class':'form-control',
#             }
#         )
#     )
#
#     #비번 확인
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )
#
#     # 아이디 유효성 검사
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError('이미 사용중인 아이디입니다')
#         return username
#
#     #비번1 비번2 일치하는지 검사
#     def clean_password2(self):
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']
#         if password1 != password2:
#             raise forms.ValidationError('비밀번호와 비밀번호 확인란이 일치하지않습니다')
#         return password2
#
#     #username 이랑 password 로 새로운 user 생성
#     def signup(self):
#         if self.is_valid():
#             return User.objects.create_user(
#                 username=self.cleaned_data['username'],
#                 password=self.cleaned_data['password2'],
#             )