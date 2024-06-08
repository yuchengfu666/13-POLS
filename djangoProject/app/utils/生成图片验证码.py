from PIL import Image, ImageDraw, ImageFont
import string
import random
from io import BytesIO


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


str_all = string.digits + string.ascii_letters


def random_code():
    width = 200
    height = 60
    # 生成白色背景图片
    img = Image.new('RGB', (width, height), color=(255, 255, 255))

    # 生成画布
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font='./font/hanyidishengxiaritifan.ttf', size=30)

    # 书写文字
    valid_code = ''
    for i in range(4):
        random_char = random.choice(str_all)
        draw.text((40 * i + 20, 10), random_char, (0, 0, 0), font=font)
        valid_code += random_char
    print(valid_code)

    for i in range(100):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), random_color())

    # 随机划线
    for i in range(15):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=random_color())

    # 创建一个内存句柄

    f = BytesIO()

    # 将图片保存到内存句柄中

    img.save(f, 'PNG')

    # 读取内存句柄
    data = f.getvalue()


if __name__ == '__main__':
    random_code()
