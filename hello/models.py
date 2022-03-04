import random
import math



class Quiz01Calculator:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        self.add()
        self.sub()

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        pass

class Quiz02Bmi:
    @staticmethod
    def getBmi(member):
        this = member
        bmires =this.weight/(this.height*this.height)*10000
        if bmires > 25:
            return '비만'
        elif bmires > 23:
            return '과체중'
        elif bmires > 18.5:
            return '정상'
        else:
            return '저체중'


class Quiz03Grade(object):
    def __init__(self, name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def sum(self):
        return self.kor+self.eng+self.math
    def avg(self):
        return (self.sum()) /3
    def pa(self):
        if (self.avg()) >= 60:
            return '합격'
        else:
            return '불합격'

class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math
    def avg(self):
        return self.kor + self.eng + self.math / 3
    def getGrade(self):
        pass
    def chkPass(self): # 60점이상이면 합격
        pass


def myRandom(start,end):
    return random.randint(start,end)

class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1,6)



class Quiz06RandomGenerator:
    def __init__(self, start, end):  # 원하는 범위의 정수에서 랜덤값 1개 추출
        self.start = start
        self.end = end

    def random(self):
        return myRandom(self.start,self.end)

class Quiz07RandomChoice:
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        return self.members[myRandom(0,23)]

class Quiz08Rps(object):
    def __init__(self,player):
        self.player = player
        # 1가위 2바위 3보
        self.computer = myRandom(0,2)


    def game(self):
        rps = ['가위', '바위', '보']
        c = self.computer
        p = self.player
        r = p-c

        if r == 0:
            res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 무승부'
        elif r == -1 or r == 2:
            res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 패배'
        elif r == 1 or r == -2:
            res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 승리'
        return res


class Quiz09GetPrime:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2



    def prime(self):
        num1 = self.num1
        num2 = self.num2
        res =''
        for i in range(num1,num2+1):
            c = 0
            for k in range(1 ,i+1):
                if i % k == 0:
                    c += 1
            if c <= 2:
                res += f'{i} \t'
        return res







class Quiz10LeapYear(object):
    def __init__(self):
        pass
class Quiz11NumberGolf(object):
    def __init__(self):
        pass
class Quiz12Lotto(object):
    def __init__(self):
        pass
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass



