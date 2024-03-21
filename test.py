from PIL import Image


def extract_hex_values():
    try:

        img = Image.open("D.png")
        result = ""
        for y in range(1):
            for x in range(53):
                # Get the RGB color value of the pixel
                pixel = img.getpixel((x, y))

                # If the pixel is an integer, convert it to an RGB tuple
                if isinstance(pixel, int):
                    pixel = (pixel, pixel, pixel)
                # If the image mode is "P" (palette), convert the pixel to RGB tuple
                elif img.mode == "P":
                    pixel = img.palette[pixel]

                r, g, b = pixel

                # Convert RGB to hexadecimal
                hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)

                # Convert hexadecimal to ASCII
                ascii_char = bytearray.fromhex(hex_value.lstrip('#')).decode("utf-8")

                # Append the ASCII character to the result
                result += ascii_char

        return result
    except Exception as e:
        return f"Error: {str(e)}"


# Call the function
output = extract_hex_values()
print(output)
