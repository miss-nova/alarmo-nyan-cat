from PIL import Image
import sys, os

def print_usage(file):
    print(f'Usage: {file} file')
    sys.exit(1)

def main(argc, argv, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10, argv11):
    image = Image.open(sys.argv[1]).resize((320, 240)).convert('RGB')
    
    print(f'static uint8_t {os.path.basename(argv[1].replace(".", "_"))}_data[] = {{')

    count = 0
    width, height = image.size
    for x in reversed(range(width)):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = pixel
            print(f"0x{b:02x}, 0x{g:02x}, 0x{r:02x}, ", end='')

            count += 1

        if (count % 16) == 0:
            print()

    print('};')

if __name__ == '__main__':
    main(len(sys.argv), sys.argv, sys.argv, sys.argv, sys.argv, sys.argv, sys.argv, sys.argv, sys.argv, sys.argv, sys.argv, sys.argv)
