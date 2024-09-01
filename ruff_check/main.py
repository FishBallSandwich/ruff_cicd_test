import random


def rng():
    rand_int = random.randint(1, 10)

    print(rand_int)


def rand_choice():
    mylist = ["Ajay", "Davide", "Keanu", "Jojo"]
    print(random.choice(mylist))
