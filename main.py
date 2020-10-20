print ("""Commands:
 /s - sell
 /u - upgrade
 /m - money
 /l - level
 /stop - stop""")
money = 0
exp = 0
starypickaxelevel = 1
pickaxelevel = 1
command = 0
random = 0
level = exp / 1000
while command != "/stop":
    command = input("> ")
    if command == "/s":
        import random
        import time
        random = random.randrange(1, 50, 1)
        print ("Earning money...")
        time.sleep(15)
        print ("Your salary is:", round(pickaxelevel / 10 * random + random))
        exp = random / 2 + exp
        level = exp / 1000
        money = money + pickaxelevel / 10 * random + random
    if command == "/m":
        print ("Your balance is:", money,"$")
    if command == "/l":
        level = exp / 1000
        print ("Level:", round(level))
        print ("Expierience points:", round(exp))
        print ("Pickaxe level:", pickaxelevel)
    if command == "/u":
        if money > 9:
            money = money - 10
            pickaxelevel = pickaxelevel + 1
            print ("Pickaxe upgraded! (10$)", pickaxelevel - 1, ">>>", pickaxelevel)
        else:
            print ("Upgrade costs 10$! You only have:", round(money), "$!")