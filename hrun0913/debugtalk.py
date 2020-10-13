import hashlib
import time
import requests

def sleep(n_secs):
    time.sleep(n_secs)

# 实现登录的参数化
def get_params():
    '''
    可以有两种方式实现：
    1、获取列表套字典的数据结构
    2、获取列表套列表的数据结构
    :return:
    '''
    # 1、获取列表套字典的数据结构
    # accounts = [
    #     {'title':'正常登录','username':'admin','password':'1234','message':'success'},
    #     {'title':'密码为空','username':'admin','password':'','message':'用户名或密码不能为空'},
    #     {'title':'用户名为空','username':'','password':'1234','message':'用户名或密码不能为空'},
    #     {'title':'用户名和密码为空','username':'','password':'','message':'用户名或密码不能为空'},
    # ]

    # 2、获取列表套列表的数据结构
    account = [
        ['正常登录','admin','1234','success'],
        ['密码为空','admin','','用户名或密码不能为空'],
        ['用户名为空','','1234','用户名或密码不能为空'],
        ['用户名和密码为空','','','用户名或密码不能为空'],
    ]
    return account

# md5 加密
def sign():
    optCode = 'testfan'
    phoneNum = 1111
    timestamp = int(time.time()*1000)
    sign = str(phoneNum) + optCode + str(timestamp)

    # 进行 md5 加密
    md5_sign = hashlib.md5(sign.encode()).hexdigest()
    your_md5_sign = {"phoneNum":phoneNum,"optCode":optCode,"timestamp":timestamp,"sign":md5_sign}
    return your_md5_sign

# token 登录实现
def get_token():
    '''
    成功登录推后获取 token 值，供依赖 token 做请求的接口去用
    :return:
    '''
    url = 'http://192.168.0.13:8080/pinter/bank/api/login2'
    data = {
        'userName':'admin',
        'password':'1234'
    }
    # 发起请求
    resp = requests.post(url, data=data)
    try:
        token = resp.json().get('data')
    # 如果错误，就让 token 为空
    except:
        token = ''
    return token

# hook 函数使用演示（前置条件和后置条件处理）
def hook_up():
    print('前置执行 setup_hook')

def hook_down():
    print('后置执行 teardown_hook')

def hook_log(value):
    print(value)

# 调试功能
if __name__ == '__main__':
    print(get_params())
    print(sign())
    print(get_token())