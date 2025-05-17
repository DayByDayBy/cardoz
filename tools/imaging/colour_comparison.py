import math
import palette

def nearest_n_colour(rgb):
    r, g, b = rgb
    min_dist = float('inf')
    nearest_color = None
    for color in palette.N_PALETTE:
        cr, cg, cb = color
        dist = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        if dist < min_dist:
            min_dist = dist
            nearest_color = color
    return nearest_color

if __name__ == "__main__":
    pixel = (100, 1500, 200)
    closest = nearest_n_colour(pixel)
    print(f'closest: {closest}')