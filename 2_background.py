import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Minkyun Game")#게임 이름


#배경이미지 불러오기

background = pygame.image.load("C:/Users/민균/Desktop/Pygame_first/background.png")
#이벤트 루프

running= True #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if  event.type == pygame.QUIT:  # 창이 닫히는 이벤트 >> x표시를 눌러 게임을 껏을 때
            running = False

    screen.blit(background, (0, 0))  #배경 그리기 (x,y좌표)
    pygame.display.update() #게임 화면은 다시 그리기 ! (계속 화면 표시)


 

# pygame 종료
pygame.quit()
