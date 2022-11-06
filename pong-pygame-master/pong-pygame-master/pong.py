# Shehraj Singh, fall 2020
# CMPUT 174 lab D03
# Mini - project 2

# An interactive minigame called Pong.

# importing modules required
import pygame, random


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((800, 600))
    # set the title of the display window
    pygame.display.set_caption('Pong')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
# An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color(64, 104, 149)

        self.FPS = 100
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        #def __init__(self, string, color, font, size, position, bold=False, italic=False, surface)

        # === game specific objects
        self.ball_velocity = [random.choice([1,-1]), random.randint(1,4)]
        self.ball = Ball('white', 7, [400, 300], self.ball_velocity, self.surface)
        self.paddle1 = Paddle(20, 250, 10, 100, 'white',0 , self.surface)
        self.paddle2 = Paddle(770, 250, 10, 100, 'white',0 , self.surface)
        self.midline = Paddle(self.surface.get_width()/2, 0, 3, self.surface.get_height(), 'grey', 0, self.surface)
        self.player1_score = Score('0', 'white', 'comic sans', 30, ((self.surface.get_width()/2)-25,0), self.surface)
        self.player2_score = Score('0', 'white', 'comic sans', 30, ((self.surface.get_width()/2)+15,0), self.surface)
        self.frame_counter = 0


    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame

            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()

            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second


    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            if event.type == pygame.KEYUP:
                self.handle_keyup(event)


    def handle_keydown(self, event):
        # handles the keydown events

        if event.key == pygame.K_q:
            self.paddle1.set_velocity(-5)
        if event.key == pygame.K_a:
            self.paddle1.set_velocity(5)
        if event.key == pygame.K_p:
            self.paddle2.set_velocity(-5)
        if event.key == pygame.K_l:
            self.paddle2.set_velocity(5)


    def handle_keyup(self, event):
        # handles the keyup events

        if event.key == pygame.K_q:
            self.paddle1.set_velocity(0)
        if event.key == pygame.K_a:
            self.paddle1.set_velocity(0)
        if event.key == pygame.K_p:
            self.paddle2.set_velocity(0)
        if event.key == pygame.K_l:
            self.paddle2.set_velocity(0)


    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color) # clear the display surface first
        self.midline.draw()
        self.player1_score.draw()
        self.player2_score.draw()
        self.ball.draw()
        self.paddle1.draw()
        self.paddle2.draw()
        pygame.display.update() # make the updated surface appear on the display


    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.ball.move(self.paddle1, self.paddle2)
        self.paddle1.move()
        self.paddle2.move()
        self.update_score()


    def update_score(self):
        # updating score

        if self.ball.hit_wall() == 1:
            self.player1_score.update()
        if self.ball.hit_wall() == 0:
            self.player2_score.update()


    def decide_continue(self):
        # Check and remember if the game should continue
        # decided on the basis whether a player has 11 score
        # - self is the Game to check

        if self.player1_score.get_score() == 11 or self.player2_score.get_score() == 11:
            self.continue_game = False


