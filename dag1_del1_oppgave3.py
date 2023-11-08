import random
#random.seed(1)
def dice_throw(d: int = 6, number_of_throws: int = 1) -> list:
    res = list()
    for i in range(number_of_throws+1):
        res.append(random.randrange(1,d+1))
    return res

def first():
    print("Lag et program som ruller en terning 12 ganger.")
    res = list()
    for i in range(12):
        res.append(dice_throw(6))
    print(res)

def second():
    print("Lag et program som ruller en 12-sidet terning 6 ganger.")
    res = list()
    for i in range(6):
        res.append(dice_throw(12))
    print(res)


def third():
    print("Lag et program som ruller to terninger 6 ganger.")
    res = list()
    for i in range(6):
        d1 = random.randrange(1,7)
        d2 = random.randrange(1,7)
        res.append(f"Dice1: {d1}, dice2: {d2}, sum: {d1 + d2}")
    print(res)

if __name__ == "__main__":
    # first()
    # second()
    # third()
    print(dice_throw(6, 12))
    print(dice_throw(12, 6))
    third()
