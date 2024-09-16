from PIL import Image


img=Image.open("favicon.png")

img.save("Logo.jpg", "PNG")


def convert_jpeg_to_ico(source_path, target_path, sizes=None):
    if sizes is None:
        sizes = [(32, 32)]
    with Image.open(source_path) as img:
        img.save(target_path, format='ICO', size=sizes)


source_jpeg_path = r'C:\Users\Andrei Baditoiu\PycharmProjects\web server\static\images\favicon.png'
target_ico_path = r'C:\Users\Andrei Baditoiu\PycharmProjects\web server\static\images\favicon.ico'

convert_jpeg_to_ico(source_jpeg_path, target_ico_path)
