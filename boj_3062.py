# import random
# rep = int(input())
# for _ in range(rep):
#  rand_num = random.randrange(10,100001)
#  num = str(rand_num)
#  num_rev = int(num[::-1])
#  num1 = int(num)
#  num2 = num1 + num_rev
#  num2_rev = int(str(num2)[::-1])
#  if num2 == num2_rev:
#      print("Yes")
#  else:    print("No")

rep = int(input())
for _ in range(rep):
    num = input()
    num_rev = int(num[::-1])
    num1 = int(num)
    num2 = num1 + num_rev
    num2_rev = int(str(num2)[::-1])
    if num2 == num2_rev:
        print("YES")
    else:    print("NO")