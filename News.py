import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
class FailToGetHTML(Exception):
    """ Falied To Get HTML """
    pass
class News:
    html = None
    status = None
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    soup = None
    url = None 
    def __init__(self,link):
        self.link = link 
        self.url = urlparse(self.link)
    def crawl(self):       
        try :
            req = requests.get(self.link,headers=self.headers)
            self.status = req.status_code
            if req.ok: 
                self.html = req.text
                self.soup = BeautifulSoup(self.html,'html.parser')
            else:
                raise FailToGetHTML("[FailToGetHTML] Failed To Get HTML")
        except FailToGetHTML as e:
           print(e,'stauts code is ',self.status) 
        except Exception as e:
            print('[DEBUG] crawl error',e)
            self.html = None 

class SecurityNewsWeek(News):
    articles = []
    def __init__(self,link):
        super().__init__(link)

    def crawl(self):
        super().crawl()
        news_list = self.soup.findAll("div",class_="news_list")
        for news in news_list:
            article = {}
            news_date = news.find("span",class_="news_writer").text.split('|')[1].strip()
            recent = datetime.strptime(news_date,"%Y.%m.%d %H:%M")

            #crawl news
            aTag = news.findAll('a')
            article.update({"news_title":aTag[0].find("span",class_="news_txt").text}) 
            article.update({"news_preview":aTag[1].text})
            article.update({"news_link":self.url.scheme+"://"+self.url.netloc+aTag[1].attrs['href']})
            news_date = news.find("span",class_="news_writer").text.split('|')[1].strip()
            article.update({"news_date":recent})

            #update news
            self.articles.append(article)        

class SecurityNews(News):
    articles = []
    def crawl(self):
        super().crawl()
        main_news_links = self.soup.findAll("div",class_="news_main_title")  
        for main_link in main_news_links:
            link = self.url.scheme+"://"+self.url.netloc+main_link.find("a").attrs['href']
            print("[SECURITY NEWS TODAY] request link :",link)
            req = requests.get(link,headers=self.headers)
            html = req.text 
            soup = BeautifulSoup(html,'html.parser')
            article = {}

            news_date = soup.select("#news_util01")[0].text
            news_date = news_date[news_date.find(":")+1:].strip()
            time = datetime.strptime(news_date,"%Y-%m-%d %H:%M")
            article.update({"news_link":link})
            article.update({"news_date":time})
            article.update({"news_title":soup.select("#news_title02")[0].text})  
            article.update({"news_preview":soup.select("#news_content > b:nth-child(1)")[0].text})
            self.articles.append(article)
                

        news_title = self.soup.select('.news_txt')
        news_content = self.soup.select('.news_content')
        news_date = self. soup.select('.news_writer')
        for title,content,date in zip(news_title,news_content,news_date):
            article={}
            link = self.url.scheme+"://"+self.url.netloc+content.attrs['href']
            article.update({'news_link':link})
            article.update({'news_preview':content.text})
            article.update({'news_title':title.text})
            str_date = date.text.split("|")[1].strip()
            time = datetime.strptime(str_date,"%Y.%m.%d %H:%M")
            article.update({'news_date':time})
            self.articles.append(article)
            
    def getTodayArticle(self):
        articles = []
        now = datetime.now()
        for article in self.articles:
            term = now - article['news_date']
            if term.days == 0 : #today  
                articles.append(article) 
        return articles 

class ElectNews(News):
    pass

class EstSecurity(News):
    pass
class AhnLab(News):
    pass
