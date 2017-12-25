from random import randint

ROCK, PAPER, SCISSORS = 1, 2, 3
HANDS = ("ROCK", "PAPER", "SCISSORS")


# 1P
class Player():
    def __init__(self):
        # Player has cards: ROCK * 2, PAPER * 2, SCISSORS * 2
        self.card = {ROCK: 2, PAPER: 2, SCISSORS: 2}

        # Player has STAR * 3
        self.star = 3

        # chosen card by Player
        self.hand = 0


    # checking cards are left
    def checkLeftCard(self, hand):
        return self.card[hand] > 0


    # set user's choice to hand
    def setCard(self, hand):
        self.card[hand] -= 1
        self.hand = hand

# 2P
class CPU(Player):
    def __init__(self):
        super().__init__()

    
    # cpu's choice at random
    def setCard(self):
        while True:

            # choice hand at random
            hand = randint(1, 3)

            # if choiced hand is not left, reset
            if not self.checkLeftCard(hand):
                continue
            else:
                self.card[hand] -= 1
                self.hand = hand
                break


# Game class
class LimitedRSP():
    def __init__(self):
        self.user = Player()
        self.cpu = CPU()

        # counters
        self.round = 1
        self.win_counter = 0
        self.lose_counter = 0
        self.draw_counter = 0


    # Show menu
    def showMenu(self):
        print("ROUND: {}".format(self.round))
        print("STAR: {}".format(self.user.star))
        print()
        print("Please choice.\n1.ROCK: ({})\n2.PAPER: ({})\n3.SCISSORS: ({})".format(self.user.card[ROCK], self.user.card[PAPER], self.user.card[SCISSORS]))


    # show result at the end
    def showResult(self):
        print("GAME OVER")
        if self.user.star == self.cpu.star:
            print("DRAW")
        elif self.user.star > self.cpu.star:
            print("WINNER: Player")
        else:
            print("WINNER: CPU")
        print("win:{}, lose:{}, draw:{}".format(self.win_counter, self.lose_counter, self.draw_counter))


    # set Card Player and CPU
    def chooseCard(self, user_choice):
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice in (ROCK, PAPER, SCISSORS):
                if self.user.checkLeftCard(user_choice):
                    self.user.setCard(user_choice)
                    self.cpu.setCard()
                    return True
                else: 
                    print("\nInvalid Choice!\n")
                    return False
            else:
                print("\nInvalid Choice!\n")
                return False
        else:
            print("\nInvalid Choice!\n")
            return False


    # check game over
    def isGameOver(self):
        return (self.user.star == 0 or self.cpu.star == 0) or (self.round > 6)


    def win(self):
        self.win_counter += 1
        self.round += 1
        self.user.star += 1
        self.cpu.star -= 1
        print("WIN")
        print("STAR {} -> {}".format(self.user.star - 1, self.user.star))
        print()


    def lose(self):
        self.lose_counter += 1
        self.round += 1
        self.user.star -= 1
        self.cpu.star += 1
        print("LOSE")
        print("STAR {} -> {}".format(self.user.star + 1, self.user.star))
        print()


    def draw(self):
        self.draw_counter += 1
        self.round += 1
        print("DRAW")
        print()
            

    # judge the outcome of janken
    def judge(self):
        # gu par choki
        user_hand, cpu_hand = self.user.hand, self.cpu.hand
        print("YOU {}\nCPU {}".format(HANDS[user_hand - 1], HANDS[cpu_hand - 1]))
        (self.draw, self.lose, self.win)[cpu_hand - user_hand]()
        
        
# MAIN
def main():
    game = LimitedRSP()
    while True:
        game.showMenu()
        user_input = input("Your choice -> ")

        # checking validity and set card
        if not game.chooseCard(user_input):
            continue

        # RSP battle
        game.judge()
        
        # if game over, show result and finish game
        if game.isGameOver():
            game.showResult()
            break


if __name__ == '__main__':
    main()
