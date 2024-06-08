from django.utils.deprecation import MiddlewareMixin
import json


# 解析post请求的数据
class Md1(MiddlewareMixin):
    # 请求中间件
    def process_request(self, request):
        if request.method =='POST':
            data = dict_data = json.loads(request.body)
            # print(data)
            request.data = data

    # 响应中间件
    def process_response(self, request, response):
        # print('响应')
        return response
