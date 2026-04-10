# 가격을 입력받는다 
price = int(input("가격 입력: "))
# 회원 여부(1: 회원, 0: 비회원)를 입력받는다 
is_member = int(input("회원 여부 (1: 회원, 0: 비회원): ")) 

# 회원이면 20% 할인을 출력하고, 비회원이면 5% 할인된 가격을 출력하라 
discount_ratio = 0.2 if is_member == 1 else 0.05
price = price * (1 - discount_ratio)

print(price)


