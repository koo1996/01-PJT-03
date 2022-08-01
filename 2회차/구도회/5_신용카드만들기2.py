import sys

sys.stdin = open("_신용카드만들기2.txt")


for i in range(1,int(input())+1):
    N = input()
    N = N.replace('-','') #'-' 제거
    if N[0] == '3' or N[0] == '4' or N[0] == '5' or N[0] == '6' or N[0] == '9':
        #3,4,5,6,9 유무
        if len(N) == 16: #길이 16인가?
            print('#{} {}'.format(i,'1')) 
        else:
            print('#{} {}'.format(i,'0'))
            
    else: 
        print('#{} {}'.format(i,'0'))