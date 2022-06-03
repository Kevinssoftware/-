# 请求 URL: https://music.163.com/discover/toplist
import requests
import re
import os
#<a href="/discover/toplist\?id=(\d+)" class="s-fc0">(.*?)</a>
def each (bangid,bang_name):

    fillname = "music\\"+bang_name+"\\"
    if not os.path.exists(fillname):
        os.mkdir(fillname)
    # <a href="/song?id=(\d+)">(.*?)</a></li><li>
    # <li><a href="/song\?id=(\d+)">(.*?)</a>
    #http://music.163.com/song/media/outer/url?id=1925452719.mp3
    url = f"https://music.163.com/discover/toplist?id={bangid}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
    }
    page  = requests.get(url=url,headers=headers)
    lists = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>',page.text)
    for id,title in lists:
        music_url = f"http://music.163.com/song/media/outer/url?id={id}.mp3"
        music_content = requests.get(url=music_url,headers=headers).content
        with open(fillname+title+".mp3",mode="wb") as f:
            f.write(music_content)
            print(title+'成功下载')

def id():
    url = "https://music.163.com/discover/toplist?id=2884035"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
    }
    id_page = requests.get(url=url,headers=headers)
    ids =re.findall('<a href="/discover/toplist\?id=(\d+)" class="s-fc0">(.*?)</a>',id_page.text)
    for id,name in ids:
        print(name)
        each(id,name)
if __name__ == '__main__':
    id()