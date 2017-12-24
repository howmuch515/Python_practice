from random import randint
ROCK, PAPER, SCISSORS = 1, 2, 3


class Player():
    def __init__(self):
        self.card = {ROCK: 2, PAPER: 2, SCISSORS: 2}
        self.star = 3
        self.hand = 0

    def haveCard(self, hand):
        return self.card[hand] > 0

    def setCard(self, hand):
        if not self.haveCard(hand):
            raise Exception("Not last")
        else: 
            self.card[hand] -= 1
            self.hand = hand

class CPU(Player):
    def __init__(self):
        super().__init__()

    def setCard(self):
        while True:
            hand = randint(1, 3)
            if not self.haveCard(hand):
                continue
            else:
                self.card[hand] -= 1
                self.hand = hand
                break



class LimitedRSP():
    def __init__(self):
        self.user = Player()
        self.cpu = CPU()
        self.round = 1


    def showMenu(self):
        print("[1] ROCK")
        print("[2] PAPER")
        print("[3] SCISSORS")


    def showStatus(self):
        print("ROUND: {}".format(self.round))
        print("STAR\nUSER: {}, CPU: {}".format(self.user.star, self.cpu.star))
        print("last card\nROCK: {}, PAPER: {}, SCISSORS: {}".format(self.user.card[ROCK], self.user.card[PAPER], self.user.card[SCISSORS]))



    def showResult(self):
        print("GAME OVER")


    def setCard(self, user_select):
        if user_select.isdigit():
            print("A")
            user_select = int(user_select)
            if user_select in (ROCK, PAPER, SCISSORS):
                if self.user.haveCard(user_select):
                    self.user.setCard(user_select)
                    self.cpu.setCard()
                    return True
                else: 
                    return False
            else:
                return False
        else:
            return False


    def isGameOver(self):
        return (self.user.star == 0 or self.cpu.star == 0) or (self.round > 6)

    def win(self):
        print("win")
        self.round += 1
        self.user.star += 1
        self.cpu.star -= 1
    def lose(self):
        print("lose")
        self.round += 1
        self.user.star -= 1
        self.cpu.star += 1

    def draw(self):
        print("draw")
        pass
            
    def judge(self):
        print("C")
        user_hand, cpu_hand = self.user.hand, self.cpu.hand
        if user_hand == cpu_hand:
            return self.draw() 
        elif user_hand == ROCK:
            if cpu_hand == PAPER:
                return self.lose()
            else:
                return self.win()
        elif user_hand == PAPER:
            if cpu_hand == SCISSORS:
                return self.lose()
            else:
                return self.win()
        else: # user_hand == SCISSORS
            if cpu_hand == ROCK:
                return self.lose()
            else:
                return self.win()

        
def main():
    game = LimitedRSP()
    while True:
        game.showStatus()
        game.showMenu()
        user_input = input("Your choice >> ")

        if not game.setCard(user_input):
            print("B")
            continue
        print("D")
        game.judge()
        if game.isGameOver():
            print("+++++ GAME OVER +++++")
            game.showResult()
            break


if __name__ == '__main__':
    main()
