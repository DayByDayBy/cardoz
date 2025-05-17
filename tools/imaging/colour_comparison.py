
import numpy as np
import palette

def nearest_n_colour(rgb):
    r, g, b = rgb
    min_dist = float('inf')
    nearest_color = None
    for color in palette.N_PALETTE:
        cr, cg, cb = color
        dist = np.linalg.norm(
            np.array([r, g, b], 
                     dtype=int) - 
            np.array([cr, cg, cb], 
                     dtype=int))  
        if dist < min_dist:
            min_dist = dist
            nearest_color = color
    return nearest_color

if __name__ == "__main__":
    pixel = (100, 1500, 200)
    closest = nearest_n_colour(pixel)
    print(f'closest: {closest}')
    
    
    
    
    
# old/alt way of doing dist:
#     # import math
#         # dist = math.sqrt((int(r) - int(cr))**2 + 
#         #                  (int(g) - int(cg))**2 + 
#         #                  (int(b) - int(cb))**2)