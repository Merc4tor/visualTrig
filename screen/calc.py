from settings.settings import *

def calc_game_to_pixel_coords(x=None, y=None):
    if isinstance(x, tuple):
        if isinstance(x[0], (int, float)) and isinstance(x[1], (int, float)):
            return ( x[0] / simfieldsizex * (simFieldX2 - simFieldX1) + simFieldX1, (simfieldsizey- x[1]) / simfieldsizey * (simFieldY2 - simFieldY1) - simFieldY1)
    elif x != None:
        return  x / simfieldsizex * (simFieldX2 - simFieldX1) + simFieldX1
    elif y != None:
        return  (simfieldsizey - y) / simfieldsizey * (simFieldY2 - simFieldY1) - simFieldY1
    else:    
        print("did not put in a valid x, y or a coord in calc_game_to_pixel_coords()")
        
def calc_pixel_to_game_coords(x=None, y=None):
    if isinstance(x, tuple):
        if isinstance(x[0], (int, float)) and isinstance(x[1], (int, float)):
            return ((x[0] - simFieldX1) / (simFieldX2 - simFieldX1) * simfieldsizex, (simFieldY2 - x[1] - simFieldY1) / (simFieldY2 - simFieldY1) * simfieldsizey)
    elif x != None:
        return  (x - 10) / (simFieldX2 - simFieldX1) * simfieldsizex
    elif y != None:
        return  (simFieldY2 - y - simFieldY1) / (simFieldY2 - simFieldY1) * simfieldsizey
    else:    
        print("did not put in a valid x, y or a coord in calc_game_to_pixel_coords()")

#calculate text coords: [[xtop, ytop],[xend, yend]]
def calc_text_coords(text="test",centre=(100, 100), font=fontfreesan):
    size = font.size(text)
    return [[centre[0] - size[0] / 2, centre[1] - size[1] / 2], [centre[0] + size[0] / 2, centre[1] + size[1] / 2]]

def mouse_in_simfield(mousex, mousey):
    if mousex - simFieldX1 >= 0 and simFieldX2 - mousex >= 0:
        if mousey - simFieldY1 and simFieldY2 - mousey >= 0:
            return True
        else:
            return False
    else:
        return False
