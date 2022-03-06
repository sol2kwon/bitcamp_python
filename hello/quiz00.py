from hello.domains import myRandom,memberlist
import random


class Quiz00:
    def quiz00calculator(self):
        a = myRandom(1,100)
        b = myRandom(1,100)
        o = ['*','-','*','/','%']
        o2 = o[myRandom(0,5)]
        if o2 == '+':
            s = f'{a}+{b}={a+b}'
        elif o2 == '-':
            s = f'{a}-{b}={a-b}'
        elif o2 == '*':
            s = f'{a}*{b}={a*b}'
        elif o2 == '/':
            s = f'{a}/{b}={a/b}'
        elif o2 == '%':
            s = f'{a}%{b}={a/b}'
        print(s)
        return None

    def quiz01bmi(self):
        h = myRandom(50,200)
        w = myRandom(1,200)
        bmires = w / (h * h) * 10000

        if bmires > 25:
            res = '비만'
        elif bmires > 23:
            res = '과체중'
        elif bmires > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{bmires} {res}')

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        p = myRandom(0,2)
        c = myRandom(0,2)
        rps = ['가위', '바위', '보']
        r = p-c
        if r == 0:
                res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 무승부'
        elif r == -1 or r == 2:
                res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 패배'
        elif r == 1 or r == -2:
                res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 승리'
        print(f'{res}')

    def quiz04leap(self):
        year = myRandom(1000,5000)
        if(year % 4 == 0 and year % 100!= 0)or(year % 400 ==0):
           res = "윤년"
        else :
            res = "평년"
        print(f"{year}년도는 {res}입니다.")



    def quiz05grade(self):
            name = memberlist()
            kor = myRandom(90, 100)
            eng = myRandom(50, 100)
            math = myRandom(50, 100)
            sum = kor+eng+math
            avg = int(sum/3)
            grade = ['A', 'B', 'C', 'D', 'E', 'F']
            if avg == 100:
                g_index = 0
            elif avg<100 and avg>40:
                g_index = int((99-avg)/10)
            else:
                g_index = 5

            print(f'{avg} {grade[g_index]}')

            if avg >= 60:
                res = '합격'
            else:
                res = '불합격'
            print(f'{name}님의 점수 → 국어:{kor} 영어:{eng} 수학:{math} 합격여부:{res}')
            ## 하나로 출력하는거 고민해 보기

    def quiz06memberChoice(self):
            print(memberlist())

#1. 1~45번 중 6개를 중복없이 뽑아야 한다.
#2. 6개를 뽑고 보너스 번호를 하나 더 뽑는다.
#3. 처음 뽑은 번호 6개가 일치하면 1등
    def quiz07lotto(self):
        lottonum = random.sample(range(46),7)
        mynum = random.sample(range(46),6)
        res = ""
        a=[1,2,3,8,9,10,7]
        b=[2,3,1,8,9,7]


        c = 0
        for i in a[0:6]:
            for k in b[0:6]:
                if i==k:
                    c += 1
                


        if c == 6:
            res = f'일등 {c} \t'
        elif c == 5 :
            for a[6] in b[0:6]:
                res = f'이등 {c} \t'
        elif c == 5:
            res = f'삼등 {c} \t'
        elif c ==4:
            res = f'사등 {c} \t'
        elif c == 3:
            res = f'오등 {c} \t'

        print(res)









    def quiz08bank(self):  # 이름, 입금, 출금만 구현
            pass

    def quiz09gugudan(self):  # 책받침구구단
            pass





