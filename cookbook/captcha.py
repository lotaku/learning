from PIL import Image, ImageOps
import pytesseract
# open('1.py')

# Image.open('captcha.jpg')
a = pytesseract.image_to_string(Image.open('simple_number2_.jpeg'))
print a
d = Image.open('temp_captcha_.jpeg')
d2 = d.convert('1')
d2.save('temp_captcha_2.jpeg')
b = pytesseract.image_to_string(Image.open('temp_captcha_2.jpeg'))
print b
# d2 = ImageOps.invert(d)
# d2.save('invsimple_number2.jpeg')
# d =Image.open('simple_number2.jpeg')
# d2 = d.convert('1')
# d2.save('simple_number2_.jpeg')
# # d = pytesseract.image_to_string(Image.open('invsimple_number2.jpeg'), lang='eng')
#
# d_ =Image.open('simple_number2.jpeg')
# d3 = pytesseract.image_to_string(d_)
# print d3
# # b = pytesseract.image_to_string(a,  lang='fra')
#
# b = pytesseract.image_to_string(Image.open('simple_number2.jpeg'), lang='eng')
# c = pytesseract.image_to_string(Image.open('simple_number.jpeg'))
# print a
# print type(b)
# print b
# print c
# a = pytesseract.image_to_string(Image.open('/Users/zezhou/workspace/learning/cookbook/simple_number.jpeg'))
# print type(a)
# print len(a)
# print a
from PIL import Image
import sys
#
# import pyocr
# import pyocr.builders
#
# tools = pyocr.get_available_tools()
# if len(tools) == 0:
#     print("No OCR tool found")
#     sys.exit(1)
# tool = tools[0]
# print("Will use tool '%s'" % (tool.get_name()))
# # Ex: Will use tool 'tesseract'
#
# langs = tool.get_available_languages()
# print("Available languages: %s" % ", ".join(langs))
# lang = langs[0]
# lang = 'chi_sim'
# print("Will use lang '%s'" % (lang))
# # Ex: Will use lang 'fra'
#
# txt = tool.image_to_string(
#     Image.open('invsimple_number2.jpeg'),
#     lang=lang,
#     builder=pyocr.builders.TextBuilder()
# )
# print txt
# word_boxes = tool.image_to_string(
#     Image.open('3.png'),
#     lang=lang,
#     builder=pyocr.builders.WordBoxBuilder()
# )
# print word_boxes
# line_and_word_boxes = tool.image_to_string(
#     Image.open('simple_number.jpeg'), lang=lang,
#     builder=pyocr.builders.LineBoxBuilder()
# )
# print line_and_word_boxes
#
# # Digits - Only Tesseract
# digits = tool.image_to_string(
#     Image.open('invsimple_number2.jpeg'),
#     lang=lang,
#     builder=pyocr.tesseract.DigitBuilder()
# )
# print digits
# print len(digits)
