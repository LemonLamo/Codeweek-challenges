from PIL import Image

def hex_to_ascii(hex_str):
    # Convert hexadecimal string to integer
    decimal_value = int(hex_str, 16)
    # Convert integer to ASCII character
    ascii_char = chr(decimal_value)
    return ascii_char

def image_to_ascii('D.png'):
    # Open the image
    img = Image.open('D.png')
    width, height = img.size

    ascii_art = ''

    # Iterate through each pixel row
    for y in range(height):
        # Iterate through each pixel column
        for x in range(width):
            # Get the color of the pixel at (x, y)
            color = img.getpixel((x, y))
            # Convert color to hexadecimal string
            hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            # Convert hexadecimal color to ASCII character
            ascii_art += hex_to_ascii(hex_color.lstrip('#'))
        ascii_art += '\n'  # Add newline at the end of each row

    return ascii_art

# Path to your image file
image_path = 'D.png'

# Convert image to ASCII art
result = image_to_ascii('D.png')
print(result)
