import pygame

pygame.init()
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄飞机 %d,%d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d " % (hero_rect.width, hero_rect.height))
print("英雄的size %d %d" % hero_rect.size)

