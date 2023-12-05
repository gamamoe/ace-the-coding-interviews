# 파이썬 내장 이진법 함수를 이용한 것
def solution1(decimal):
    return bin(decimal)[2:]

def solution(decimal): #책의 풀이
    stack = [] #스택통
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder)) #2로 나눈 나머지 push
        decimal //= 2 #계속해서 몫을 decimal로 정의
    stack.reverse() #거꾸로 읽어야하므로 뒤집는다.
    return ''.join(stack) #문자열로 출력
#이 경우 pop으로 하나하나 문자열을 더하기보다는
#join이 pop보다 시간복잡도가 효율적이므로 join을 사용한다


d1 = 10
d2 = 27
d3 = 12345

print(solution(d1)) # 1010
print(solution(d2)) # 11011
assert solution(d3) == '11000000111001', '출력값3 에러'