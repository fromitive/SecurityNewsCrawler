from News import *

class CrawlMachine:
    def __init__(self):
        self.dock = []
        self.today_articles = []
    def addDock(self,CrawlObject):
        self.dock.append(CrawlObject)
        print('add',CrawlObject)   
    def launch(self,today=True):
        for CrawlObject in self.dock:
            print("[INFO] CrawlStart :",CrawlObject)
            CrawlObject.crawl()
            if today:
                articles = CrawlObject.getTodayArticle()
                self.today_articles.extend(articles)
        if today:
            return self.today_articles

crawl = CrawlMachine()
crawl.addDock(SecurityNewsWeek())
crawl.addDock(SecurityNews())

crawl.addDock(ElectNews('http://www.etnews.com/news/section.html?id1=11'))
crawl.addDock(ElectNews('http://www.etnews.com/news/section.html?id1=04&id2=045'))

crawl.addDock(EstSecurity('https://blog.alyac.co.kr/category/국내외%20보안동향'))
crawl.addDock(EstSecurity('https://blog.alyac.co.kr/category/악성코드%20분석%20리포트'))
