from django.http import JsonResponse


# 和前端一起协商每个状态码代表的含义
class HttpCode:
    ok = 200  # 一切正常
    params_error = 400  # 客户端传入的参数错误，比如密码过短
    un_auth = 401  # 没有授权（也就是被封号了）
    method_error = 405  # 请求的方法错误（比如post请求，传入了get）
    server_error = 500  # 服务器内部报错


# 封装JsonResponse，这里的kwargs还是有必要的
def result(code=HttpCode.ok, message='', data=None, kwargs=None):
    json_dict = {
        'code': code,
        'message': message,
        'data': data,
    }
    # 假设传入的字典里包含`token`，这里需要将其更新到`json_dict`中
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})


# 封装状态正常的方法
def ok(message='', data=None):
    return result()


# 封装参数错误
def params_error(message='', data=None):
    return result(code=HttpCode.params_error, message=message, data=data)


# 封装冻结用户错误
def un_auth(message='', data=None):
    return result(code=HttpCode.un_auth, message=message, data=data)


# 封装方法错误
def method_error(message='', data=None):
    return result(code=HttpCode.method_error, message=message, data=data)


# 封装服务器内部错误
def server_error(message='', data=None):
    return result(code=HttpCode.server_error, message=message, data=data)
