import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import bullet
import enemy
import supply
from random import *

pygame.init()
pygame.mixer.init()

bg_size=width,height=480,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战')

#背景图片  不透明不需要加alpha
background=pygame.image.load('images/background.png').convert()

#载入游戏音乐
pygame.mixer.music.load('sound/game_music.ogg')#bgm
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

enemy3_flying_sound=pygame.mixer.Sound('sound/enemy3_flying.wav')
enemy3_flying_sound.set_volume(0.2)

enemy1_down_sound=pygame.mixer.Sound('sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.1)

enemy2_down_sound=pygame.mixer.Sound('sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.2)

enemy3_down_sound=pygame.mixer.Sound('sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.5)

me_down_sound=pygame.mixer.Sound('sound/me_down.wav')
me_down_sound.set_volume(0.2)

def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
        
def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2=enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3=enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def main():
    pygame.mixer.music.play(-1)

    #生成我方飞机
    me=myplane.MyPlane(bg_size)
    
    #生成敌方飞机
    enemies=pygame.sprite.Group()
    #生成敌方小型飞机
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    #生成敌方中型飞机
    mid_enemies=pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    #生成敌方大型飞机
    big_enemies=pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)

    clock=pygame.time.Clock()

    #中弹图片索引
    e1_destroy_index=0
    e2_destroy_index=0
    e3_destroy_index=0
    my_destroy_index=0

    #切换图片
    switch_image=True

    #飞机尾气延时
    delay=100

    running=True

    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        #检测键盘操作
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()
        
        #绘制背景background   绘制代码不要随便变动代码位置  背景置底
        screen.blit(background,(0,0))

        #绘制敌方飞机 大型机
        for each in big_enemies:
            if each.active:
                each.move()
                if switch_image:
                    screen.blit(each.image1,each.rect)
                else:
                    screen.blit(each.image2,each.rect)
                #即将出现在画面中播放音效
                if each.rect.bottom>-50:
                    enemy3_flying_sound.play()
            else:
                #毁灭
                enemy3_down_sound.play()
                if not(delay%3):
                    screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                    e3_destroy_index=(e3_destroy_index+1)%6
                    if e3_destroy_index==0:
                        each.reset()
                    
        #绘制敌方飞机 中型机
        for each in mid_enemies:
            if each.active:
                each.move()
                screen.blit(each.image,each.rect)
            else:
                #毁灭
                enemy2_down_sound.play()
                if not(delay%3):
                    screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                    e2_destroy_index=(e2_destroy_index+1)%4
                    if e2_destroy_index==0:
                        each.reset()
        #绘制敌方飞机 小型机
        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image,each.rect)
            else:
                #毁灭
                enemy1_down_sound.play()
                if not(delay%3):
                    screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                    e1_destroy_index=(e1_destroy_index+1)%4
                    if e1_destroy_index==0:
                        each.reset()


        #检测我方飞机是否被撞
        enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
        if enemies_down:
           # me.active=False
            for e in enemies_down:
                e.active=False
                

        #绘制我方飞机
        if me.active:
            if switch_image:
                screen.blit(me.image1,me.rect)
            else:
                screen.blit(me.image2,me.rect)
        else:
            #毁灭
            me_down_sound.play()
            if not(delay%3):
                screen.blit(me.destroy_images[me_destory_index],me.rect)
                me_destroy_index=(me_destroy_index+1)%4
                if me_destroy_index==0:
                    print('Game Over')
                    running=False
        #切换图片
        if not (delay%5):
            switch_image=not switch_image
            
        delay-=1
        if not delay:
            delay=100

        

            


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
