#提升版本:把所有的请求都写成一个可复用的函数
#1.根据你的需求判断是进行get请求还是post请求
#2.注册、登陆、充值、提现全部复用一个http请求函数

# import requests
# def http_request(url,data,header,method):
#     if method=='get':
#         result=requests.get(url,json=data,headers=header)
#     else:
#         result=requests.post(url,json=data,headers=header)
#     return result.json    #renturn返回指定的结果
#
# if __name__ == '__main__':
#
#
#     #调用函数
#     #头部
#     header={'X-Lemonban-Media-Type':'lemonban.v2'}
#     #登陆
#     login_url='http://120.78.128.25:8766/futureloan/member/login'
#     login_data={'mobile_phone':18688889027,'pwd':'123456789021'}
#     response=http_request(login_url,login_data,header,'post')
#
#     #充值
#     token=response['data']['token_info']['token']
#     header_2={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':'Bearer '+token}
#     rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
#     rec_data={'member_id':206535,'amount':50000}
#     print(http_request(rec_url,rec_data,header_2,'post'))
#
#     import requests
#     def http_request(url,data,header,method:'post'):
#         if method=='get':
#             result=requests.get(url,json=data,headers=header)
#         else:
#             result=requests.post(url,json=data,headers=header)
#         return result.json()    #renturn返回指定的结果
#     #调用函数
#     #头部
#     header={'X-Lemonban-Media-Type':'lemonban.v2'}
#     #登陆
#     login_url='http://120.78.128.25:8766/futureloan/member/login'
#     login_data={'mobile_phone':18688889027,'pwd':'123456789021'}
#     response=http_request(login_url,login_data,header,'post')
#     print('登陆的结果是:{}'.format(response))
#     #充值
#     header_2={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':'Bearer '+response['data']['token_info']['token']}
#     rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
#     rec_data={'member_id':response['data']['id'],'amount':50000}
#     print(http_request(rec_url,rec_data,header_2,'post'))


import requests
def http_request(url,data,token=None,method='post'):
    header= {'X-Lemonban-Media-Type': 'lemonban.v2','Authorization':token}
    if method=='get':
        result=requests.get(url,json=data,headers=header)
    else:
        result=requests.post(url,json=data,headers=header)
    return result.json()    #renturn返回指定的结果

if __name__ == '__main__':

    #调用函数
    #登陆
    login_url='http://120.78.128.25:8766/futureloan/member/login'
    login_data={'mobile_phone':18688889027,'pwd':'123456789021'}
    response=http_request(login_url,login_data)
    print('登陆的结果是:{}'.format(response))

    #充值
    token=response['data']['token_info']['token']
    rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data={'member_id':206535,'amount':50000}
    print(http_request(rec_url,rec_data,'Bearer '+token))
#由于‘Bearer'不能与None值拼接在一起
#token不需要判断为空，因为在登陆的时候，不管Authorization传什么值都不校验，只有充值的时候，必须传一个token值


    # import requests
    # def http_request(url,data,header,method:'post'):
    #     if method=='get':
    #         result=requests.get(url,json=data,headers=header)
    #     else:
    #         result=requests.post(url,json=data,headers=header)
    #     return result.json()    #renturn返回指定的结果
    # #调用函数
    # #头部
    # header={'X-Lemonban-Media-Type':'lemonban.v2'}
    # #登陆
    # login_url='http://120.78.128.25:8766/futureloan/member/login'
    # login_data={'mobile_phone':18688889027,'pwd':'123456789021'}
    # response=http_request(login_url,login_data,header,'post')
    # print('登陆的结果是:{}'.format(response))
    # #充值
    # header_2={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':'Bearer '+response['data']['token_info']['token']}
    # rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
    # rec_data={'member_id':response['data']['id'],'amount':50000}
    # print(http_request(rec_url,rec_data,header_2,'post'))