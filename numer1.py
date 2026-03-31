#점수 
score = 85 
# 출석률
attendance = 93 
# 나이
age = 17 
# 보호자 
guardian = True
# vip 
is_vip = False
# 참석자
is_member = True 

# 점수가 80 이상이고 출석률이 90 초과인 식 
print(score) 
score >= 80 and attendance > 90
# 점수가 70 이상이고 출석률이 80 이상인 식
score >= 70 and attendance >= 80 
# 나이가 20 이상이거나 보호자가 있는 식 
age >= 20 or guardian 
# 나이가 19세 미만이거나 vip인 식 
age < 19 or is_vip 
# vip가 아닌 식
not is_vip 
# 회원이고 vip인 식
is_member and is_vip 
# 회원이 아니거나 나이가 20 이상인 식 
(not is_member) or age >= 20 
# 점수가 90 이상이거나 출석률이 95 이상인 식 
score >= 90 or attendance >= 95 