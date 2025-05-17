from PIL import Image
import colour_comparison

def nesify_image(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            original = pixels[x, y]
            pixels[x, y] = colour_comparison.nearest_n_colour(original)

    img.save(output_path)
    
if __name__ == "__main__":
    nesify_image('ar01.jpg', 'test.jpg')