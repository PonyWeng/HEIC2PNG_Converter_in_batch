# HEIC2PNG_Converter_in_batch
A simple tool to help you batch convert HEIC images to PNG.

## Features
- Batch converts all `.heic` files in a folder to `.png`
- Adjustable output quality
- Original `.heic` files are preserved by default (deletion is opt-in)
- Auto-creates the output folder if it doesn't exist

## Requirements
- Python 3.7+
- [heic2png](https://pypi.org/project/heic2png/)

## Install requirement
```bash
pip install heic2png
```

## Project Structure
```
HEIC2PNG_Converter_in_batch/
├── HEIC2PNG_Converter.py
├── input_images/          # put your .heic files here
│   ├── IMG_0001.HEIC
│   └── IMG_0002.HEIC
└── output_images/         # converted .png files appear here (auto-created)
    ├── IMG_0001.png
    └── IMG_0002.png
```

## Usage

1. Clone or download this repository.
2. Create an `input_images` folder in the project directory (if it doesn't already exist) and place your `.heic` files inside it.
3. Run the script:

```bash
python HEIC2PNG_Converter.py
```

4. Converted `.png` files will be saved to `output_images`, which is created automatically if it doesn't exist.

## Configuration

| Option | Location | Default | Description |
|---|---|---|---|
| `input_folder` | bottom of script | `'input_images'` | Folder containing source `.heic` files |
| `output_folder` | bottom of script | `'output_images'` | Folder where `.png` files are saved |
| `quality` | `convert_and_delete_heic()` | `90` | Output PNG quality (0–100) |

## Deleting original files after conversion

By default, original `.heic` files are **kept**. If you want them deleted automatically after a successful conversion, uncomment this line inside `convert_and_delete_heic()`:

```python
# os.remove(heic_file_path)
```

⚠️ This is irreversible — make sure your PNGs are correct before enabling it.

## Example output

```
Start Converting...
Converted input_images/IMG_0001.HEIC, saved as output_images/IMG_0001.png
Converted input_images/IMG_0002.HEIC, saved as output_images/IMG_0002.png
```

## License
Feel free to use, modify, and share.

<br>

Good Luck 😆
