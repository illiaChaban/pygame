# Tanks

My attempt to build modern tanks with old pygame.

## Whatch demo:
<a href="https://www.youtube.com/watch?v=zgsTj9R55g0">
  <img src="https://user-images.githubusercontent.com/34459770/40556781-f242539e-601b-11e8-80b2-c86b3700243c.png"
    height="150"/>
</a>

## Screnshots:

<div>
  <img width="250" alt="sc1" src="https://user-images.githubusercontent.com/34459770/40556945-74c67156-601c-11e8-8dac-edf1eec5748e.png">
  <img width="250" alt="sc2" src="https://user-images.githubusercontent.com/34459770/40556947-75da2592-601c-11e8-8d6e-b1f8f90c1867.png">
</div>


After dealing with pygame, I consider myself overqualified for Google Maps. 

## Challenges:

    DANGER: A LOT OF MATHS INVOLVING COS, SIN ANG TRIGONOMETRY FORMULAS

    Most of the time working on this game was spent outside the laptop, 
    trying to remember trigonometry and geometry formulas from school
    and correlating them to pygame coordinate system. 
    (which made my brain hurt,
    still does)


    - rotaing: 
        - rotating in pygame is happening not about center, but relative to top 
        left corner of the rectangle the image is in. While the image is rotating,
        its rectangle is changing its size. To make it look like the image rotates about
        its center you have to change the coordinates of the top left corner of the
        image. 
        It's hard to read, it was even harder to code.
        It was probably the most challenging part of the project.

        - finding center of bottom image to put the tank top in

        - tring to change the relative center of tank top -- the point the top is 
        rotating about
    
        - finding exact spots where some of theimages should appear (like fire out 
        of the turret when the tank shoots)

        - shooting shells involved rotating too. Despite already having code that 
        handled this kind of stuff quite good, the amount of small bugs accumulated 
        by that time and some inattention made this task increadibly hard.
        It forced me to review my code a couple of hundred of times and do some major
        refactoring

        
    - time:    
        - creating time in the game, so that images (like explisions) can render
        depending on that time

    - collision:
        - finding the tank area depending on its corners and checking if the point
        lies inside that area. Pygame coordinate system made this task even harder.

    

## Code snippets: 
```Python

    def move_tank_bottom(self, list_of_objects):
        radians = self.bottom_angle * math.pi / 180
        add_x = math.cos(radians) * self.speed
        add_y = math.sin(radians) * self.speed

        new_bottom_angle = self.bottom_angle + self.turn_speed 
        new_x = self.x + add_x
        new_y = self.y - add_y

        if self.detect_collision(list_of_objects, self.find_corners(new_bottom_angle, new_x, new_y, self.width, self.height)):
            new_x = self.x + add_x/2 
            new_y = self.y - add_y/2
            new_bottom_angle = self.bottom_angle + self.turn_speed/2
        if not self.detect_collision(list_of_objects, self.find_corners(new_bottom_angle, self.x, self.y, self.width, self.height) ):
            self.bottom_angle = new_bottom_angle
        if not self.detect_collision(list_of_objects, self.find_corners(self.bottom_angle, new_x, self.y, self.width, self.height) ):
            self.x = new_x
        if not self.detect_collision(list_of_objects, self.find_corners(self.bottom_angle, self.x, new_y, self.width, self.height) ):
            self.y = new_y
            
            
    def point_within_my_area(self, point_coordinates, corners_list):
        #x1,y1###############x2,y2#
        #                         #
        #                         #
        #x4,y4###############x3,y3#

        ## straight (line) formula =>  ax + bx + c = 0  
        ##  or   (y1 -y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0
        x = point_coordinates[0]
        y = point_coordinates[1]

        for i in range(len(corners_list)):
            x1 = corners_list[i][0]
            y1 = corners_list[i][1]

            next_i = (i + 1) % (len(corners_list))
            x2 = corners_list[next_i][0]
            y2 = corners_list[next_i][1]

            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1

            if a * x + b * y + c < 0:  ## checking if the point lies on the right side 
                return False           ## of every line, which would mean it's inside
        return True                    ## the area

    def detect_collision(self, list_of_objects, my_corners_list):
        for obj in list_of_objects:
            if obj != self:
                if self.it_within_my_area(obj, my_corners_list) or self.me_within_its_area(obj, my_corners_list ):
                    return True
        return False
 ```
 
 
All in all, even though there were probably thousands of libraries better suited
for game developing at that point, I'm incredibly glad I encountered all of those
challenges and were able to persevere.

Of course, I wouldn't be able to do this by myself, especially at the start, when this
huge pile of problems seemed to be impossible to solve. For guidence and assistence,
I'd like to thank all of my mentors and especially Jonathan Martin @nybblr.
