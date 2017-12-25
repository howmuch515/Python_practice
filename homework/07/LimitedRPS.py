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
        self.you = Player()
        self.cpu = CPU()

        # counters
        self.round = 1
        self.win_counter = 0
        self.lose_counter = 0
        self.draw_counter = 0


    # Show menu
    def showMenu(self):
        print("+" * 30)
        print("ROUND: {}".format(self.round))
        print("STAR: {}".format(self.you.star))
        print()
        print("Please choice.")

        # show choice
        for i in range(1, 4):
            print("{}.{}: ({})".format(i, HANDS[i - 1], self.you.card[i]))

        print()


    # show result at the end
    def showResult(self):
        print("GAME OVER")
        if self.you.star == self.cpu.star:
            print("DRAW")
        elif self.you.star > self.cpu.star:
            print("WINNER: YOU")
        else:
            print("WINNER: CPU")
        print("win:{}, lose:{}, draw:{}".format(self.win_counter, self.lose_counter, self.draw_counter))
        print()


    # set Card You and CPU
    def chooseCard(self, you_choice):
        if not you_choice in ("1", "2", "3"):
            print("Invalid Choice!")
            print()
            raise Exception

        # type change. str -> int
        you_choice = int(you_choice)

        if self.you.checkLeftCard(you_choice):
            self.you.setCard(you_choice)
            self.cpu.setCard()
            return True
        else:
            print("Not left")
            print()
            raise Exception


    # check game over
    def isGameOver(self):
        return (self.you.star == 0 or self.cpu.star == 0) or (self.round > 6)


    def win(self):
        self.win_counter += 1
        self.round += 1
        self.you.star += 1
        self.cpu.star -= 1
        print("WIN")
        print("STAR {} -> {}".format(self.you.star - 1, self.you.star))
        print()


    def lose(self):
        self.lose_counter += 1
        self.round += 1
        self.you.star -= 1
        self.cpu.star += 1
        print("LOSE")
        print("STAR {} -> {}".format(self.you.star + 1, self.you.star))
        print()


    def draw(self):
        self.draw_counter += 1
        self.round += 1
        print("DRAW")
        print()
            

    # judge the outcome of janken
    def judge(self):
        you_hand, cpu_hand = self.you.hand, self.cpu.hand
        print("YOU {}\nCPU {}".format(HANDS[you_hand - 1], HANDS[cpu_hand - 1]))
        print()

        # judge method
        (self.draw, self.lose, self.win)[cpu_hand - you_hand]()
        
        
# MAIN
def main():
    game = LimitedRSP()
    while True:
        game.showMenu()
        you_input = input("Your choice -> ")
        print()

        # checking validity and set card
        try: 
            game.chooseCard(you_input)
        except:
            continue


        # RSP battle
        game.judge()
        
        # if game over, show result and finish game
        if game.isGameOver():
            game.showResult()
            break


if __name__ == '__main__':
    main()
