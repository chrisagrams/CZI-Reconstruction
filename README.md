# CZI-Reconstruction
A series of scripts to extract the z-stack from a `.czi` file.

## Prerequisites
Python >= 3.9 installed on your machine.

Create a virual environment and install requirements:
```sh
python3 -m venv .venv/
pip install -r requirements.txt
```

## CZI-to-PNG
This script will extract the z-stack into individual `.png` files in greyscale and alpha channel.

### Usage
Run the script with:
``` sh
python czi_to_png_stack.py <INPUT_CZI_FILE> --output_directory=<OUTPUT_DIRECTORY>
```

#### Arguments
| Argument | Description | Default |
| -------- | ----------- | ------- | 
| `--output_directory` | Directory to output the `.png` stack to. | `out/` |
| `--channel` | Channel to extract. | `2` |
| `--dpi` | DPI for output image. | `100` |
| `--threshold` | Threshold value to cut off noise. Values below threshold will be transparent. | `20` |


## CZI-to-OBJ
This script will extract the z-stack into a `.obj` file. Each pixel in the `x,y` coordinate will be placed as a voxel in the 3D space in its z-index. To be used with 3D modeling software (eg. Blender) for further processing into a mesh.

### Usage
```sh
python czi_to_obj.py <INPUT_CZI_FILE> --output_file=<OUTPUT_FILE>
```

#### Arguments 
| Argument | Description | Default |
| -------- | ----------- | ------- |
| `--output_file` | Output filename (`.obj`) | `output.obj` |
| `--channel` | Channel to extract. | `2` |
| `--threshold` | Threshold value to cut off noise. Values below threshold will be transparent. | `20` |
| `--voxel_size` | Size of voxel in z-axis. | `0.1` |
