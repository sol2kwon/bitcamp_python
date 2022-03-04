from hello.ex import myRandom
import random
import math

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
        pass


    def quiz05grade(self):
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
            print(f'국어:{kor} 영어:{eng} 수학:{math} 합격여부:{res}')

    def quiz06memberChoice(self):
        def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
            self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                            "권혜민", "서성민", "조현국", "김한슬", "김진영",
                            '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                            '최민서', '한성수', '김윤섭', '김승현',
                            "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def quiz07lotto(self):
            pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
            pass

    def quiz09gugudan(self):  # 책받침구구단
            pass





def myRandom(start,end):
    return random.randint(start,end)