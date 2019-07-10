import requests
class FailToGetHTML(Exception):
    """ Falied To Get HTML """
    pass
class News:
    html = None
    status = None
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    def __init__(self,link):
        self.link = link 
    def crawl(self):       
        try :
            req = requests.get(self.link,headers=self.headers)
            self.status = req.status_code
            if req.ok: 
                self.html = req.text
            else:
                raise FailToGetHTML("[FailToGetHTML] Failed To Get HTML")
        except FailToGetHTML as e:
           print(e,'stauts code is ',self.status) 
        except Exception as e:
            print('[DEBUG] crawl error',e)
            self.html = None 

class SecurityNews(News):
    pass

class ElectNews(News):
    pass

class EstSecurity(News):
    pass
class AhnLab(News):
    pass
