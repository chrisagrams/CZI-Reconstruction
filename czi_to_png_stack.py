import os
from argparse import ArgumentParser
from czifile import imread
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


parser = ArgumentParser(description="Convert .czi file to PNG image stack.")
parser.add_argument("czi_file", help="Input .czi file.")
parser.add_argument("--output_directory", help="Directory to output to.", default="out/")
parser.add_argument("--channel", help="Channel to extract.", default=2)
parser.add_argument("--dpi", help="DPI for output image.", default=100)
parser.add_argument("--threshold", help="Theshold value to cut off noise.", default=20)
args = parser.parse_args()

# Disable interactive mode
plt.ioff()

if __name__ == __name__:
    print(f"Reading {args.czi_file}...")
    image = imread(args.czi_file)
    
    num_slices = image.shape[3]
    print(f"Number of slices: {num_slices}")

    img_height, img_width = image.shape[4], image.shape[5]
    print(f"Dimmensions: {img_height}x{img_width}")

    h_inches_size = img_height / args.dpi
    w_inches_size = img_width / args.dpi

    plt.figure(figsize=(h_inches_size, w_inches_size), dpi=args.dpi)

    os.makedirs(args.output_directory, exist_ok=True)

    for z_slice_index in tqdm(range(num_slices), desc="Processing slices"):
        slice_data = image[0, 0, args.channel, z_slice_index, :, :, 0]

        slice_data_normalized = (slice_data - slice_data.min()) / (slice_data.max() - slice_data.min()) * 255
        slice_data_normalized = slice_data_normalized.astype(np.uint8)

        rgba_image = np.zeros((slice_data_normalized.shape[0], slice_data_normalized.shape[1], 4), dtype=np.uint8)
        rgba_image[..., 0] = slice_data_normalized
        rgba_image[..., 1] = slice_data_normalized
        rgba_image[..., 2] = slice_data_normalized

        rgba_image[..., 3] = slice_data_normalized

        plt.imshow(rgba_image)
        plt.axis("off")
        plt.imsave(f"{args.output_directory}/{z_slice_index}.png", rgba_image)
        # plt.savefig(f"{args.output_directory}/{z_slice_index}.png", dpi=args.dpi, bbox_inches="tight", pad_inches=0)
        plt.close()