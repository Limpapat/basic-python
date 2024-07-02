#print loop

for i in range(10):
    print("i =",i)
    if i == 5:
        print("i = 5")
        break
    if i == 3:
        print("i = 3")
        continue
    print("i =",i)
    print("Hello world")
