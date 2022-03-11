import random
import urllib
from hello.domains import myRandom, memberlist
from quiz00 import Quiz00
import random

from bs4 import BeautifulSoup
from urllib.request import urlopen
import  pandas as pd


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

    def quiz24zip(self,ls1,ls2) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')#html.parser vs lxml
        ls1 = self.reuse(soup, 'title')
        ls2 = self.reuse(soup, 'artist')
        '''
        a = [ i if i ==0 or i ==0 else i for in range(1)]
        b =  [i if i ==0 or i ==0 else i for i in[]]
        c = [(i,j) for i, j in enumerate([])]
        dt = {i: j for i, j in zip(ls1, ls2)}
        l = i + j for i, j in zip(ls1,ls2)]
        l2 = list(zip(ls1,ls2))
        di = dict(zip(ls1,ls2))
        print(dt)
        '''

        #self.dict1(ls1, ls2)
        #self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)

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

        '''
        for i,j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(i for i in [i for i in self.reuse(soup,j)]))
        '''
        # a = [i for i in [soup, 'title']]
        # a = [i for i in [soup,
        # 'artist']]
        # print(soup.prettify())



    @staticmethod
    def dict3(ls1,ls2):
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
            print(dict)
        return dict


    @staticmethod
    def dict2(ls1,ls2):
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1,ls2) -> None:
        dict = {}
        for i in range(len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)


    def reuse_rank(self,soup)-> None:
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.reuse(soup, j)):
                print(f'{i}위 : {j}')
            print('#'*100)


    @staticmethod
    def reuse(soup,cls_nm) -> []:
            ls = soup.find_all('p', {'class': cls_nm})
            return [i.get_text() for i in ls]
            # print(''.join(i for i in titles))


    @staticmethod
    def quiz25dictcom()-> str:
        a = Quiz00
        #1명인데 5명 추출 0~100사이 랜덤
        b = set([a.quiz06memberChoice() for i in range(5)])
        print(b)
        while len(b) !=5:
            b.add(a.quiz06memberChoice())

        scores = [myRandom(0,101)for i in range(5)]
        students = list(b)
        aa={i : j for i , j in zip (students,scores)}

        print(aa)




    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
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


        mls1 = self.reuse(soup, 'title')
        mls2 = self.reuse(soup, 'artist')

        mdict = {}
        for i, j in zip(mls1, mls2):
            mdict[i] = j
            print(mdict)
        return mdict

    @staticmethod
    def mdict(mls1,mls2):
        mdict = {}
        for i, j in enumerate(mls1):
            mdict[j] = mls2[i]
        print(mdict)



    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict,orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep =',', na_rep ='NaN')
    '''
    다음 결과 출력
        a   b   c
     1  1   3   5
     2  2   4   6
     
    '''


    def quiz29_pandas_(self) -> object:
        d1 = {'a': [1, 2]
            , 'b': [3, 4],
              'c': [5, 6]}
        d = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d, index=[1, 2])
        d2 = {"1": [1, 3, 5], "2": [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2, orient='index', columns=['a', 'b', 'c'])
        d3 = {"1": [1, 3, 5]}
        d4 = {"2": [2, 4, 6]}


        x = []
        y = []
        [x.append(i) if i % 2 == 0 else y.append(i) for i in range(1, 7)]
        f = [y,x]
        ind = ["1","2"]
        dic = {i:j for i,j in zip(ind,f)}

        columns = [chr(i) for i in range(97,100)]
        df3 = pd.DataFrame.from_dict(dic, orient='index',columns=columns)

        print(df3)

        #frame = pd.DataFrame(d1, index=[1,2])
        #print(frame)


        return None
