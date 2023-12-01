import pygame
import sys
import random


width = 600
height = 800
screen = pygame.display.set_mode((width, height))


white = (255, 255, 255)
black = (0, 0, 0)
random_color = white

paddle_w = 20
paddle_h = 120
paddle_sd = 15

ball_sz = 20
ball_sd_x = 6
ball_sd_y = 6

paddle_l = pygame.Rect(20, height // 2 - paddle_h
                       // 2, paddle_w, paddle_h)

paddle_r = pygame.Rect(width - 40, height // 2 -
                       paddle_h // 2, paddle_w,
                       paddle_h)

ball = pygame.Rect(width // 2 - ball_sz // 2,
                   height // 2 - ball_sz // 2,
                   ball_sz, ball_sz)


image = pygame.image.load('pexels-eva-bronzini-7630329.jpg')


def backgrnd(image):
    size = pygame.transform.scale(image,(width, height))
    screen.blit(size,(0, 0))


def mv_paddles():
    key = pygame.key.get_pressed()

    if key[pygame.K_w] and paddle_l.top > 0:
        paddle_l.y -= paddle_sd

    if key[pygame.K_s] and paddle_l.bottom < height:
        paddle_l.y += paddle_sd

    if key[pygame.K_UP] and paddle_r.top > 0:
        paddle_r.y -= paddle_sd

    if key[pygame.K_DOWN] and paddle_r.bottom < height:
        paddle_r.y += paddle_sd


def mv_ball():
    global ball_sd_x, ball_sd_y, random_color
    ball.x += ball_sd_x
    ball.y += ball_sd_y
    

    if ball.top <= 0 or ball.bottom >= height:
        ball_sd_y *= -1

    if ball.left <= 0 or ball.right >= width:
        ball.x = width // 2 - ball_sz // 2
        ball.y = height // 2 - ball_sz // 2

    if ball.colliderect(paddle_l) or ball.colliderect(paddle_r):
        ball_sd_x *= -1 
        random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))



def main(): 

    pygame.init()
    pygame.display.set_caption('PING THE PONG!')


    running = True
    while running:
        screen.fill(black)

        backgrnd(image)
        

        pygame.draw.rect(screen, black, paddle_l)
        pygame.draw.rect(screen, black, paddle_r)
        pygame.draw.ellipse(screen, random_color, ball)
        pygame.draw.aaline(screen, white,(width // 2, 0), 
                        (width // 2, height))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mv_paddles()
        mv_ball()
        

        pygame.display.flip()
        clock= pygame.time.Clock()
        clock.tick(60)


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
