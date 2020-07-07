# 第一步，配置环境。
#
# 第二步，绘制窗口，监测键盘。

import pygame

from pygame.locals import *

import time


def start():
    # 1.创建一个窗口，用来显示内容

    screen = pygame.display.set_mode((480, 640), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景

    image_file_path = './feiji/background.png'

    background = pygame.image.load(image_file_path).convert()

    # 3.把背景图片放到窗口中显示

    while True:

        screen.blit(background, (0, 0))

        # 判断是否是点击了退出按钮

        for event in pygame.event.get():

            if event.type == QUIT:

                print("exit，退出")

                exit()

            elif event.type == KEYDOWN:

                if event.key == K_a or event.key == K_LEFT:

                    print('left，左移')

                elif event.key == K_d or event.key == K_RIGHT:

                    print('right，右移')

                elif event.key == K_SPACE:

                    print('space，开枪')

        # 通过延时的方式，从而降低了CPU占用率

        time.sleep(0.01)

        # 刷新屏幕

        pygame.display.update()


if __name__ == '__main__':
    start()

# 游戏编程思路：
#
# 使用pygame，初始化窗口。
#
# 设置图片，刷新到窗口。包括背景图片，游戏人物图片，敌人图片，场景图片。
#
# 监测动作事件。
#
# 循环刷新窗口。



#
#
# 第三步：定义子弹类
#
# 坐标，子弹类型，所在窗口，使用图片。
#
# 扩展：其他子弹类型，扩展子弹的飞行速度。子弹的威力等。

class PublicBullet(object):
    x = 0

    y = 0

    type_name = ""

    screen = None

    image = None

    def __init__(self, x, y, screen, type_name):

        self.screen = screen

        self.type_name = type_name

        if type_name == "hero":

            self.x = x + 40

            self.y = y - 20

            image_name = "./feiji/bullet-3.gif"



        elif type_name == "enemy":

            self.x = x + 30

            self.y = y + 30

            image_name = "./feiji/bullet-1.gif"

        self.image = pygame.image.load(image_name).convert()

    def move(self):

        if self.type_name == "hero":

            self.y -= 2

        elif self.type_name == "enemy":

            self.y += 2

    def display(self):

        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):

        if self.y > 890 or self.y < 0:

            return True

        else:

            return False

#
# 第四步：定义飞机类
#
# 坐标，飞机类型，所在窗口，使用图片，子弹列表（用于存储：坐标，消失，某个子弹击中等。）
#
# 初始化，移动，开枪

import pygame

from bullet import *

import random


class Plane(object):
    x = 0

    y = 0

    name = ""

    screen = None

    image = None

    image_name = ""

    bullet_list = []

    def __init__(self, screen, name):

        # 飞机的名称

        self.name = name

        # 设置要显示内容的窗口

        self.screen = screen

        self.image = pygame.image.load(self.image_name).convert()

        # 用来存储英雄飞机发射的所有子弹

        self.bullet_list = []

    def display(self):

        # 更新飞机的位置

        self.screen.blit(self.image, (self.x, self.y))

        # 用来存放需要删除的对象信息

        need_del_list = []

        # 保存需要删除的对象

        for item in self.bullet_list:

            if item.judge():
                need_del_list.append(item)

        # 删除bullet_list中需要删除的对象

        for del_item in need_del_list:
            self.bullet_list.remove(del_item)

        for bullet in self.bullet_list:
            bullet.display()

            bullet.move()

    def launch_bullet(self):

        new_bullet = PublicBullet(self.x, self.y, self.screen, self.name)

        self.bullet_list.append(new_bullet)


class HeroPlane(Plane):

    def __init__(self, screen, name):
        # 设置飞机默认的位置

        self.x = 230

        self.y = 600

        self.image_name = "./feiji/hero.gif"

        super().__init__(screen, name)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    # 

    # def move_up(self):

    #     self.y -= 10

    # 

    # def move_down(self):

    #     self.y += 10


class EnemyPlane(Plane):

    # 重写父类的__init_方法

    def __init__(self, screen, name):

        # 设置飞机默认的位置

        self.x = 0

        self.y = 0

        self.image_name = "./feiji/enemy-1.gif"

        # 调用父类的__init__方法

        super().__init__(screen, name)

        # 移动方向

        self.direction = "right"

    def move(self):

        # 如果碰到了右边的边界，那么就往左走，如果碰到了左边的边界，那么就往右走

        if self.direction == "right":

            self.x += 2

        elif self.direction == "left":

            self.x -= 2

        if self.x > 480 - 50:

            self.direction = "left"

        elif self.x < 0:

            self.direction = "right"

    def launch_bullet(self):

        number = random.randint(1, 100)  # 随机开枪

        if number == 88:
            super().launch_bullet()

#
# 需要完善的内容：
#
# 飞机移动，上下左右。
#
#
#




# 判断是否击毁飞机。增加飞机和子弹的坐标，高度宽度，结束可以调用爆炸画面。

for enmyblt in enemy_plane.bullet_list:

    if enmyblt.x > hero_plane.x and enmyblt.x < hero_plane.x + hero_plane.width and \
 \
            enmyblt.y > hero_plane.y and enmyblt.y < hero_plane.y + hero_plane.height:
        hero_plane.isdy = True

        print("game over!")

        # return

# 爆炸效果：

# 添加爆炸效果

self.bomb_image_list = []

self.__get_bomb_image()  # 加载爆炸图片

self.isbomb = False  # false没有爆炸，True爆炸

self.image_num = 0  # 显示过的图片数

self.image_index = 0  # 显示图片的下标变化


def bomb(self, isbomb):
    self.isbomb = isbomb


# 加载爆炸图片

def __get_bomb_image(self):
    for i in range(1, 4):
        im_path = 'feiji/enemy0_down' + str(i) + '.png'

        self.bomb_image_list.append(pygame.image.load(im_path))

    # 总数有多少张

    self.image_length = len(self.bomb_image_list)


def display(self):
    # 判断是否要爆炸

    if self.isbomb:

        bomb_image = self.bomb_image_list[self.image_index]

        self.screen.blit(bomb_image, (self.x, self.y))

        self.image_num += 1

        if self.image_num == (self.image_length + 1):

            self.image_num = 0

            self.image_index += 1

            if self.image_index > (self.image_length - 1):
                self.image_index = 5

                time.sleep(2)

                exit()

