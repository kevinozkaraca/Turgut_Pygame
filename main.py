# coding UTF-8

# Librairies utilisées
import time
import pygame
pygame.init()
pygame.mixer.init()

# Variables pour detecter les mouvements et les actions

anim_move_up = False
anim_move_down = False
anim_move_left = False
anim_move_right = False
anim_move_axe = False
axe_launched = False
is_playing = False
moves = 0
player_velocity = 8

# Tuple de toutes les images de TURGUT alias player

imagesOfTurgut = [pygame.image.load("turgutAnimDown1.png"), pygame.image.load("turgutAnimDown2.png"), pygame.image.load("turgutAnimDownShield1.png"), pygame.image.load("turgutAnimDownShield2.png"), pygame.image.load("turgutAnimDownShieldDownStay.png"), pygame.image.load("turgutAnimDownStay.png"), pygame.image.load("turgutAnimLeft1.png"), pygame.image.load("turgutAnimLeft2.png"), pygame.image.load("turgutAnimLeftShield1.png"), pygame.image.load("turgutAnimLeftShield2.png"), pygame.image.load("turgutAnimLeftShieldStay.png"), pygame.image.load("turgutAnimLeftStay.png"), pygame.image.load("turgutAnimRight1.png"), pygame.image.load("turgutAnimRight2.png"), pygame.image.load("turgutAnimRightShield1.png"), pygame.image.load("turgutAnimRightShield2.png"), pygame.image.load(
    "turgutAnimRightShieldStay.png"), pygame.image.load("turgutAnimRightStay.png"), pygame.image.load("turgutAnimUp1.png"), pygame.image.load("turgutAnimUp2.png"), pygame.image.load("turgutAnimUpShield1.png"), pygame.image.load("turgutAnimUpShield2.png"), pygame.image.load("turgutAnimUpShieldStay.png"), pygame.image.load("turgutAnimUpStay.png"), pygame.image.load("turgutAttackDown.png"), pygame.image.load("turgutAttackLeft.png"), pygame.image.load("turgutAttackRight.png"), pygame.image.load("turgutAttackUp.png"), pygame.image.load("turgutDie.png"), pygame.image.load("turgutHitDown.png"), pygame.image.load("turgutHitLeft.png"), pygame.image.load("turgutHitRight.png"), pygame.image.load("turgutHitUp.png"), pygame.image.load("turgutWin.png")]

'''Liste des images :
0 à 5.......Down

0 	turgutAnimDown1.png                                                  
1 	turgutAnimDown2.png                                                  
2 	turgutAnimDownShield1.png                                            
3 	turgutAnimDownShield2.png                                            
4 	turgutAnimDownShieldDownStay.png                                     
5 	turgutAnimDownStay.png                                               

6 à 11......Left

6 	turgutAnimLeft1.png                                                  
7 	turgutAnimLeft2.png                                                  
8 	turgutAnimLeftShield1.png                                            
9 	turgutAnimLeftShield2.png                                            
10	turgutAnimLeftShieldStay.png                                         
11	turgutAnimLeftStay.png                                               

12 à 17.....Right

12	turgutAnimRight1.png                                                 
13	turgutAnimRight2.png                                                 
14	turgutAnimRightShield1.png                                           
15	turgutAnimRightShield2.png                                           
16	turgutAnimRightShieldStay.png                                        
17	turgutAnimRightStay.png                                              

18 à 23.....Up

18	turgutAnimUp1.png                                                    
19	turgutAnimUp2.png                                                    
20	turgutAnimUpShield1.png                                              
21	turgutAnimUpShield2.png                                              
22	turgutAnimUpShieldStay.png                                           
23	turgutAnimUpStay.png                                                 

24 à 27.....Attack

24	turgutAttackDown.png                                                 
25	turgutAttackLeft.png                                                 
26	turgutAttackRight.png                                                
27	turgutAttackUp.png                                                   

28..........Die

28	turgutDie.png  

29 à 32.....Hit      
                                   
29	turgutHitDown.png                                                    
30	turgutHitLeft.png                                                    
31	turgutHitRight.png                                                   
32	turgutHitUp.png                                                      
 
33..........Win
33	turgutWin.png   '''

