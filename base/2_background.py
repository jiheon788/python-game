import pygame

pygame.init() #초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Practice")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\82104\\PythonWorkspace\\pygame_basic\\background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
  for event in pygame.event.get(): # 어떤이벤트가 발생하엿는가
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하엿는가?
      running = False # 게임진행중아님

  # screen.fill((0, 0, 255))  rgb
  screen.blit(background, (0, 0)) # 배경그리기

  pygame.display.update() # 게임화면 다시그리기


# 게임종료
pygame.quit()