class Ball:
# An object in this class represents a Dot that moves

    def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
        # Initialize a Ball.
        # - self is the ball to initialize
        # - color is the pygame.Color of the ball
        # - center is a list containing the x and y int
        #   coords of the center of the ball
        # - radius is the int pixel radius of the ball
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame.Surface object

        self.color = pygame.Color(ball_color)
        self.radius = ball_radius
        self.center = ball_center
        self.velocity = ball_velocity
        self.surface = surface

    def get_x(self):
        return self.center[0]

    def get_y(self):
        return self.center[1]

    def get_radius(self):
        return self.radius

    def get_velocity(self):
        return self.velocity

    def get_vx(self):
        return self.velocity[0]

    def get_vy(self):
        return self.velocity[1]

    def move(self, paddle1, paddle2):
        # Change the location of the ball by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the ball

        for i in range(0,2):
            self.center[i] = (self.center[i] + self.velocity[i])

        # changing direction if ball bounces off top or bottom
        if self.get_y() <= 0 or self.get_y() >= self.surface.get_height():
            self.velocity[1] = -self.velocity[1]

        # changing direction if ball bounces off left or right
        if self.get_x() <= 0 or self.get_x() >= self.surface.get_width():
            self.velocity[0] = -self.velocity[0]

        # changing direction if ball hits paddle 1
        if (self.get_x() == (paddle1.get_x() + paddle1.get_width())
        and self.get_vx()< 0
        and paddle1.get_y() <= self.get_y() <= (paddle1.get_y() + paddle1.get_height())):

            self.velocity[0] = -self.velocity[0]

        # changing direction if ball hits paddle 2
        if (self.get_x() == paddle2.get_x()
        and self.get_vx() > 0
        and paddle2.get_y() <= self.get_y() <= (paddle2.get_y() + paddle2.get_height())):

            self.velocity[0] = -self.velocity[0]

    def draw(self):
        # Draw the ball on the surface
        # - self is the ball
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


    def hit_wall(self):
    # checks if the ball hits the left or right walls
    # returns 0 if it hits left wall
    # returns 1 if it hits right wall
        if self.get_x() <= 0:
            return 0
        if self.get_x() >= self.surface.get_width():
            return 1

class Paddle:
# an object of this class represents a paddle that moves on user input

    def __init__(self, x, y, width, height, paddle_color, velocity, surface):
        # Initialize a paddle
        # -self is the paddle
        # -x is the coordinate of topleft of paddle
        # -y is the coordinate of topleft of paddle
        # -width is the width of the paddle
        # -height is the height of the paddle
        # -paddle_color is the color of the paddle
        # -surface is the surface to draw on

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = pygame.Color(paddle_color)
        self.velocity = velocity
        self.surface = surface

    def get_x(self):
        # returns x of topleft of paddle
        return self.x

    def get_y(self):
        # returns y of topleft of paddle
        return self.y

    def get_height(self):
        # returns height of the paddle
        return self.height

    def get_width(self):
        # returns width of the paddle
        return self.width

    def draw(self):
        # draws a rectangle
        rect_params = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, rect_params)

    def move(self):
        # move the paddle
        # self is the paddle

        # stopping the paddle if at the edge
        if self.y <= 0 :
            self.y = 0
        elif self.y + self.height >= self.surface.get_height():
            self.y = self.surface.get_height() - self.height

        # moving by adding velocity
        self.y = self.y + self.velocity

    def set_velocity(self, velocity):
        # moves paddle up according to the velocity
        if velocity > 0 and self.y + self.height < self.surface.get_height():
            self.velocity = velocity
        elif velocity < 0 and self.y > 0:
            self.velocity = velocity
        else :
            self.velocity = 0


class Score:
    # represents score object
    def __init__(self, string, color, font, size, position, surface, bold=False, italic=False):
        # Initialize a score
        # - self is the score
        # - string the text
        # - color is the color of text
        # - font is the font of text
        # - size is the size of text
        # - position is the position if rendered image from text
        # - bold is optional and is set to false by default
        # - italic is optional and is set to false by default
        # - surface is the surface on which the text is blit

        self.text = string
        self.color = pygame.Color(color)
        self.font = font
        self.size = size
        self.pos = position
        self.bold = bold
        self.italic = italic
        self.surface = surface

    def __int__(self):
        # defines value of Score
        return int(self.text)

    def get_score(self):
        # returns int value of Score
        return int(self)

    def draw(self):
        # draw the score on the window

        text_font = pygame.font.SysFont(self.font, self.size, self.bold, self.italic)
        text_image = text_font.render(self.text, True, self.color)
        self.surface.blit(text_image, self.pos)

    def update(self):
        # update the Score
        self.text = int(self.text)
        self.text += 1
        self.text = str(self.text)
        text_font = pygame.font.SysFont(self.font, self.size, self.bold, self.italic)
        text_image = text_font.render(self.text, True, self.color)
        self.surface.blit(text_image, self.pos)

main()


## Help taken from ##
# https://stackoverflow.com/questions/18995652/pygame-key-set-repeat-not-working
