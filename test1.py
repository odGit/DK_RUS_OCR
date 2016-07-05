from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'tesseract'

lang = "dan"
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'

# txt = tool.image_to_string(Image.open('test.png'),
#                            lang=lang,
#                            builder=pyocr.builders.TextBuilder())

# print txt
# word_boxes = tool.image_to_string(Image.open('test.png'),
#                                   lang=lang,
#                                   builder=pyocr.builders.WordBoxBuilder())

list_func = pyocr.PrintVariablesToFile
# print word_boxes
# line_and_word_boxes = tool.image_to_string(
#         Image.open('test.png'), lang=lang,
#         builder=pyocr.builders.LineBoxBuilder())

# # Digits - Only Tesseract
# digits = tool.image_to_string(Image.open('test-digits.png'),
#                               lang=lang,
#                               builder=pyocr.tesseract.DigitBuilder())