radians_top = self.top_angle * math.pi / 180
        change_x = math.cos(radians_top) * (15)   #8 pixels - how far back i want to put the tank top
        change_y = math.sin(radians_top) * (15)
        top_x = self.x - change_x
        top_y = self.x + change_y
        #optimize
        x2 = pygame.mouse.get_pos()[0]
        y2 = pygame.mouse.get_pos()[1]
        centered_x = top_x
        centered_y = top_y

        #finding angle between mouse and tank
        dx = x2 - centered_x
        dy = y2 - centered_y
        rads = math.atan2(-dy, dx) % (2* math.pi)
        angle = math.degrees(rads)
        self.top_angle = angle

        # changing the center while rotating 
        copied_top = self.image_top.copy()
        copied_top = pygame.transform.rotate(copied_top, self.top_angle)
        width_top = copied_top.get_rect()[2] - change_x
        height_top = copied_top.get_rect()[3] + change_y
        change_coo_x_top = (width_top - self.rect[2]) / 2
        change_coo_y_top = (height_top - self.rect[3]) / 2