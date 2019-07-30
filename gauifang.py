list = [1, 4, 6, 8, 9, 10, 14, 15]
a = int(input("a is "))
# a = input("a is ")
print(type(a))

middle = list[int(len(list) // 2)]
if a == middle:
    print('a de xiabiao is :', int(len(list) // 2))

elif a > middle:
    for i in range(int(len(list) // 2) + 1, len(list)):
        if a == list[i]:
            print('a de xiaobaio is :', i)
            break

else:
    for i in range(int(len(list) / 2)):
        if a == list[i]:
            print('a de xiabiao is :', i)
            break