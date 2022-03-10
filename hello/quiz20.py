import random
import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('---legacy---')
        a=[]
        for i in range(5):
            a.append(i)
        print(a)

        print('---comprehension---')
        a2=[i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')#html.parser vs lxml
        dict = {}
        # print(soup.prettify())
        artist = soup.find_all('p',{'class':'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        #artists = [i.get_text() for i in artists]
        #print(type(artists))

        #title = soup.find_all('p', {'class': 'title'})
        #title = [i.get_text() for i in title]
       # print(''.join(i for i in title))

        # print(''.join(i for i in artists))
        #print(''.join(i for i in artists))
        ls=[]
        '''
        for i,j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(i for i in [i for i in self.reuse(soup,j)]))
        '''


        # a = [i for i in [soup, 'title']]
        # a = [i for i in [soup, 'artist']]
        # print(soup.prettify())
        return None
    
    def reuse_rank(self,soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.reuse(soup, j)):
                print(f'{i}위 : {j}')
            print('#'*100)


    @staticmethod
    def reuse(soup,cls_nm) -> []:
            ls = soup.find_all('p', {'class': cls_nm})
            return [i.get_text() for i in ls]
            # print(''.join(i for i in titles))



    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent':'Mozilla/5.0'}
        url='https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req= urllib.request.Request(url,headers=headers)
        soup = BeautifulSoup(urlopen(req).read(),'lxml')  # html.parser vs lxml
        artists = soup.find_all('span',{'class':'checkEllipsis'})
        artists = [i.get_text() for i in artists]
        #print(artists)
        title = soup.find_all('div',{'class':'ellipsis rank01'})
        title =[i.get_text() for i in title]
        print(''.join(i for i in title))
        #print(soup)
        #print('\n'.join(i for i in artists))
        return None

    def quiz28(self) -> str: return None


    def quiz29(self) -> str: return None





