from PIL import Image

with open('_61563_5_83fa8e4885b8d494619ba2722d8099b0.jpg', 'rb') as fil:
    byte = fil.read()
print(byte)
image = Image.frombytes('RGB', (128, 128), byte, 'raw')
image.show()
