import sys

sys.stdin = open("_암호문1.txt")

T = 10

for t in range(1, T+1):
    origin_list = int(input())
    origin_list = list(map(int,input().split()))

    command_len = int(input())
    command_list = input().split()

    #i의 초기화
    i = 0

    #while문 (반복문)
    while i < len(command_list):
        command = command_list[i]
        if command == 'I':
            #x,y 숫자리스트 s 구해야한다.
            x = int(command_list[i+1])
            y = int(command_list[i+2])
            number_list = command_list[i+3:i+3+y]

            #insert 메서드를 써서 x의 위치에 숫자들을 삽입한다.
            #역순으로 삽입한다.
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))
        i = i + 1
    print(f'#{t} ',*origin_list[:10])