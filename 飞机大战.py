import pygame

# 初始
print(pygame.ver)
pygame.init()

# 游戏代码
#创建游戏窗口
main_screen = pygame.display.set_mode((480,700))

# 绘制背景
bg = pygame.image.load("./images/background.png")
main_screen.blit(bg,(0, 0))

#加载英雄飞机
hero_plane = pygame.image.load("./images/pangci.png")
main_screen.blit(hero_plane, (200,500))

# 刷新屏幕
pygame.display.update()

# 创建时钟对象

clock = pygame.time.Clock()

# 定义rect记录飞机的位置
hero_rect = pygame.Rect(200, 500, 102, 126)
mouse_x, mouse_y = (0, 0)

# 设定鼠标
# pygame.mouse.set_visible(False)

# 游戏循环

while True:
    clock.tick(60)
    # 获得事件列表
    event_list = pygame.event.get()
    # 获得坐标

    # print(mouse_x)
    # print(mouse_y)

    if len(event_list) > 0:
        print(event_list)
    # 监听
    for event in event_list:
        # 游戏结束按钮
        if event.type == pygame.QUIT:
            print("游戏结束")
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos


    # 修改英雄的位置
    hero_rect.y = mouse_y - 63
    hero_rect.x = mouse_x - 51
    # if hero_rect.bottom < 0:
    #     hero_rect.y = 700
    # 调用blit写内存
    main_screen.blit(bg, (0, 0))
    main_screen.blit(hero_plane,hero_rect)
    # 刷新屏幕
    pygame.display.update()



# 释放内存
# pygame.quit()
