import pygame

pygame.init()

screenHeight = 600
screenWidth = 1100
screen = pygame.display.set_mode((screenWidth, screenHeight))

backgroundImage = pygame.image.load("dinosaur/background.png")

class Dinosaurus:
    x = 80
    y = 310
    yDuck = 340
    jumpVelDefault = 8.5
 
    def __init__(self):
        self.runningSprite = [pygame.image.load("dinosaur/run1.png"), pygame.image.load("dinosaur/run2.png")]
        self.duckingSprite = [pygame.image.load("dinosaur/duck1.png"), pygame.image.load("dinosaur/duck2.png")]
 
        self.ducking = False
        self.running = True
        self.jumping = False
 
        self.steps = 0
        #self.jumpVel = self.jumpVel
        self.image = self.runningSprite[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.jumpVel = self.jumpVelDefault
 
    def update(self, userInput):
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        if self.jumping:
            self.jump()
 
        if self.steps >= 10:
            self.steps = 0
 
        if userInput[pygame.K_UP] and not self.jumping:
            self.ducking = False
            self.running = False
            self.jumping = True
        elif userInput[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif not (self.jumping or userInput[pygame.K_DOWN]):
            self.ducking = False
            self.running = True
            self.jumping = False
 
    def duck(self):
        self.image = self.duckingSprite[self.steps // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.yDuck
        self.steps += 1
 
    def run(self):
        self.image = self.runningSprite[self.steps // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.steps += 1
 
    def jump(self):
        self.image = self.runningSprite[1]
        if self.jumping:
            self.dino_rect.y -= self.jumpVel * 4
            self.jumpVel -= 0.8
        if self.jumpVel < - self.jumpVelDefault:
            self.jumping = False
            self.jumpVel = self.jumpVelDefault
 
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cactus:
    def __init__(self):
        self.image = pygame.image.load("dinosaur/cactus.png")
        self.rect = self.image.get_rect()
        self.rect.x = screenWidth
 
    def update(self):
        self.rect.x -= gameSpeed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
 
    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    global gameSpeed, bgX, bgY, points, obstacles
    running = True
    clock = pygame.time.Clock()
    player = Dinosaurus()
    gameSpeed = 20
    bgX = 0
    bgY = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []

    def score():
        global points, gameSpeed
        points += 1
        if points % 100 == 0:
            gameSpeed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        screen.blit(text, textRect)

    def background():
        global bgX, bgY
        image_width = backgroundImage.get_width()
        screen.blit(backgroundImage, (bgX, bgY))
        screen.blit(backgroundImage, (image_width + bgX, bgY))
        if bgX <= -image_width:
            screen.blit(backgroundImage, (image_width + bgX, bgY))
            bgX = 0
        bgX -= gameSpeed

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)

        if len(obstacles) == 0:
            obstacles.append(Cactus())

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1

        background()
        score()

        clock.tick(30)
        pygame.display.update()

main()
