"""
Библиотека requests
"""
import requests

# requests.get()
# Этот метод используется для отправки GET-запроса к указанному URL. Он позволяет получать данные с сервера.

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

# requests.post()
# Метод post() используется для отправки данных на сервер.
# Это может быть полезно для создания новых ресурсов.

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.status_code)
print(response.json())

# requests.put()
# Метод put() используется для обновления существующего ресурса на сервере.
# Он отправляет данные на указанный URL.

data = {'key': 'new_value'}
response = requests.put('https://httpbin.org/put', json=data)
print(response.status_code)
print(response.json())

"""
Библиотека Pillow.
Ссылка на изображение, на примере которого показана работа с библиотекой:
https://1drv.ms/i/c/6748c63a4a3f0486/EW8VE0w8aulJo5gevnrYMOoBqJ-unjQ1kxJcMethVdZ2Cg?e=r2rqGK

и шрифт:
https://1drv.ms/u/c/6748c63a4a3f0486/EYclDXkMqMZDvCQ7O_i0WQcBI5m8ZBWLIMKztZxOGgbS9Q?e=B5fBYE
"""
from PIL import Image

# Открытие изображения по указанному пути
image = Image.open('The_elder_scrolls_v_skyrim.jpg')
image.show()
print(image.size)

# Изменим размер картинки
new_image_1 = image.resize((500, 200))
new_image_1.save('image_resize.jpg')

new_image_1.show()

# Добавим к оригинальной картинке какой-нибудь фильтер
# Для этого нам понадобится дополнительный модуль из библиотеки
from PIL import ImageFilter

blured_image = image.filter(ImageFilter.BLUR)
blured_image.show()

blured_image.save('image_blur.jpg')

# Изменим формат файла
image.save('image_png.png', 'PNG')

# А может добавим текст на картинку? Почему бы и... Да.
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(image)
text = "The Elder Scrolls V"
font_size = 24

try:
    font = ImageFont.truetype("Runic_Alt.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

text_color = (255, 255, 255)
text_position = (image.width//2, image.height//2+150)
draw.text(text_position, text, fill=text_color, font=font)

image.save('image_with_text.jpg')
