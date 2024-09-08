"""
Meme Generator that takes image, and inserts
a given quote and corresponding author into image
at random location.
"""

from PIL import Image, ImageDraw, ImageFont
from random import randint
import os
import textwrap


class MemeEngine:
    """Image and quotes are loaded for meme"""

    def __init__(self, output_dir):
        """Intialize Output directory."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create meme and store in output file."""
        img = Image.open(img_path)
        img = self._resize_image(img, width)
        img = self._add_text(img, text, author)

        out_file = os.path.join(self.output_dir, f"{randint(0, 10000)}.jpg")
        img.save(out_file, "JPEG")

        return out_file

    def _resize_image(self, img, width):
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        return img.resize((width, height), Image.NEAREST)

    def _add_text(self, img, text, author):
        text = text.replace("\u2019", "")
        author = author.replace("\u2019", "")
        wrapper = textwrap.TextWrapper(width=50)
        wrapped_text = wrapper.fill(text=text)

        draw = ImageDraw.Draw(img)

        random_y = randint(0, int(img.size[1] / 2))

        font_size = 20
        font = ImageFont.truetype("./MemeEngine/arial.ttf", size=font_size)

        # Calculate the maximum text height based on the image height
        max_text_height = img.size[1] - random_y

        # Determine the number of lines required for the wrapped text
        lines = wrapped_text.count('\n') + 1

        # Calculate the total height required for the wrapped text
        total_text_height = lines * font_size

        # Check if the total text height exceeds the maximum text height
        if total_text_height > max_text_height:
            # Reduce the font size to fit the text within the image height
            font_size = int(max_text_height / lines)
            font = ImageFont.truetype("./MemeEngine/arial.ttf", size=font_size)

        # Calculate the y-coordinate for the author text
        author_y = random_y + total_text_height + 10

        # Calculate the width and height of the wrapped text
        max_text_width = 0
        wrapped_text_lines = wrapped_text.split('\n')
        for line in wrapped_text_lines:
            line_bbox = font.getbbox(line)
            line_width = line_bbox[2] - line_bbox[0]
            max_text_width = max(max_text_width, line_width)

        # Calculate the x-coordinate for centering the text
        text_x = (img.size[0] - max_text_width) // 2

        # Draw the wrapped text lines
        for line in wrapped_text_lines:
            line_bbox = font.getbbox(line)
            line_width = line_bbox[2] - line_bbox[0]
            draw.text((text_x, random_y), line, fill='white',
                      font=font, encoding='utf-8')
            random_y += font_size

        draw.text((text_x, author_y), f"   -{author}",
                  fill='white', font=font, encoding='utf-8')

        return img
