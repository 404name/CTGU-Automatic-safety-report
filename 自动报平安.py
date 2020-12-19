import requests


def sentMsg(msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://qmsg.zendee.cn/send/af83ed8cfbb3e7a2ea86f286c86e5c86?msg= %s" % msg
    return requests.post(api_url, headers=headers).content


text = '测试'
print(sentMsg(text))
