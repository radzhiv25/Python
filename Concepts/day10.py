#break
for i in range(1,12):
    if(i == 11):
        print("Loop broke")
        break
    print("5 times", i, "=", 5*(i))

#continue
x = 10
while(x > 0):
    print("2 times", x, "=", 2*x)
    x = x - 1
    if(x==5):
        print("Iteration Skipped")
        continue