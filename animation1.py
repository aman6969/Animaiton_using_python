import pygame
pygame.init
#color
white=(255,255,255)
black=(0,0,0)
green=(154,205,50)
#width
width=800
height=600
run=True
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("animation")
clock=pygame.time.Clock()
fps=60
#ball
ball_x=100
ball_y=100
ball_width=70
ball_height=70
ball_speed_x=5
ball_speed_y=5
ball=pygame.Rect(ball_x,ball_y,ball_width,ball_height)
while run :#endless run krega
    for event in pygame.event.get():# read events from keyboard
        if(event.type==pygame.QUIT):#jab cross button press krenge toh value false ho jyga...
            run=False
    ball.x=ball.x+ball_speed_x
    ball.y=ball.y+ball_speed_y# ball move kr rha h
    if(ball.left  <=0 or ball.right >= width):
        ball_speed_x=ball_speed_x*-1
    if(ball.top<=0 or ball.bottom>=height):
            ball_speed_y=ball_speed_y*-1
    screen.fill(white)# to change the screen color
    pygame.draw.ellipse(screen,green,ball)
    pygame.display.update()# to update the screen
    clock.tick(fps)

pygame.quit()            
quit()

