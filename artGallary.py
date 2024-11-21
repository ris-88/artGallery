from PIL import Image

image = Image.open('monro.jpg')
if image.mode != 'RGB':
    image = image.convert('RGB')

red_channel, green_channel, blue_channel = image.split()

left_coordinates = (50, 0, image.width, image.height)
right_coordinates = (0, 0, image.width - 50, image.height)
middle_coordinates = (25, 0, image.width - 25, image.height)

cropped_red = red_channel.crop(right_coordinates)
cropped_middle_red = red_channel.crop(middle_coordinates)
blended_red = Image.blend(cropped_red, cropped_middle_red, 0.6)

cropped_blue = blue_channel.crop(left_coordinates)
cropped_middle_blue = blue_channel.crop(middle_coordinates)
blended_blue = Image.blend(cropped_blue, cropped_middle_blue, 0.6)

cropped_middle_green = green_channel.crop(middle_coordinates)

new_image = Image.merge('RGB', (blended_red, cropped_middle_green, blended_blue))

new_image.thumbnail((80, 80))

new_image.save('new_image.jpg')