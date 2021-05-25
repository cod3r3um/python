# 삼각형 출력하기

'''
#
##
###
####
#####
'''

# range(e) 0 ~ e-1
# range(s, e) s ~ e-1
# range(s, e, step) s ~ e-1

cnt = 10

for i in range(5):
    print("#"*i)

print()

for i in range(1,5):
    print("#"*i)

print()

for i in range(1,10,2):
    print("#"*i)

print()

for i in range(9,0,-2):
    print("#"*i)

print()

for i in range(1,10,2):
    print(" "*(10-i), end="")
    print("#"*i)

print()

for i in range(0,cnt):
    print(" "*(cnt-i), end="")
    print("*" *(i*2+1))

for i in range(0,cnt-1):
    print(" "*(i+2),end="")
    print("*"*((cnt-i-1)*2-1))