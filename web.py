import requests
from bs4 import BeautifulSoup
import time
import re

#文字爬虫（Text crawler）
def get(a,b,c,x):
    while a != "" and b != "" and c != "" and x != "":
        try:
            response = requests.get(a)
            response.encoding = x
            bs = BeautifulSoup(response.text, 'html.parser')
            writer_list = bs.find_all(b,class_= c)
            with open("file.txt","w",encoding='utf-8') as f:
                for writer in writer_list:
                    print(writer.get_text())
                    f.write(writer.get_text())
                    time.sleep(1)
            print("文件已保存成功!")    
        except Exception as e:
            print(e)

def got(a,b,x):
    while a != "" and b != "" and x != "":
        try:
            response = requests.get(a)
            response.encoding = x
            bs = BeautifulSoup(response.text, 'html.parser')
            writer_list = bs.find_all(b)
            with open("file.txt","w",encoding='utf-8') as f:
                for writer in writer_list:
                    print(writer.get_text())
                    f.write(writer.get_text())
                    time.sleep(1)
            print("文件已保存成功!")    
        except Exception as e:
            print(e)
#图片爬虫（Picture crawler）
def gut(a):
    while a != "":
        try:
            response = requests.get(a)
            with open('img/pic.png', 'wb') as file:
                file.write(response.content)
        except Exception as e:
            print(e)
#多图片爬虫（Multi picture crawler）
def gat(a,x):
    while a != "" and x != "":
        try:
            response = requests.get(a)
            response.encoding = x
            url_list = re.findall('https.*png',response.text)
        except Exception as e:
            print(e)

        for url in url_list:
            try:
                response = requests.get(url)
                content_list = url.split('/')
                img_name = content_list[-1]
                img_path = 'img/' + img_name
                with open(img_path, 'wb') as file:
                    file.write(response.content)
            except Exception as e:
                print(e)
            time.sleep(1)






        

