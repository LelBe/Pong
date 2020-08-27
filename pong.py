import pygame
from pygame.locals import *
import sys
from math import *
from number import *
import random

#Constantes

WIDTH = 1280
HEIGHT = 900
block_size = 10
WHITE = (255, 255, 255)

#Initialisation

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
pygame.mouse.set_visible(False)

class Ball(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.pos_x = WIDTH/2
        self.pos_y = random.randrange(0, HEIGHT, 2)
        self.dx = 0
        self.dy = 0
        self.velocity = 2
        self.ball_rect = pygame.Rect(self.pos_x, self.pos_y, block_size, block_size)
        self.angle = random.randrange(-45, 45, 5)
        
    def check_collision(self, paddle_p1, paddle_p2):
        
        if self.ball_rect.colliderect(paddle_p1.paddle_rect):

            if paddle_p1.pos_y < self.pos_y < paddle_p1.pos_y + 10 or paddle_p1.pos_y < self.pos_y - 5 < paddle_p1.pos_y + 10:
                self.angle = -45

            if paddle_p1.pos_y + 10 < self.pos_y < paddle_p1.pos_y + 20:
                self.angle = -30

            if paddle_p1.pos_y + 20 < self.pos_y < paddle_p1.pos_y + 30:
                self.angle = -15
                
            if paddle_p1.pos_y + 30 < self.pos_y < paddle_p1.pos_y + 40:
                self.angle = -10
                
            if paddle_p1.pos_y + 40 < self.pos_y < paddle_p1.pos_y + 50:
                self.angle = 10
                
            if paddle_p1.pos_y + 50 < self.pos_y < paddle_p1.pos_y + 60:
                self.angle = 15
                
            if paddle_p1.pos_y + 60 < self.pos_y < paddle_p1.pos_y + 70:
                self.angle = 30

            if paddle_p1.pos_y + 70 < self.pos_y < paddle_p1.pos_y + 80 or paddle_p1.pos_y + 70 < self.pos_y + 5 < paddle_p1.pos_y + 80:
                self.angle = 45


        if self.ball_rect.colliderect(paddle_p2.paddle_rect):

            if paddle_p2.pos_y < self.pos_y < paddle_p2.pos_y + 10 or paddle_p2.pos_y < self.pos_y - 5 < paddle_p2.pos_y + 10:
                self.angle = -135

            if paddle_p2.pos_y + 10 < self.pos_y < paddle_p2.pos_y + 20: 
                self.angle = -150

            if paddle_p2.pos_y + 20 < self.pos_y < paddle_p2.pos_y + 30: 
                self.angle = -165

            if paddle_p2.pos_y + 30 < self.pos_y < paddle_p2.pos_y + 40: 
                self.angle = 170

            if paddle_p2.pos_y + 40 < self.pos_y < paddle_p2.pos_y + 50:
                self.angle = 190
        
            if paddle_p2.pos_y + 50 < self.pos_y < paddle_p2.pos_y + 60: 
                self.angle = 165
    
            if paddle_p2.pos_y + 60 < self.pos_y < paddle_p2.pos_y + 70: 
                self.angle = 150

            if paddle_p2.pos_y + 70 < self.pos_y < paddle_p2.pos_y + 80 or paddle_p2.pos_y + 70 < self.pos_y + 5 < paddle_p2.pos_y + 80:
                self.angle = 135


    def moove_ball(self):
        
        self.dx = self.velocity * cos(radians(self.angle))
        self.dy = self.velocity * sin(radians(self.angle))

        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_y > HEIGHT - block_size or self.pos_y < 0:
            self.angle = - self.angle

        self.ball_rect = pygame.Rect(self.pos_x, self.pos_y, block_size, block_size)
    
    def draw_ball(self):
        pygame.draw.rect(screen, WHITE, self.ball_rect)



class Paddle(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = 4
        self.lenght = 8
        self.paddle_rect = pygame.Rect(self.pos_x, self.pos_y, block_size, self.lenght * block_size)
        self.key_pressed = {'up': False, 'down': False}

    def moove_paddle(self, key_pressed):

        if key_pressed['down']:
            if self.pos_y > HEIGHT - self.lenght * block_size - 25:
                pass
            else:
                self.pos_y += self.dy
        elif key_pressed['up']:
            if self.pos_y < 25:
                pass
            else:
                self.pos_y -= self.dy
    
    def draw_paddle(self):

        self.paddle_rect = pygame.Rect(self.pos_x, self.pos_y, block_size, self.lenght * block_size)
        pygame.draw.rect(screen, WHITE, self.paddle_rect)


class Pong:

    def __init__(self):

        self.paddle_p1 = Paddle(25, HEIGHT/2)
        self.paddle_p2 = Paddle(WIDTH - 25, HEIGHT/2)
        self.paddle = [self.paddle_p1, self.paddle_p2]
        self.ball = Ball()
        self.run = True
        self.p1_has_goal = False
        self.p2_has_goal = False

    def score_update(self, score_p1, score_p2):

        #Update du score du joueur 1

        if score_p1 <= 9:

            number = number_liste[score_p1]
            for i, line in enumerate(number):
                for j, case in enumerate(line):
                    if number[i][j] == 1:
                        pygame.draw.rect(screen, WHITE, Rect(WIDTH/2 - 250 + j * 15, 25 + i * 15, 15, 15))
            
        elif score_p1 > 9:

            number = []
            st_score = str(score_p1)
            number = [int(st_score[0]), int(st_score[1])]
            d, u = number_liste[number[0]], number_liste[number[1]]

            for i, line in enumerate(d):
                for j, case in enumerate(line):
                    if d[i][j] == 1:
                        pygame.draw.rect(screen, WHITE, Rect(WIDTH/2 - 250 + j * 15, 25 + i * 15, 15, 15))
        
            for i, line in enumerate(u):
                for j, case in enumerate(line):
                    if u[i][j] == 1:
                        pygame.draw.rect(screen, WHITE, Rect(WIDTH/2 - 200 + j * 15, 25 + i * 15, 15, 15))
        
        # Update du score du joueur 2

        if score_p2 <= 9:

            number = number_liste[score_p2]
            for i, line in enumerate(number):
                for j, case in enumerate(line):
                    if number[i][j] == 1:
                        pygame.draw.rect(screen, WHITE, Rect(WIDTH/2 + 160 + j * 15, 25 + i * 15, 15, 15))
            
        elif score_p2 > 9:

            number = []
            st_score = str(score_p2)
            number = [int(st_score[0]), int(st_score[1])]
            d, u = number_liste[number[0]], number_liste[number[1]]

            for i, line in enumerate(d):
                for j, case in enumerate(line):
                    if d[i][j] == 1:
                        pygame.draw.rect(screen, WHITE, Rect(WIDTH/2 + 130 + j * 15, 25 + i * 15, 15, 15))
        
            for i, line in enumerate(u):
                for j, case in enumerate(line):
                    if u[i][j] == 1:
                        pygame.draw.rect(screen, WHITE, Rect(WIDTH/2 + 180 + j * 15, 25 + i * 15, 15, 15))

    def draw_gameboard(self):
        y = 15
        for i in range(0, 20):
            block = pygame.draw.rect(screen, WHITE, Rect(WIDTH/2, y, 5, 30))
            y += 60

    def reset_round(self):
        
        spawn_height = random.randrange(0, HEIGHT-10, 1)
        
        if self.p1_has_goal:
            self.ball.angle = random.randrange(5, 45, 1)
            self.ball.pos_x = WIDTH/2
            self.ball.pos_y = spawn_height

        if self.p2_has_goal:
            self.ball.angle = 180 - random.randrange(5, 45, 1)
            self.ball.pos_x = WIDTH/2
            self.ball.pos_y = spawn_height

        if self.p1_has_goal or self.p2_has_goal:
            self.paddle_p1.pos_x, self.paddle_p1.pos_y = 25, HEIGHT/2
            self.paddle_p2.pos_x, self.paddle_p2.pos_y = WIDTH -25, HEIGHT/2
        
            self.p1_has_goal = False
            self.p2_has_goal = False
            pygame.time.wait(500)

    def main(self):
        
        #Remise à 0 des scores

        score_p1 = 0
        score_p2 = 0
        clock = pygame.time.Clock()        

        while self.run:
            
            pygame.Surface.fill(screen, (0,0,0))
            self.draw_gameboard()
            self.score_update(score_p1, score_p2)

            #On vérifie les événemenents des joueurs

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w: self.paddle_p1.key_pressed['up'] = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_w: self.paddle_p1.key_pressed['up'] = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s: self.paddle_p1.key_pressed['down'] = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_s: self.paddle_p1.key_pressed['down'] = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_o: self.paddle_p2.key_pressed['up'] = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_o: self.paddle_p2.key_pressed['up'] = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_l: self.paddle_p2.key_pressed['down'] = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_l: self.paddle_p2.key_pressed['down'] = False

            #On parcourt la liste des raquettes des joueurs

            for p in self.paddle:
                p.moove_paddle(p.key_pressed)
                p.draw_paddle()

            #On vérifie si il y a collision avec une des deux raquettes
            self.ball.check_collision(self.paddle_p1, self.paddle_p2)
            
            #On bouge la ball avec les coordonnées mises à jour
            self.ball.moove_ball()

            #On dessine la balle mise à jour
            self.ball.draw_ball()

            if self.ball.pos_x > WIDTH:
                self.p1_has_goal, self.p2_has_goal = True, False
                score_p1 += 1
            elif self.ball.pos_x < 0:
                self.p1_has_goal, self.p2_has_goal = False, True
                score_p2 += 1

            self.reset_round()

            clock.tick(500)
            
            pygame.display.update()

if __name__ == '__main__':

    game = Pong()
    game.main()
