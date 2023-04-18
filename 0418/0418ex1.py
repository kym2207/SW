'''
2023-04-18
김유민
성적처리 프로그램
입력받은 성적이 90이상이면 'A',90이상이면 'A',80이상 90미만이면 'B',70이상 80미만이면 'C',70이하이면 'F'
'''

jumsu=int(input("성적 입력:"))

if jumsu >=70:
    if jumsu >=80:
        if jumsu >=90:
            print("A학점입니다.")
        else :
            print("B학점입니다.")
    else :
        print("C학점입니다.")
else :
    print("F학점입니다.")