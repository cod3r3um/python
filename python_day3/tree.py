line = int(input("Tree의 높이를 입력하세요. (5~30) > "))

for x in range(1, line+1):
    print((" "*(line-x)) + ("*" * (x*2-1)))

for y in range(1, 4):
    print(" " * (line-2) + "***")

# for i in range(0,tree) :
#      print(" " * (tree-i) , end=" ")
#      print("*" * (i*2+1))
# for i in range(0,3):
#     print(" " * (tree - 1), end=" ")
#     print("*" * 3 )