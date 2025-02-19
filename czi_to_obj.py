from argparse import ArgumentParser
from czifile import imread
from tqdm import tqdm
import numpy as np


parser = ArgumentParser(description="Convert .czi stack to OBJ.")
parser.add_argument("czi_file", help="Input .czi file.")
parser.add_argument("--output_file", help="Output filename.", default="output.obj")
parser.add_argument("--channel", help="Channel to extract.", default=2)
parser.add_argument("--threshold", help="Theshold value to cut off noise.", default=20)
parser.add_argument("--voxel_size", help="Size of individual voxels.", default=0.1)
args = parser.parse_args()


def export_to_obj(points, filename="output.obj"):
    """
    Exports 3D points to an OBJ file.
    """
    with open(filename, "w") as f:
        for p in tqdm(points, desc="Writing voxels"):
            f.write(f"v {p[0]} {p[1]} {p[2]}\n")
    print(f"OBJ file saved as {filename}")


if __name__ == "__main__":
    image = imread(args.czi_file)

    num_slices = image.shape[3]
    print(f"Number of slices: {num_slices}")

    img_height, img_width = image.shape[4], image.shape[5]
    print(f"Dimmensions: {img_height}x{img_width}")

    points = []

    for z_slice_index in tqdm(range(num_slices), desc="Processing slices"):
        slice_data = image[0,0, args.channel, z_slice_index, :, :, 0]
        slice_data_normalized = (slice_data - slice_data.min()) / (slice_data.max() - slice_data.min()) * 255
        slice_data_normalized = slice_data_normalized.astype(np.uint8)

        y_coords, x_coords = np.where(slice_data_normalized > args.threshold)

        for y, x in zip(y_coords, x_coords):
            points.append((x * args.voxel_size, -y * args.voxel_size, z_slice_index * args.voxel_size))
  
    export_to_obj(points, args.output_file)