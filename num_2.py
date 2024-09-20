# START
name_of_athlete: str = ""
jump_height: float = 0
account: int = 0
jump_record: float = 6.23
max_jump: float = 0
avg_result: float = 0
sum_jump: float = 0
for i in range(7):
    jump_height: float = float(input("Enter the jump height of the athletes from seven countries:"))
    if jump_height < 5.80:
        continue
    else:
        account += 1
        sum_jump =+ jump_height
        if jump_height > jump_record:
            max_jump = jump_height
            name_of_athlete = input("Enter the name of the athlete who made this score:")
print(f" the number of the good result: {account}")
avg_result = sum_jump // account
print(f"The average of the good results: {avg_result}")
print(f"The highest result: {max_jump}")
if max_jump > jump_record:
    print(f"the max jump in world is :{name_of_athlete}")
    print(f"the name of athlete who did it is: {max_jump}")
else:
    print("None")
# END
