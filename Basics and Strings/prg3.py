def arm_num(n):
    num = n
    sum = 0
    while num > 0:
        temp = num % 10
        sum += temp ** 3
        num  //= 10
    if sum == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

number = int(input("Enter a Number :"))
arm_num(number)