from random import randint
ROCK, PAPER, SCISSORS = 1, 2, 3

class Player():
    def __init__(self):
        self.card = {ROCK: 2, PAPER: 2, SCISSORS: 2}
        self.star = 3

    def select_hand(hand):
        if self.card[hand] == 0:
            print("Card is nothing...")
        else: 
            self.card[hand] -= 1


class CPU(Player):
    def __init__(self):
        super().__init__()

    def select_hand():
        hand = randint(1, 3)
        if self.card[hand] == 0:
            return select_hand()
        else:
            self.card[hand] -= 1
            return hand



class LimitedRSP():
    def __init__(self):
        self.user = Player()
        self.cpu = CPU()



    def menu(self):
        print("[1] ROCK")
        print("[2] PAPER")
        print("[3] SCISSORS")
        user_input = input("YOUR SELECT ==> ")
        return user_input

        if user_select.isdigit():
            user_select = int(user_select)
            if user_select in (ROCK, PAPER, SCISSORS)
                user.select_hand(user_selct)
                cpu_select = self.cpu.select_hand()
            else:
                print("Invalid input!!")
        else:
            print("Invalid input!!")


        
    def judge(self):
        WIN, DRAW, LOSE = 1, 0, -1

        

        
def main():
    pass


if __name__ == '__main__':
    main()
