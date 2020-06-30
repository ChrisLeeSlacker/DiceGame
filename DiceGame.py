from random import randint

rounds = 10 ** 5
# Max row width
width = 70
# Create list with 13 zero slots
list = 13 * [0]

for i in range(rounds):
    dice = randint(1, 6) + randint(1, 6)
    # Fill the empty slots
    list[dice] += 1
    
ratio = max(list) / width
print(' Statistics:')
for num in range(2,13):
    if num < 10: print(' ', end = '')
    print(num, int(list[num]/ratio) * '=' + '[' + str(list[num]) + ']')
