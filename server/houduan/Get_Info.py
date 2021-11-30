from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def Gene_cards():
    url = "https://www.genecards.org/Guide/Sources"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    res = []
    oths = [17, 53, 99, 105, 116, 141, 146, 157]
    for i in range(1, 180):
        iid = i
        # print(i, "begin----")
        if i not in oths:
            dbname = driver.find_element_by_xpath("//*[@id='mobile-padding-wrapper']/div/ol/li[%d]/a" % i).text
            try:
                db_url = driver.find_element_by_xpath("//*[@id='mobile-padding-wrapper']/div/ol/li[%d]/a" % i).get_attribute("href")
            except:
                db_url = ''
        else:
            no = oths.index(i)
            dbname = driver.find_element_by_xpath("//*[@id='mobile-padding-wrapper']/div/ol/li[%d]/span[1]" % i).text
            db_url = ''
        try:
            introduction = driver.find_element_by_xpath("//*[@id='mobile-padding-wrapper']/div/ol/li[%d]/span" % i).text
        except:
            introduction = ''
        dicts = {'ID': iid, 'DBName': dbname,  'DBUrl': db_url, 'Introduction': introduction, 'category': 'empty'}
        res.append(dicts)
        # print(dicts)
        # print(dbname, " get----")

    return res


# if __name__ == '__main__':
#     res = Gene_cards()
#     print(res)
