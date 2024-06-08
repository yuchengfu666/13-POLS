from django import forms
from django.contrib import auth
from app.models import UserInfo
from django.views import View
from django.http import JsonResponse


class LoginBaseFrom(forms.Form):
    name = forms.CharField(error_messages={'required': '请输入用户名'})
    pwd = forms.CharField(error_messages={'required': '请输入密码'})
    code = forms.CharField(error_messages={'required': '请输入验证码'})

    def __init__(self, *args, **kwargs):
        #
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        # 局部钩子

    def clean_code(self):
        code = self.cleaned_data.get('code')
        valid_code = self.request.session.get('valid_code')
        if code.upper() != valid_code.upper():
            self.add_error('code', '验证码输入错误!')
        return self.cleaned_data


# 登陆的字段验证
class LoginForm(LoginBaseFrom):

    # 全局钩子
    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')
        print(name)
        print(pwd)
        user = auth.authenticate(username=name, password=pwd)
        print(user)

        if not user:
            # 为我们的字段添加错误信息
            self.add_error('pwd', '用户名或密码错误')
            return self.cleaned_data

        # 把用户对象放到cleaned_data中
        self.cleaned_data['user'] = user
        return self.cleaned_data


# 注册的字段验证
class SignForm(LoginBaseFrom):
    re_pwd = forms.CharField(error_messages={'required': '请确认密码'})

    # 重写init方法

    # 全局钩子
    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd != re_pwd:
            self.add_error('re_pwd', '两次密码不一致')
        return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        user_query = UserInfo.objects.filter(username=name)
        if user_query:
            self.add_error('name', '该用户已注册')
        return self.cleaned_data


# CBV
# 登录失败可复用代码
def clean_form(form):
    err_dict: dict = form.errors
    # 拿到所有错误字段的名字
    err_valid = list(err_dict.keys())[0]
    # 拿到第一个字段的第一个信息
    err_msg = err_dict[err_valid][0]
    return err_valid, err_msg


class LoginView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': "登录成功!",
            "self": None
        }

        form = LoginForm(request.data, request=request)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)

        # 执行登录操作
        user = form.cleaned_data.get('user')
        # 登录操作
        auth.login(request, user)

        res['code'] = 0
        return JsonResponse(res)


class SignView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': "注册成功",
            "self": None,
        }
        form = SignForm(request.data, request=request)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        # 注册成功代码
        user = UserInfo.objects.create_user(
            username=request.data.get('name'),
            password=request.data.get('pwd')
        )
        auth.login(request, user)
        res['code'] = 0

        return JsonResponse(res)
