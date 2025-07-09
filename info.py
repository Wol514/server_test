import requests
import re
from bs4 import BeautifulSoup
import datetime

# 获取当天拼接链接的招标信息
def get_bid_joint(input):
    res = []
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }
    r = requests.get(input["链接"][0]["text"],headers=header)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    info = eval(input["列表字段"][0]["text"])
    contents = soup.find('ul', attrs={info["attr"]:info["value"]}).find_all('li')
    for content in contents:
        # print(content)
        url = input["拼接链接"][0]["text"]+ content.find('a')['href']
        title = content.find(input["标题"][0]["text"]).text
        time = content.find(input["日期"][0]["text"]).text
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        # 获取昨日的信息
        if(time==yesterday):
            # 筛选
            if re.search('(技术改造|课题|后评价|可行性研究|监理|项目管理|全过程咨询)', title):
                text = '项目名称:' + title + '\n公告日期:' + time + '\n'

                r = requests.get(url, headers=header)
                soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
                artile = eval(input["文章字段"][0]["text"])
                contents = soup.find('div', attrs={artile["attr"]: artile["value"]}).find_all('p')

                for content in contents:
                    text += content.text
                    text += '\n'
                print(text)
                res.append(text)
    return res

# 获取非拼接链接的招标信息
def get_bid_unjoint(input):
    res = []
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }
    r = requests.get(input["链接"][0]["text"], headers=header)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    info = eval(input["列表字段"][0]["text"])
    contents = soup.find('ul', attrs={info["attr"]: info["value"]}).find_all('li')
    for content in contents:
        # print(content)
        url = content.find('a')['href']
        title = content.find(input["标题"][0]["text"]).text
        time = content.find(input["日期"][0]["text"]).text
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        # 获取昨日的信息
        if (time == yesterday):
            # 筛选
            if re.search('(技术改造|课题|后评价|可行性研究|监理|项目管理|全过程咨询)', title):
                text = '项目名称:' + title + '\n公告日期:' + time + '\n'

                r = requests.get(url, headers=header)
                soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
                artile = eval(input["文章字段"][0]["text"])
                contents = soup.find('div', attrs={artile["attr"]: artile["value"]}).find_all('p')

                for content in contents:
                    text += content.text
                    text += '\n'
                print(text)
                res.append(text)
    return res

# 获取拼接链接的中标信息
def get_bfw_joint(input):
    res = []
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }
    r = requests.get(input["链接"][0]["text"], headers=header)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    info = eval(input["列表字段"][0]["text"])
    contents = soup.find('ul', attrs={info["attr"]: info["value"]}).find_all('li')
    for content in contents:
        # print(content)
        url = content.find('a')['href']
        title = content.find(input["标题"][0]["text"]).text
        time = content.find(input["日期"][0]["text"]).text
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        # 获取昨日的信息
        if (time == yesterday):
            # 筛选
            if re.search('中标.*公示', title):
                text = '项目名称:' + title + '\n公告日期:' + time + '\n'

                r = requests.get(url, headers=header)
                soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
                artile = eval(input["文章字段"][0]["text"])
                contents = soup.find('div', attrs={artile["attr"]: artile["value"]}).find_all('p')

                for content in contents:
                    text += content.text
                    text += '\n'
                print(text)
                res.append(text)
    return res

# 获取非拼接链接的中标信息
def get_bfw_unjoint(input):
    res = []
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }
    r = requests.get(input["链接"][0]["text"], headers=header)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    info = eval(input["列表字段"][0]["text"])
    contents = soup.find('ul', attrs={info["attr"]: info["value"]}).find_all('li')
    for content in contents:
        # print(content)
        url = content.find('a')['href']
        title = content.find(input["标题"][0]["text"]).text
        time = content.find(input["日期"][0]["text"]).text
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        # 获取昨日的信息
        if (time == yesterday):
            # 筛选
            if re.search('中标.*公示', title):
                text = '项目名称:' + title + '\n公告日期:' + time + '\n'

                r = requests.get(url, headers=header)
                soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
                artile = eval(input["文章字段"][0]["text"])
                contents = soup.find('div', attrs={artile["attr"]: artile["value"]}).find_all('p')

                for content in contents:
                    text += content.text
                    text += '\n'
                print(text)
                res.append(text)
    return res