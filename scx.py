# 국어 점수를 입력 받으시오
korean = int(input("국어 점수를 입력해: ")) 
# 영어 점수를 입력 받으시오
english = int(input("영어 점수를 입력해: ")) 
# 수학 점수를 입력 받으시오
math = int(input("수학 점수를 입력해: "))

# 국어를 선언하시오. 
sub1 = "국어"
# 영어를 선언하시오.
sub2 = "영어"
# 수학을 선언하시오.
sub3 = "수학"
# 총점을 0으로 초기화 하시오.
total = 0 
# +=를 사용하여 총점을 계산하시오
# 국어의 총점을 입력하시오.  
total += korean
# 영어의 총점을 입력하시오.
total += english
# 수학의 총점을 입력하시오.
total += math

# 평균을 구하는 식을 쓰시오

average = total / 3 

# 과목명을 출력하시오(국어, 영어, 수학) 

print("과목:", sub1, sub2, sub3) 

# 각점수를 출력하시오 

#국어 점수 
print(sub1 + ":", korean)

#영어 점수 
print(sub2 + ":", english)

#수학 점수 
print(sub3 + ":", math) 

# 총점을 출력하시오
print("총점: ", total) 
# 평균을 출력하시오
print("평균: ", average) 



