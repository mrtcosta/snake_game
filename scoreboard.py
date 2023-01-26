from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("data.txt", mode="r") as highscore_text:
            self.high_score = int(highscore_text.read())


    # INITIAL SCREEN
    def menu(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 20)
        self.hideturtle()
        self.write("     SNAKE GAME\nPress space to start", False, 'center', font=("Courier", 28, 'bold'))

    # COUNTING THE SCORE
    def points(self, got_food):

        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        if got_food == 'yes':
            self.scores += 1
        self.write(f"Score: {self.scores} High Score: {self.high_score}", False, "center", font=("Courier", 24, "bold"))


    # FINISH THE GAME
    def game_over(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
            with open("data.txt", mode="w") as highscoretext:
                highscoretext.write(str(self.high_score))

        self.clear()
        self.goto(0, 0)
        self.write(f"       GAME OVER\n\nScore: {self.scores}  High Score: {self.high_score}\n\nPress space to continue"
                   , False, align="center", font=("Courier", 24, "bold"))