# icone du programme
programIcon = pygame.image.load('kayiobasi.png')
pygame.display.set_icon(programIcon)

# Création de la hache LEFT et ses caracteristiques


class Axe_left(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = -3
        self.image = pygame.image.load("axe1.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        '#place de la hache à sa sortie (rajouté + apres x ou y pour améliorer'
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 4
        self.image = pygame.transform.rotozoom(
            self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_axes.remove(self)
        self.axe_reload()

    def axe_reload(self):
        global axe_launched
        axe_launched = False
        global game
        global player
        game.player.velocity = player_velocity
        game.player.image = pygame.transform.scale(imagesOfTurgut[6], (50, 50))

    def move(self):
        global moves
        moves += 1
        self.rect.x += self.velocity
        self.rotate()
        print("left")
        if self.rect.x < -1280:
            self.remove()
            print("supprimé")

# Création de la hache RIGHT et ses caracteristiques


class Axe_right(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load("axe2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        '# place de la hache à sa sortie (rajouté + apres x ou y pour améliorer'
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += -4
        self.image = pygame.transform.rotozoom(
            self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_axes.remove(self)
        self.axe_reload()

    def axe_reload(self):
        global axe_launched
        axe_launched = False
        global game
        game.player.velocity = player_velocity
        game.player.image = pygame.transform.scale(
            imagesOfTurgut[12], (50, 50))

    def move(self):
        global moves
        moves += 1
        self.rect.x += self.velocity
        self.rotate()
        print("right")
        if self.rect.x > 1280:
            self.remove()
            print("supprimé")


# Création de la hache UP et ses caracteristiques

class Axe_up(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = -3
        self.image = pygame.image.load("axe1.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        '# place de la hache à sa sortie (rajouté + apres x ou y pour améliorer'
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 4
        self.image = pygame.transform.rotozoom(
            self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_axes.remove(self)
        self.axe_reload()

    def axe_reload(self):
        global axe_launched
        axe_launched = False
        global game
        global player
        game.player.velocity = player_velocity
        game.player.image = pygame.transform.scale(
            imagesOfTurgut[18], (50, 50))

    def move(self):
        global moves
        moves += 1
        self.rect.y += self.velocity
        self.rotate()
        print("up")
        if self.rect.y < -1280:
            self.remove()
            print("supprimé")

# Création de la hache DOWN et ses caracteristiques


class Axe_down(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load("axe2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        '# place de la hache à sa sortie (rajouté + apres x ou y pour améliorer'
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += -4
        self.image = pygame.transform.rotozoom(
            self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_axes.remove(self)
        self.axe_reload()

    def axe_reload(self):
        global axe_launched
        axe_launched = False
        global game
        global player
        game.player.velocity = player_velocity
        game.player.image = pygame.transform.scale(imagesOfTurgut[0], (50, 50))

    def move(self):
        self.rect.y += self.velocity
        self.rotate()
        print("down")
        if self.rect.y > 1280:
            self.remove()
            print("supprimé")

# Création du joueur et déplacements


class TURGUT(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_axes = pygame.sprite.Group()
        self.velocity = 6
        self.image = imagesOfTurgut[13]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 500

    def launch_axe_up(self):
        self.all_axes.add(Axe_up(self))
        global anim_move_up
        anim_move_up = False
        global anim_move_down
        anim_move_up = False
        global anim_move_left
        anim_move_up = False
        global anim_move_right
        anim_move_up = False

    def launch_axe_left(self):
        self.all_axes.add(Axe_left(self))
        global anim_move_up
        anim_move_up = False
        global anim_move_down
        anim_move_up = False
        global anim_move_left
        anim_move_up = False
        global anim_move_right
        anim_move_up = False

    def launch_axe_right(self):
        self.all_axes.add(Axe_right(self))
        global anim_move_up
        anim_move_up = False
        global anim_move_down
        anim_move_up = False
        global anim_move_left
        anim_move_up = False
        global anim_move_right
        anim_move_up = False

    def launch_axe_down(self):
        self.all_axes.add(Axe_down(self))
        global anim_move_up
        anim_move_up = False
        global anim_move_down
        anim_move_up = False
        global anim_move_left
        anim_move_up = False
        global anim_move_right
        anim_move_up = False

    # Deplacements

    def move_right(self):
        global player
        global game
        global moves
        self.rect.x += self.velocity
        game.player.image = pygame.transform.scale(
            imagesOfTurgut[12], (50, 50))
        if moves > 5:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[13], (50, 50))
            if moves > 10:
                game.player.image = pygame.transform.scale(
                    imagesOfTurgut[12], (50, 50))
                moves = 0

    def move_left(self):
        global player
        global game
        global moves
        self.rect.x -= self.velocity
        self.image = pygame.transform.scale(imagesOfTurgut[6], (50, 50))
        if moves > 5:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[7], (50, 50))
            if moves > 10:
                game.player.image = pygame.transform.scale(
                    imagesOfTurgut[6], (50, 50))
                moves = 0

    def move_up(self):
        global player
        global game
        global moves
        self.rect.y -= self.velocity
        self.image = pygame.transform.scale(imagesOfTurgut[18], (50, 50))
        if moves > 5:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[19], (50, 50))
            if moves > 10:
                game.player.image = pygame.transform.scale(
                    imagesOfTurgut[18], (50, 50))
                moves = 0

    def move_down(self):
        global player
        global game
        global moves
        self.rect.y += self.velocity
        self.image = pygame.transform.scale(imagesOfTurgut[0], (50, 50))
        if moves > 5:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[1], (50, 50))
            if moves > 10:
                game.player.image = pygame.transform.scale(
                    imagesOfTurgut[0], (50, 50))
                moves = 0

# Creation du jeu


class Game:
    def __init__(self):
        global is_playing
        self.is_playing = False
        self.player = TURGUT()
        self.pressed = {}

    def music_play(self):
        global game
        BMGinGame = pygame.mixer.Sound('son01.ogg')
        BMGinGame.play(loops=-1)
        BMGinGame.set_volume(0.4)

    def update(self):
        global timing_start
        global game
        global moves
        global axe_launched
        global anim_move_right
        global anim_move_left
        global anim_move_up
        global anim_move_down
        global backgrounds
        global clock
        clock.tick(100)
        timing_start = 0
        screen.blit(pygame.transform.scale(
            backgrounds[2], (8000, 2618)), (0, 0))
        screen.blit(game.player.image, game.player.rect)
        '#Affichage de la hache'
        for axe_up in game.player.all_axes:
            axe_up.move()
        for axe_down in game.player.all_axes:
            axe_down.move()
        for axe_left in game.player.all_axes:
            axe_left.move()
        for axe_right in game.player.all_axes:
            axe_right.move()
        game.player.all_axes.draw(screen)
        pygame.display.flip()

        '#Deplacements et actions liés à RIGHT'
        if game.pressed.get(pygame.K_RIGHT) and axe_launched == False:
            game.player.velocity = player_velocity
            game.player.move_right()
            anim_move_up = False
            anim_move_down = False
            anim_move_left = False
            anim_move_right = True
            moves += 1
        if game.pressed.get(pygame.K_x) and anim_move_right == True and axe_launched == False:
            axe_launched = True
            moves += 1
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[26], (50, 50))
            '#La fonction launch_axe... appelle remove et reload qui remet axe_launched = False'
            soundAxeLaunch.play()
            game.player.launch_axe_right()
        if axe_launched == True and anim_move_right == True:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[26], (50, 50))
            game.player.velocity = 0

        '#Deplacements et actions liés à LEFT'
        if game.pressed.get(pygame.K_LEFT) and axe_launched == False:
            game.player.velocity = player_velocity
            game.player.move_left()
            anim_move_up = False
            anim_move_down = False
            anim_move_left = True
            anim_move_right = False
            moves += 1
        if game.pressed.get(pygame.K_x) and anim_move_left == True and axe_launched == False:
            axe_launched = True
            moves += 1
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[25], (50, 50))
            '#La fonction launch_axe... appelle remove et reload qui remet axe_launched = False'
            soundAxeLaunch.play()
            game.player.launch_axe_left()
        if axe_launched == True and anim_move_left == True:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[25], (50, 50))
            game.player.velocity = 0

        '#Deplacements et actions liés à UP'
        if game.pressed.get(pygame.K_UP) and axe_launched == False:
            game.player.velocity = player_velocity
            game.player.move_up()
            anim_move_up = True
            anim_move_down = False
            anim_move_left = False
            anim_move_right = False
            moves += 1
        if game.pressed.get(pygame.K_x) and anim_move_up == True and axe_launched == False:
            axe_launched = True
            moves += 1
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[27], (50, 50))
            '#La fonction launch_axe... appelle remove et reload qui remet axe_launched = False'
            soundAxeLaunch.play()
            game.player.launch_axe_up()
        if axe_launched == True and anim_move_up == True:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[27], (50, 50))
            game.player.velocity = 0

        '#Deplacements et actions liés à DOWN'
        if game.pressed.get(pygame.K_DOWN) and axe_launched == False:
            game.player.velocity = player_velocity
            game.player.move_down()
            anim_move_up = False
            anim_move_down = True
            anim_move_left = False
            anim_move_right = False
            moves += 1
        if game.pressed.get(pygame.K_x) and anim_move_down == True and axe_launched == False:
            axe_launched = True
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[24], (50, 50))
            '#La fonction launch_axe... appelle remove et reload qui remet axe_launched = False'
            soundAxeLaunch.play()
            game.player.launch_axe_down()
        if axe_launched == True and anim_move_down == True:
            game.player.image = pygame.transform.scale(
                imagesOfTurgut[24], (50, 50))
            game.player.velocity = 0

        '#Empecher les déplacements en diagonale -- A REVOIR'
        if game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_UP):
            game.player.velocity = 0
        if game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_UP):
            game.player.velocity = 0
        if game.pressed.get(pygame.K_DOWN) and game.pressed.get(pygame.K_UP):
            game.player.velocity = 0
        if game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_DOWN):
            game.player.velocity = 0
        if game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_DOWN):
            game.player.velocity = 0
        if game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_RIGHT):
            game.player.velocity = 0


