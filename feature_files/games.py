import random


class BotMessages:
    messages = {
        "reflexion": "How can I beat you..."
    }


class Interaction:
    @staticmethod
    def prompt_user(message: str):
        return input("GAME> " + message)

    @staticmethod
    def tell_user(message: str):
        print("GAME> " + message)

    @staticmethod
    def wait_for_user(message: str):
        input("GAME> " + message + "\n\tPRESS ENTER")

    def pick_random(message_type):
        return random.choice(BotMessages.messages[message_type])


class TicTacToe:
    def __init__(self):
        self.grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]  # 0 means nothing, 1 human, 2 computer
        self.turn = random.randint(1, 2)
        self.winner = 0
        self.play()

    def player_input(self):
        number = Interaction.prompt_user(
            "\t1, 2, 3\n\t4, 5, 6\n\t7, 8, 9\nWhatEmplacement do you want to take? ")
        try:
            number = int(number)
        except:
            return "Invalid"
        if number < 1 or number > 9:
            return "Invalid"
        return ((number-1) // 3, (number-1) % 3)

    def computer_input(self):
        possible_coos = []
        for i, row in enumerate(self.grid):
            for j, item in enumerate(row):
                if item == 0:
                    possible_coos.append((i, j))
        if len(possible_coos) == 0:
            return "Endgame"
        else:
            return random.choice(possible_coos)

    def display_game(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print("")

    def play(self):
        while self.winner == 0:
            self.display_game()
            if self.turn == 1:
                coos = self.player_input()
                if type(coos) is str:
                    Interaction.tell_user("Invalid input. You wasted a turn")
                elif self.grid[coos[0]][coos[1]] == 0:
                    self.grid[coos[0]][coos[1]] = 1
                else:
                    Interaction.tell_user(
                        "The emplacement you choosed is already taken. You wasted a turn")
            else:
                Interaction.tell_user(Interaction.pick_random("reflexion"))
                coos = self.computer_input()
                if type(coos) is str:
                    Interaction.tell_user("Endgame")
                else:
                    self.grid[coos[0]][coos[1]] = 2
            self.turn = 2 if self.turn == 1 else 1


if __name__ == "__main__":
    TicTacToe()
