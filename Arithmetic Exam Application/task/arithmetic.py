import random
count = []
inp1 = 0
inp2 = 0

def start_play():
    while True:
        global inp1
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
        inp1 = input()
        if (inp1 == '1' or inp1 == '2') and inp1.isdigit():
            int(inp1)
            check_what_level()
            break
        else:
            print("Incorrect format.")


def check_what_level():
    global inp1
    if inp1 == '1':
        level2()
    else:
        level1()


def level1():
    global inp2
    global count
    while len(count) != 5:
        expression = f"{random.randint(11, 29)}"
        def one():
            while True:
                print(expression)
                inp2 = input()
                if inp2.isdigit():
                    res = "Right!" if int(inp2) == int(expression) ** 2 else "Wrong!"
                    print(res)
                    count.append(res)
                    break
                else:
                    print("Wrong format! Try again.")
                    continue

        one()
    final_step()


def level2():
    global inp2
    global count
    while len(count) != 5:
        expression = f"{random.randint(2, 9)} {random.choice(['+', '-', '*'])} {random.randint(2, 9)}"
        def two():
            while True:
                print(expression)
                try:
                    inp2 = int(input())
                    res = "Right!" if inp2 == eval(expression) else "Wrong!"
                    print(res)
                    count.append(res)
                    break
                except Exception:
                    print("Wrong format! Try again.")
                    continue
        two()
    final_step()


def final_step():
    global count
    global inp1
    name_level = "simple operations with numbers 2-9" if inp1 == 2 else "integral squares of 11-29"
    print(f"Your mark is {count.count('Right!')}/5. Would you like to save the result? Enter yes or no.")
    if input() in ['yes', 'YES', 'y', 'Yes']:
        name = input("What is your name?")
        file = open("results.txt", 'a')
        file.write(f"{name}: {count.count('Right!')}/5 in level {inp1} {name_level}")
        file.close()
        print('The results are saved in "results.txt"')

start_play()




























