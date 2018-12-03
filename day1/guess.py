#Author: Jenliver

# age = 60
# for i in range(3):
#     guess_age = int(input("guess age:"))
#     if guess_age == age:
#         print("ok")
#         break
#     elif guess_age < age:
#         print("small")
#     else:
#         print("big")

age = 60
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age:
        print("ok")
        break
    elif guess_age < age:
        print("small")
    else:
        print("big")

    count += 1
    if count == 3:
        continue_confie = input("do you want to keep again? y/n:")
        if continue_confie == 'n':
            break
        else:
            count = 1
#else:
#    print('you have tried many times ....fuck off')