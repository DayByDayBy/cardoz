import os
import glob
import card_straightener

def batch_process(input_dir, output_dir, padding=25):
    os.makedirs(output_dir, exist_ok=True)
    image_paths = glob.glob(os.path.join(input_dir, '*.jpg'))
    for img_path in image_paths:
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)
        card_straightener.straighten_and_crop(img_path, output_path, padding)
        

if __name__ == "__main__":
    
    input_dir = "image_dir"
    output_dir = "straightened_dir"
    batch_process(input_dir, output_dir)
