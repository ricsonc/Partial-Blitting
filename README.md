Partial-Blitting
================

Games written with the pygame library, (and in general) often blit dirty rectangles to the screen in order to update parts of the screen without changing others in order to improve performance.

This is especially important with pygame because updating the entire screen every frame causes unacceptably low frame-rate. Therefore 3d-games which must update the entire screen each frame are often impractical using pygame.

This code is a proof-of-concept of an algorithm which avoids this problem. The algorithm samples some points over the screen, and decides how much a particular area has changed. Then, it blits only the sections which have changed the most, resulting in increased frame-rate.
