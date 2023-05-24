'''
2023-05-24
김유민
#문제분석
    난수를 발생시켜 num.txt 파일을 만들고, 이 파일을 이용해서 각 학생의 평균을 구한다음 avg.txt파일에 저장 하기
'''
import random #난수 모듈 추가
with open("c:/data/num.txt","w") as f: #파일 객체 생성
    for i in range(5):#줄 반복
        for j in range(5): #랜덤 수 찍기 반복
            f.write(str(random.randint(1,100)))#랜덤 수 파일에 쓰기
            f.write(' ') #숫자 다음 공백 찍기
        f.write("\n") #줄 바꿈

with open("c:/data/num.txt","r") as f1: #읽기 파일 객체
    with open("c:/data/avg.txt","w") as f2: #쓰기 파일 객체
        l=1
        while True:
            score=f1.readline() #num.txt 한줄 읽어 오기
            if score=='': #내용이 없으면
                break
            scorelist=score.split() #읽어 온 한 줄을 공백 기준 리스트로 변환
            sum=0 #합계
            for i in range(5): #한 학생당 5과목의 점수 더하기
                sum+=int(scorelist[i])
            print(l,"번 학생의 평균:",sum/5,file=f2)#결과 파일에 저장
            l+=1