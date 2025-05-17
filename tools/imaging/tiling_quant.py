from PIL import Image
import numpy as np
import colour_comparison  

TILE_SIZE = 8
NUM_COLORS_PER_TILE = 4

def get_tile(img_array, x, y):
    return img_array[y:y+TILE_SIZE, x:x+TILE_SIZE]

def nes_palette_tile_quantize(tile):
    
    # flattening tile to list of RGB tuples:
    flat_pixels = tile.reshape(-1, 3)
    
    # then:
    n_mapped = [colour_comparison.nearest_n_colour(tuple(p)) for p in flat_pixels]
    
    # counting most common n_mapped colors in this tile 
    unique, counts = np.unique(n_mapped, axis=0, return_counts=True)
    sorted_indices = np.argsort(-counts)  # descending by frequency
    tile_palette = [tuple(unique[i]) for i in sorted_indices[:NUM_COLORS_PER_TILE]]
    
    # remap tile pixels to one tile_palette colors
    remapped = [
        min(tile_palette, key=lambda c: np.sum((np.array(p, dtype=int) - np.array(c, dtype=int))**2))
        for p in n_mapped
    ]
    
    return np.array(remapped, dtype=np.uint8).reshape(tile.shape)

def nesify_image_by_tile(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    np_img = np.array(img)
    h, w, _ = np_img.shape

    # make sure dimensions are divisible by tile size
    h = h - (h % TILE_SIZE)
    w = w - (w % TILE_SIZE)
    np_img = np_img[:h, :w]
    
    output_img = np.zeros_like(np_img)

    for y in range(0, h, TILE_SIZE):
        for x in range(0, w, TILE_SIZE):
            tile = get_tile(np_img, x, y)
            quantized_tile = nes_palette_tile_quantize(tile)
            output_img[y:y+TILE_SIZE, x:x+TILE_SIZE] = quantized_tile

    Image.fromarray(output_img).save(output_path)

if __name__ == "__main__":
    nesify_image_by_tile("ar01.jpg", "nes_tiles.jpg")