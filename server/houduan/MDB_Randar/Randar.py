from pymysql import cursors
import requests
from lxml import etree
from queue import Queue
import time
from random import shuffle
from requests import status_codes
import pymysql
import re

# db = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123456',
#     database='nar')
db = pymysql.connect(
    host="bj-cynosdbmysql-grp-eloic4ac.sql.tencentcdb.com",
    port=21320,
    user="root",
    password='lhllhl828..',
    database='BioPlatform')


# db = pymysql.connect(
#     host='172.31.246.30',
#     port=3307,
#     user='stu1',
#     password='dachuang1234',
#     database='dachuang_li')

def format_str(ss):
    res = ss.replace("\n", "").replace("\t", "")
    res = res.replace("\r", "")
    res = re.sub(" +", " ", res)
    return res

def format_url(urls_list):
    urlist = urls_list
    for url in urlist:
        if 'www' in url:
            continue
        elif url == '':
            urlist.remove(url)
    return urlist

class Randar:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'}
        self.queue = Queue()
        self.cururl = ''
        self.records = []
        self.linkform = []
        self.relationform = []
        self.count = 0
        
    def init_queue(self, urlist):
        for url in urlist:
            self.queue.put(url)
        
    def get_url(self):
        self.cururl = self.queue.get()
        try:
            self.res = requests.get(url=self.cururl, headers=self.headers, timeout=5)
            self.res.raise_for_status()
            self.records.append(self.cururl)
        except Exception as e:
            print(e.__context__)
    
    def parse(self):
        # print(type(self.res.text))
        
        print("--------------< fetch all urls >--------------")
        html = etree.HTML(self.res.text.encode('utf-8'))
        try:
            url_path = html.xpath('//a/@href')
            url_path = list(set(url_path))
            for urlp in url_path:
                if 'www' in urlp:
                    continue
                else:
                    url_path.remove(urlp)
            print("examples: {}".format(url_path[0]))
            print("--------------< Successfully fetched >--------------")
        except Exception as e:
            print("[Error]", e.__context__)
            
            
        print("--------------< fetch this url details >--------------")
        # sli = html.xpath('.//title/text()')
        # title = format_str("".join(sli))
        # if title == '':
        
        
        curent_url = format_str(self.cururl)
        title = curent_url
        sli = html.xpath("//p/text()")[:8]
        sli = [format_str(ss) for ss in sli]
        sstr = " ".join(sli)
        texts = sstr
        self.linkform.append((title, curent_url, texts))
        
        print("title:", title)
        print("url:", curent_url)
        print("introduction:", texts)
        print("--------------< Successfully fetched >--------------")
        
        print("--------------< Begin to bulid net >--------------")
        for ul in url_path:
            self.queue.put(ul)
            if 'www' in ul:
                self.relationform.append((curent_url, ul))
                self.count += 1
    
    def back_url(self):
        return self.records
    
    def status_for_queue(self):
        return self.queue.empty()
    
    def rc_linkform(self):
        res = self.linkform
        self.linkform = []
        return res 
    
    def rc_relationform(self):
        res = self.relationform
        self.relationform = []
        return res   
    
def get_db_url():
    cursor = db.cursor()
    res = []
    sql = "SELECT dbname, db_url FROM mdatabases "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            dbname = row[0]
            db_url = row[1]
            res.append(db_url)
    except Exception as e:
        print(e.__context__)
    cursor.close()
    return res
    

def insert_web_link(links):
    cursor = db.cursor()
    print("--------------< Insert the web link >--------------")
    try:
        sql = "insert into weblink (title, durl, introduction) values (%s, %s, %s)"
        cursor.executemany(sql, links)
        db.commit()
        print("--------------< Successfully inserted >--------------")
    except Exception as e:
        db.rollback()
        print(e.__context__)    
    cursor.close()
       
       
def insert_edges(edges):
    cursor = db.cursor()
    print("--------------< Insert the edges >--------------")
    try:
        sql = "insert into edges (url1, url2) values (%s, %s)"
        cursor.executemany(sql, edges)
        db.commit()
        print("--------------< Successfully inserted >--------------")
    except Exception as e:
        db.rollback()
        print(e.__context__)    
    cursor.close() 
    
if __name__ == '__main__':
    # Step 1: Get the db url
    res = get_db_url()
    res = format_url(res)
    print("The Number of the BioDB in BioPlatform is ", len(res))
    shuffle(res)
    
    # Step 2: Activate the randar  per 100 per insert
    rr = Randar()
    if rr.status_for_queue:
        rr.init_queue(res)
    node_sum = 5000
    i = 0
    while rr.status_for_queue is not False:
        # 1. get html text
        rr.get_url()
        
        # 2. parse the html text
        rr.parse()
        i += 1
        
        # 3. insert into the database
        # can get many many links, but just 5000 try it
        if i % 3 == 0:
            links = rr.rc_linkform()
            insert_web_link(links)
            print(links)
            print("[OK] Successfully insert! Links are as follows:")
            time.sleep(1)
            propertys= rr.rc_relationform()
            insert_edges(edges=propertys)
            print(propertys)
            time.sleep(1)
    
        if i > node_sum:
            break
    
    