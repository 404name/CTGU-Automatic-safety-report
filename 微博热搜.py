# https://s.weibo.com/top/summary/
import requests
from bs4 import BeautifulSoup
import lxml


def wb():
    news = []
    # 新建数组存放热搜榜
    hot_url = 'https://s.weibo.com/top/summary/'
    # 热搜榜链接
    r = requests.get(hot_url, timeout=None)
    # 向链接发送get请求获得页面
    soup = BeautifulSoup(r.text, 'lxml')
    # 解析页面

    urls_titles = soup.select(
        '#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    hotness = soup.select(
        '#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')

    # for i in range(len(urls_titles)-1):
    hot_news = "【微博每日热搜爬虫0v0】\n"
    for i in range(10):
        # 将信息保存到字典中
        hot_news += '[' + str(i+1) + '] :' + \
            urls_titles[i+1].get_text() + '\n'
        # get_text()获得a标签的文本
        # hot_news['url'] = "https://s.weibo.com"+urls_titles[i]['href']
        # ['href']获得a标签的链接，并补全前缀
        # hot_news['hotness'] =
        # 获得热度文本
        # 字典追加到数组中
    hot_news += "———————————\n"
    hot_news += "我是Qmsg酱消息机器人喔\n"
    return hot_news


def sentMsg(msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://qmsg.zendee.cn/sent/49bdb9375842537a41ebc635a09229b2?msg= %s" % msg
    return requests.post(api_url, headers=headers, timeout=None).content


sentMsg(wb())
