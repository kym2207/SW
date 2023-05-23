'''
2023-05-23
김유민
#문제정의  
    stu.txt 파일을 읽어서 각 학생의 평균 성적 계산해서 출력하기
#문제분석
    변수-한줄씩 읽어서 저장(score),리스트자료로 변환(scorelist)
        리스트에서 이름 항목 저장(name),합계(sum)
#알고리즘
    1.파일 열기(쓰기)
    2.파일 처리
        2.1 (반복)whlie True;
                    한 줄 읽어서 score저장
                    (선택)if score==' ':
                        break
                    읽어온 내용을 리스트로 변환해서 scorelist저장
                    scorelist에서 첫번째 항목(이름)을 name변수에 저장
                    (반복)for i in range(1,4):
                        scorelist의 1,2,3항목의 값을 sum에 더하기
    3.파일 닫기

'''
f=open("C:/data/stu.txt","r")#쓰기모드 파일 객체 생성
while True:
    score=f.readline()#한 줄식 읽어 오기
    if score=='':
        break

    scorelist=score.split()#리스트 자료로 변환
    name=scorelist[0] #리스트 첫번째 항목은 이름
    sum=0 #합계
    for i in range(1,4):
        sum+=int(scorelist[i]) #3과목 성적의 합계
    print(name,"의 편균 성적은:%.2f"%(sum/3))
f.close()#파일 닫기