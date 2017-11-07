import pygame
import sys
import traceback
from pygame.locals import *

pygame.init()
pygame.mixer.init()

bg_size=width,height=480,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战')

#背景图片  不透明不需要加alpha
background=pygame.image.load('images/background.png').convert()

#载入游戏音乐
pygame.mixer.music.load('sound/ganme_music.ogg')#bgm
pygame.mixer.music.set_volume(0.2)#音乐大小

bullet_sound=pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)

bomb_sound=pygame.mixer.Sound('sound/use_bomb.wav')
bomb_sound.set_volume(0.2)

supply_sound=pygame.mixer.Sound('sound/supply.wav')
supply_sound.set_volume(0.2)

get_bomb_sound=pygame.mixer.Sound('sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)

get_bullet_sound=pygame.mixer.Sound('sound/get_bullet.wav')
get_bullet_sound.set_volume(0.2)

upgrade_sound=pygame.mixer.Sound('sound/upgrade.wav')
upgrade_sound.set_volume(0.2)

bullet_sound=pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)

def main():
    pygame.mixer.music.play(-1)

    clock=pygame.time.Clock()

    running=True

    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background,(0,0))

        pygame.display.flip()

        clock.tick(60)


if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
