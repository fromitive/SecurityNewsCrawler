from News import *

class CrawlMachine:
    dock = []
    def addDock(self,CrawlObject):
        self.dock.append(CrawlObject)
        print('add',CrawlObject)   
    def launch(self):
        for CrawlObject in self.dock:
            print("[INFO] CrawlStart :",CrawlObject)
            CrawlObject.crawl() 

crawl = CrawlMachine()
crawl.addDock(SecurityNewsWeek())
crawl.addDock(SecurityNews())

crawl.addDock(ElectNews('http://www.etnews.com/news/section.html?id1=11'))
crawl.addDock(ElectNews('http://www.etnews.com/news/section.html?id1=04&id2=045'))

crawl.addDock(EstSecurity('https://blog.alyac.co.kr/category/국내외%20보안동향'))
crawl.addDock(EstSecurity('https://blog.alyac.co.kr/category/악성코드%20분석%20리포트'))

crawl.addDock(AhnLab('https://www.ahnlab.com/kr/site/securityinfo/secunews/secuNewsList.do?curPage=1&menu_dist=1&seq=&key=&dir_group_dist=&dir_code=&searchDate='))





