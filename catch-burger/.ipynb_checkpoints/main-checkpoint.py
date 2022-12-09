import pygame
import random
import os

pygame.init() #초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Catch Burger")

# FPS
clock = pygame.time.Clock()
################################################################################################################
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(image_path, "rider_right.png"))
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아해에 위치
character_speed = 10

# enemy 캐릭터 불러오기
stink = pygame.image.load(os.path.join(image_path, "stink.png"))
stink_size = stink.get_rect().size # 이미지 크기를 구해옴
stink_width = stink_size[0] # 캐릭터의 가로 크기
stink_height = stink_size[1] # 캐릭터의 세로 크기
stink_x_pos = random.randint(0, screen_width - stink_width) # 화면 가로의 절반크기에 해당하는곳에 위치
stink_y_pos = 0 # 화면 세로 크기 가장 아해에 위치
stink_speed = 12

# burger 캐릭터 불러오기
burger = pygame.image.load(os.path.join(image_path, "burger.png"))
burger_size = burger.get_rect().size # 이미지 크기를 구해옴
burger_width = burger_size[0] # 캐릭터의 가로 크기
burger_height = burger_size[1] # 캐릭터의 세로 크기
burger_x_pos = random.randint(0, screen_width - burger_width) # 화면 가로의 절반크기에 해당하는곳에 위치
burger_y_pos = 0 # 화면 세로 크기 가장 아해에 위치
burger_speed = 16

# coke 캐릭터 불러오기
coke = pygame.image.load(os.path.join(image_path, "coke.png"))
coke_size = coke.get_rect().size # 이미지 크기를 구해옴
coke_width = coke_size[0] # 캐릭터의 가로 크기
coke_height = coke_size[1] # 캐릭터의 세로 크기
coke_x_pos = random.randint(0, screen_width - coke_width) # 화면 가로의 절반크기에 해당하는곳에 위치
coke_y_pos = 0 # 화면 세로 크기 가장 아해에 위치
coke_speed = 10

# stars 캐릭터 불러오기
stars = pygame.image.load(os.path.join(image_path, "stars.png"))
stars_size = stars.get_rect().size # 이미지 크기를 구해옴
stars_width = stars_size[0] # 캐릭터의 가로 크기
stars_height = stars_size[1] # 캐릭터의 세로 크기
stars_x_pos = 0 # 화면 가로의 절반크기에 해당하는곳에 위치
stars_y_pos = 0 # 화면 세로 크기 가장 아해에 위치
stars_speed = 14

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트객체 생성 (폰트, 크기)

# 총 시간
total_time = 60

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 현재 틱을 받아옴

# 점수
score = 0

# 이벤트 루프
running = True # 게임이 진행중인가?

while running:
  dt = clock.tick(60) #화면의 초당 프레임수 설정
  # print(f"fps : {str(clock.get_fps())}")
  
  for event in pygame.event.get(): # 어떤이벤트가 발생하엿는가
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하엿는가?
      running = False # 게임진행중아님

    if event.type == pygame.KEYDOWN: # 키가 눌러졋는지 확인
      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽
        character = pygame.image.load(os.path.join(image_path, "rider_left.png"))
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽
        character = pygame.image.load(os.path.join(image_path, "rider_right.png"))
        to_x += character_speed
      
    if event.type == pygame.KEYUP: # 방향키 뗴면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
        to_y = 0

  character_x_pos += to_x
  # 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width

  stink_y_pos += stink_speed
  if stink_y_pos > screen_height:
    stink_y_pos = 0
    stink_x_pos = random.randint(0, screen_width - stink_width)

  burger_y_pos += burger_speed
  if burger_y_pos > screen_height:
    burger_y_pos = 0
    burger_x_pos = random.randint(0, screen_width - burger_width)

  coke_y_pos += coke_speed
  if coke_y_pos > screen_height:
    coke_y_pos = 0
    coke_x_pos = random.randint(0, screen_width - coke_width)

  stars_y_pos += stars_speed
  
  # 충돌 처리
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  stink_rect = stink.get_rect()
  stink_rect.left = stink_x_pos
  stink_rect.top = stink_y_pos

  burger_rect = burger.get_rect()
  burger_rect.left = burger_x_pos
  burger_rect.top = burger_y_pos

  coke_rect = coke.get_rect()
  coke_rect.left = coke_x_pos
  coke_rect.top = coke_y_pos

  stars_rect = stars.get_rect()
  stars_rect.left = stars_x_pos
  stars_rect.top = stars_y_pos

  # 충돌 체크
  if character_rect.colliderect(stink_rect):
    print("충돌했어요.")
    score -= 5000
    stink_y_pos = 0
    stink_x_pos = random.randint(0, screen_width - stink_width)
    # running = False
  
  if character_rect.colliderect(burger_rect):
    score += 1000
    stars_y_pos = burger_y_pos
    stars_x_pos = burger_x_pos
    burger_y_pos = 0
    burger_x_pos = random.randint(0, screen_width - burger_width)
    

  if character_rect.colliderect(coke_rect):
    score += 500
    stars_y_pos = coke_y_pos
    stars_x_pos = coke_x_pos
    coke_y_pos = 0
    coke_x_pos = random.randint(0, screen_width - coke_width)

  
  screen.blit(background, (0, 0))
  screen.blit(character, (character_x_pos, character_y_pos)) 
  screen.blit(stink, (stink_x_pos, stink_y_pos)) 
  screen.blit(burger, (burger_x_pos, burger_y_pos))  
  screen.blit(coke, (coke_x_pos, coke_y_pos))
  screen.blit(stars, (stars_x_pos, stars_y_pos))
  


  # 타이머
  # 경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 

  timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
  # 출력할 글자 시간, 트루, 글자색상
  screen.blit(timer, (10, 10))

  money = game_font.render(f"SCORE: {int(score)}", True, (255, 255, 255))
  screen.blit(money, (120, 10))

  if total_time - elapsed_time <= 0:
    print("Time Out!")
    running = False

  pygame.display.update() 

msg = game_font.render(f"SCORE: {int(score)}", True, (255, 255, 0))
msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) 

# 게임종료
pygame.quit()