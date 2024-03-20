import pygame
class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始值"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.speed = ai_game.settings.ship_speed

        # 加载飞船图形并获取其外接矩形
        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放置在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x, y中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)