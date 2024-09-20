# START
positive: int = 0
negative: int = 0
zero: int = 0
divisible_by_7: int = 0
list_of_positive = []
list_of_negative = []
last_positive = None
last_negative = None
for i in range(10):
    num: int = int(input("enter a number:"))
    if 1000 < num or num < - 1000:
        continue
    if num == -999:
        break
    if num > 0:
        positive += 1
        if num % 7 == 0:
            divisible_by_7 += 1
        list_of_positive.append(num)
    elif num < 0:
        negative += 1
        if num % 7 == 0:
            divisible_by_7 += 1
        list_of_negative.append(num)
    else:
        zero += 1
if positive > 0:
    last_positive = list_of_positive[-1]
    print(f"The last positive number entered is:{last_positive}")
else:
    print(None)
if negative > 0:
    last_negative = list_of_negative[-1]
    print(f"The last negative number entered is:{last_negative}")
else:
    print(None)
print(f"The amount of positive numbers received: {positive}")
print(f"The amount of negative numbers received: {negative}")
print(f"The amount of zero numbers received: {zero}")
print(f"The amount of divisible_by_7 numbers received: {divisible_by_7}")
# END
