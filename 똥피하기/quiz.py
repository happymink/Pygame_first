import pygame
import random
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Minkyun Game")  #게임 이름


#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("C:/Users/민균/Desktop/Pygame_first/똥피하기/background.jpg")


#스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/민균/Desktop/Pygame_first/똥피하기/dog.png")
character_size = character.get_rect().size #캐릭터의 가로 세로 크기 구하기 함수 
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = ( screen_width / 2 ) - ( character_width / 2 )   #화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height  #화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)


# 이동할 좌표
to_x = 0


#이동 속도
character_speed = 0.6
enemy_speed = 10


#적 캐릭터 enemy
enemy = pygame.image.load("C:/Users/민균/Desktop/Pygame_first/똥피하기/enemy.png")
enemy_size = enemy.get_rect().size #캐릭터의 가로 세로 크기 구하기 함수 
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_height = enemy_size[1] #캐릭터의 세로 크기
enemy_x_pos = (random.randint((enemy_width),(screen_width-enemy_width)))   #랜덤 위치
enemy_y_pos = (0)  #화면 세로 크기 가장 위에 해당하는 곳에 위치 (세로)


# 폰트 정의 
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 100

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() #시작 tick 을 받아옴


#이벤트 루프

running= True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if  event.type == pygame.QUIT:  # 창이 닫히는 이벤트 >> x표시를 눌러 게임을 껏을 때
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            

    
        
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x *dt #프레임 당 속도를 맞춰주기 위해 *dt
   


    #적이 화면 밖으로 나갈 때 맨위로 원위치 - x좌표 랜덤부여
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = (random.randint(0,screen_width-enemy_width))


    #가로 경계값 처리 (캐릭터가 화면 밖으로 나갈 때)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

        
    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    #충동 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background, (0, 0))  #배경 그리기 (x,y좌표)
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기


    #타이머 집어 넣기
    #경과시간 계산
    elapsed_time = ( pygame.time.get_ticks() - start_ticks )  / 1000               #지난 시간 ms이기 때문에 초(s)로 표현하기 위해  /1000

    timer = game_font.render(str(int (total_time - elapsed_time)), True, (0,0,255) )  #초단위로 하기위해 인트형으로 형변환 
    #출력할 글자 , True, 글자 색상
    screen.blit(timer, (10, 10))

    #만약 시간이 0이하면 게임 종료
    if total_time - elapsed_time <=0:
        print("클리어")
        running = False 


    pygame.display.update() #게임 화면은 다시 그리기 ! (계속 화면 표시)
    

pygame.time.delay(2000) # 2초 대기
 

# pygame 종료
pygame.quit()
