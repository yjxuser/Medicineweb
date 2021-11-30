import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pymysql
import time
import threading
import time
from io import BytesIO
'''
爬取PubMed
base_url : https://pubmed.ncbi.nlm.nih.gov/
url : base_url + ?term=keyword&page=num + herf

'''

class CatchMed:
    def __init__(self, keyword):
        chrome_options=Options()

        #设置chrome浏览器无界面模式
        chrome_options.add_argument('--headless')
        self.keyword = keyword
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver2 = webdriver.Chrome(options=chrome_options)
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        self.count = 0      #文章爬取计数器
        self.require_pages = 3
        self.records = []

    #获取每个paper自己的详情页
    def get_URL(self):
        page = 1
        while page <= self.require_pages:
            dUrl = self.base_url + "?term=%s&page=%d" %(self.keyword, page)
            self.driver.get(dUrl)
            elem_url = self.driver.find_elements_by_class_name("docsum-title")
            for url in elem_url:
                title = url.text
                url_content = url.get_attribute("href")
                self.get_detail(title, url_content)
                if self.count == 10:
                    break
            if self.count == 10:
                break
            time.sleep(1)
            page += 1

    def get_detail(self, title, url_content):
        print(url_content)
        self.count += 1
        # filename = self.save_path + "\\%d.txt" % self.count
        # if self.count % 10 == 1:
        #     self.records.append([])

        self.driver2.get(url_content)
        try:
            paper_title = self.driver2.find_element_by_class_name("heading-title").text
        except:
            paper_title = ""
        try:
            authors_list = self.driver2.find_element_by_class_name("authors-list").text
        except:
            authors_list = ""
        try:
            but = self.driver2.find_element_by_id("toggle-authors").click()
            affiliations = self.driver2.find_element_by_class_name("affiliations").text
        except:
            affiliations = ""
        try:
            expanded_authors = self.driver2.find_element_by_class_name("expanded-authors").text
        except:
            expanded_authors = ""
        try:
            PMID = self.driver2.find_element_by_class_name("current-id").text
        except:
            PMID = ""
        try:
            DOI = self.driver2.find_elements_by_class_name("doi")[0]
            DOI_text = DOI.text
        except:
            DOI_text = ""
        try:
            DOI_href = DOI.get_attribute("href")
        except:
            DOI_href = ""
        try:
            Abstract = self.driver2.find_element_by_class_name("abstract-content").text
        except:
            Abstract = ""
        DOI_text = "https://doi.org/" + DOI_text[4:]
        DOI_text = DOI_text.replace(' ', '')
        self.records.append([int(PMID), self.keyword, paper_title, authors_list, affiliations, DOI_text, Abstract, url_content])
        print(str(self.count) + ": " + paper_title)
        print([int(PMID), paper_title, authors_list, affiliations, expanded_authors, DOI_text, Abstract, url_content])


    def rep(self):
        return self.records


# if __name__ == '__main__':
#     keyword = "cancer"
#
#     Spider = CatchMed(keyword)
#     Spider.get_URL()

