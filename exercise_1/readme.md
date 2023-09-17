# Exercise 1 - Rgb Hello World 
### Seasons through a Tree

**Concept:**

Since the exercise is about demonstrating a story with just one pixel, my plan was to depict a cycle of some sort. Initially, my idea was to showcase the phases of the moon using shadow (by placing a cardboard cutout) and adjusting brightness. However, I soon realized that it's more about the position of the LED than the shadow.
Then, I came up with the idea of portraying the seasonal changes in tree leaves, with spring, summer, autumn, and winter seasons. The colours I used were as follows:
Spring: Bright pink (cherry blossom; light pink was too faint)
Summer: Bright green
Autumn: Warm orange
Winter: Snow white.
I understand that trees rejuvenate, but this particular tree's lifespan only extends until winter, so there's no looping involved in the code.

**Code:**

Here's a snippet of my code:

    # Cherry Blossom (Bright Pink to Dark Green)
        for i in range(speed):
            r = int(255 - (i * 10))
            g = int(0 + (i * 5))  # these numbers are trial for ex 7 was too much 
            b = int(80 - (i * 4)) # and less than 4 (blue) was less so g settled w 5 (6 is ok too)
            led[0] = (r, g, b)   
            time.sleep(speed / 10) 
        
        # Summer (Dark Green to Warm Orange)
        # (0,128,0) is bright green what i tried to achieve in prev loop- works well with speed =20
        for i in range(speed):
            r = int(0 + (i * 12))  # trial, 10 was less 12 felt nice 15 was too quick
            g = int(128 + (i * 2))
            b = int(0)
            led[0] = (r, g, b)
            time.sleep(speed / 10)`

In this section, I begin with bright pink (with no hint of green) and transition toward bright green. The speed varies; for demonstration purposes, I chose a value of 10, but for a smoother transition, 20 is ideal as it's somewhat calculated. I attempted to approximate the RGB value at the end of the 20-loop cycle. Then, we initiate another loop starting with bright green (0, 128, 0) and transitioning toward the autumn colour. The values added and subtracted from the RGB were determined through trial and error. For instance, in the line "r = int(0 + (i * 12))," 10 represented a slower increase, 12 felt more appropriate, and 15 was too rapid in transitioning to the other colour. I repeated the same pattern for other seasons. 

**Reflection:**

I believe the code could benefit from additional calculations to achieve a smoother transition. I felt that 30 seconds was too short, but perhaps I could achieve a better and faster transition by further experimenting with the sleep and speed values.


