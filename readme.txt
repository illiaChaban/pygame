Challenges:

    DANGER: A LOT OF MATHS INVOLVING COS, SIN ANG TRIGONOMETRY FORMULAS

    Most of the time working on this game was spent outside the laptop, 
    trying to remember trigonometry and geometry formulas from school
    and correlating them to pygame coordinate system. 
    (which made my brain hurt,
    still does)


    - rotaing: 
        - old library ==> rotates not about center, but about top left corner,
        while changing sizes of rectangle the image is in

        - finding center to put the tank top in

        - tring to change the ralative center of tank top -- the point top is 
        rotating about
    
        - finding exact spots where images should appear (like fire out of the turret
        when you shoot)

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

    

All in all, even though there were probably thousands of libraries better suited
for game developing at that point, I'm incredibly glad I encountered all of those
challenges and were able to persevere.

Of course, I wouldn't be able to do this by myself, especially at the start, when this
huge pile of problems seemed to be impossible to solve. For guidence and assistence,
I'd like to thank all of my mentors and especially Jonathan Martin @nybblr.

After all the challenges in pygame, I believe I'm overqualified for Google Maps. 