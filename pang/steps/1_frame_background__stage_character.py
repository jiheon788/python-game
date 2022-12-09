import os
import pygame
#################################################################################################
# 기본 초기화
pygame.init() #초기화

# 화면 크기 설정
screen_width = 640 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang")

# FPS
clock = pygame.time.Clock()
#################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도,폰트 등)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


running = True 

while running:
  dt = clock.tick(30) 
  
  # 2. 이벤트 처리(키보드, 마우스 등)
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 

  # 3. 게임 캐릭터 위치 정의
  
  # 4. 충돌 처리
 
  # 5. 화면에 그리기
  screen.blit(background, (0, 0))
  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))
 
  pygame.display.update() 

pygame.quit()