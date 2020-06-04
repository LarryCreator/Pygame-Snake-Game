import pygame
from math import isclose
from random import randint
#I could have made a new class to the food, but i didn't think it was necessary.
#As it's such a little game.
pygame.init()
white = (255, 255, 255)
grey = (50,50, 50)
green = (0, 128, 0)
red = (255, 8, 0)

class Snake():
    def __init__(self):
        self.surface = pygame.Surface((20, 20))
        self.food_surface = pygame.Surface((20, 20))
        self.surface.fill(green)
        self.food_surface.fill(red)
        self.facing = 'L'
        self.food = 0
        self.food_position = (0, 0)
        self.body_list = [(400, 10), (410, 10), (420, 10)]
        self.speed = int(400 * (1/60))
        self.length = 3

    def change_dir(self):
        #This function changes the direction that the snake
        #should be facing.
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.facing != 'D':
            self.facing = 'U'
        elif key[pygame.K_s] and self.facing != 'U':
            self.facing = 'D'
        elif key[pygame.K_a] and self.facing != 'R':
            self.facing = 'L'
        elif key[pygame.K_d] and self.facing != 'L':
            self.facing = 'R'

    def move(self):
        #This function moves the snake to the direction
        #that it's facing
        if self.facing == 'R':
            self.body_list.insert(0,(self.body_list[0][0] + self.speed, self.body_list[0][1]))
        if self.facing == 'L':
            self.body_list.insert(0,(self.body_list[0][0] - self.speed, self.body_list[0][1]))
        if self.facing == 'U':
            self.body_list.insert(0,(self.body_list[0][0], self.body_list[0][1] - self.speed))
        if self.facing == 'D':
            self.body_list.insert(0,(self.body_list[0][0], self.body_list[0][1] + self.speed))
        self.body_list.pop(self.length)

    def grow_up(self):
        #This function makes the snake grow when it's length increases.
        if self.length == len(self.body_list):
            pass
        else:
            if self.facing == 'R':
                while self.length != len(self.body_list):
                    self.body_list.insert(0, (self.body_list[0][0] + self.speed, self.body_list[0][1]))
            if self.facing == 'L':
                while self.length != len(self.body_list):
                    self.body_list.insert(0, (self.body_list[0][0] - self.speed, self.body_list[0][1]))
            if self.facing == 'U':
                while self.length != len(self.body_list):
                    self.body_list.insert(0, (self.body_list[0][0], self.body_list[0][1] - self.speed))
            if self.facing == 'D':
                while self.length != len(self.body_list):
                    self.body_list.insert(0, (self.body_list[0][0], self.body_list[0][1] + self.speed))

    def collision(self):
        #If  the snake collides with itself the game ends
        for i in self.body_list[1:]:
            if i == self.body_list[0]:
                print(f'\nYou died, your length was {self.length}!')
                quit(0)

    def create_food(self, screen):
        #This function creates a new food everytime the snake
        #gets close enough to one. And also blits it on the screen.
        if self.food == 0:
            self.food_position = (randint(0, 490), randint(0, 490))
            self.food = 1
        elif self.food == 1:
            screen.blit(self.food_surface, self.food_position)

    def just_ate(self):
        #If the snake just ate, it increases it's length by one.
        if isclose(self.body_list[0][0], self.food_position[0], abs_tol=20)\
           and isclose(self.body_list[0][1], self.food_position[1], abs_tol=20):
            self.food = 0
            self.length += 1

    def keep_on_screen(self):
        if self.body_list[0][0] <= -40:
            self.body_list[0] = (540, self.body_list[0][1])
        elif self.body_list[0][0] >= 540:
            self.body_list[0] = (-40, self.body_list[0][1])
        if self.body_list[0][1] <= -40:
            self.body_list[0] = (self.body_list[0][0], 540)
        elif self.body_list[0][1] >= 540:
            self.body_list[0] = (self.body_list[0][0], -40)

    def blit(self, screen):
        #This function blits the snake on the screen
        for i in self.body_list:
            screen.blit(self.surface, (i))



class Game():
    def __init__(self):
        self.fps = 60
        self.screen_size = (500, 500)
        self.screen = pygame.display.set_mode((self.screen_size))
        self.clock = pygame.time.Clock()
        self.snake = Snake()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)
            self.clock.tick(self.fps)
            self.screen.fill(0)
            self.snake.change_dir()
            self.snake.grow_up()
            self.snake.move()
            self.snake.collision()
            self.snake.create_food(self.screen)
            self.snake.just_ate()
            self.snake.keep_on_screen()
            self.snake.blit(self.screen)
            pygame.display.update()

Game().main()