game = Game()
# Generer la fenetre du jeu

pygame.display.set_caption("The legend of Turgut")

# Rajouter set_mode((1280,720),pygame.FULLSCREEN) plus tard

screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Images de fond du jeu -- A CHANGER

backgrounds = (pygame.image.load("ecran_Titre1test.jpg"), pygame.image.load(
    "ecran_Tritre2.jpg"), pygame.image.load("Maprevu.png"))

# Timing du début de jeu et screen avant le lancement

timing_start = 5
soundStart = pygame.mixer.Sound('soundStart.wav')
soundAxeLaunch = pygame.mixer.Sound('soundAxeLaunch.wav')

'''
#Musique du jeu METTRE -- soundAxeLaunch.play() -- dans le code apres
soundAxeLaunch = pygame.mixer.Sound('soundAxeLaunch.mp3')
BMGingame = pygame.mixer.Sound('BMGingame.mp3')
STARTsound = pygame.mixer.Sound('BMGingame.mp3')
'''


# Generer le joueur dans le jeu

player = TURGUT()

# Boucle du jeu et de la fenetre fixation des FPS

running = True
clock = pygame.time.Clock()

while running:
    '#Condition de départ pour le jeu'
    pygame.display.flip()
    if game.is_playing == False and timing_start == 5:
        screen.blit(backgrounds[0], (0, 0))
    if game.pressed.get(pygame.K_s) and timing_start > 4:
        soundStart.play(loops=0)
        while timing_start < 15 and timing_start > 4:
            timing_start += 1
            print(timing_start)
            screen.blit(backgrounds[1], (0, 0))
            pygame.display.flip()
            if timing_start > 14:
                time.sleep(5)
                game.is_playing = True
                game.music_play()
    if game.is_playing:
        # Le lancement du jeu remet le timing_start à 0
        game.update()

    # Touches evenements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if game.pressed.get(pygame.K_ESCAPE):
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False
