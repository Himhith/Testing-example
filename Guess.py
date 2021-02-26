from random import randint
import sys
# generate a number 1~10
ans = randint(1, 10)

# input from user?
# check that input is a number 1~10


def guess_num(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
            print('try harder')
            return False
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        return False


if __name__ == "__main__":
    while True:
        if (guess_num(int(input('guess a number 1~10:  ')), ans)):
            break
