"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Dylan Frazee.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 15)
red_turtle.speed = 1

yellow_turtle = rg.SimpleTurtle('turtle')
yellow_turtle.pen = rg.Pen('yellow', 15)
yellow_turtle.speed = 1

for k in range(2):
    red_turtle.forward(100)
    red_turtle.right(120)
red_turtle.forward(105)
red_turtle.pen = rg.Pen('green', 15)
red_turtle.forward(95)
red_turtle.left(120)
for p in range(2):
    red_turtle.left(120)
    red_turtle.forward(100)

for z in range(2):
    yellow_turtle.backward(100)
    yellow_turtle.left(120)
yellow_turtle.backward(105)
yellow_turtle.pen = rg.Pen('purple', 15)
yellow_turtle.backward(95)
yellow_turtle.right(60)
yellow_turtle.forward(100)
yellow_turtle.right(120)
yellow_turtle.forward(100)

window.close_on_mouse_click()
