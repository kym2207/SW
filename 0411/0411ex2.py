'''2023.04.11
김유민
선택문 if-elif-else
성적이 90이상이면 A학점,성적이 90미만이면 B학점
성적이 80이상이면 C학점,성적이 70미만상이면 F학점
'''
score=int(input("성적 입력:"))

if score>=90:
    print("A학점")
elif score>=80:
    print("B학점")
elif score>=70:
    print("C학점")
else:
    print("F학점")