import sys
import requests as r
import json
import telepot

tele_enable=False
sign='https://n.cg.163.com/api/v2/sign-today'
current='https://n.cg.163.com/api/v2/client-settings/@current'
cookie=''
teleid=0
teletoken=''
if len(sys.argv)==1:
    print('[网易云游戏自动签到]未设置cookie，正在退出……')
elif len(sys.argv)==2:
    cookie=sys.argv[1]
    teleid=0
    teletoken=''
elif len(sys.argv)==4:
    cookie=sys.argv[1]
    teleid=sys.argv[2]
    teletoken=sys.argv[3]
    tele_enable=True

getheader={
    'Host': 'n.cg.163.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Platform': '0',
    'Authorization': str(cookie),
    'Origin': 'https://cg.163.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cg.163.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5'  
}

signheader={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
    'Authorization': str(cookie),
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'n.cg.163.com',
    'Origin': 'https://cg.163.com',
    'Referer': 'https://cg.163.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Platform': '0'
}

def signin(url,header):
    result=r.post(url=url,headers=header)
    return result

def getme(url,header):
    result=r.get(url=url,headers=header)
    return result


if __name__ == "__main__":
    me=getme(current,getheader)
    if(me.status_code!=200):
        message='[网易云游戏自动签到]签到失败！请检查Cookie是否过期！或者附上报错信息到 https://github.com/GamerNoTitle/wyycg-autosignin/issues 发起issue'
        send(teleid,message)
        print(message)
        sys.exit()
    sign=signin(sign,signheader)
    if(sign.status_code==200):
        message='[网易云游戏自动签到]签到成功！'
        print(message)
    else:
        message='[网易云游戏自动签到]签到失败，回显状态码为{}\n具体错误信息如下：\n{}'.format(sign.status_code,sign.text)
        print(message)
