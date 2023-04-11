su1=int(input('수 입력'))
op=input('연산자 입력')
su2=int(input('수 입력'))

if op=='+':
    print('값:',su1+su2)
elif op=='-':
    print('값:',su1-su2)
elif op=='*':
    print('값:',su1*su2)
else:
    print('값:',su1/su2)
