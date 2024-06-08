from PIL import Image, ImageDraw, ImageFont
import string
import random
from io import BytesIO


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


str_all = string.digits + string.ascii_letters


def random_code(size=(200, 60), length=4, point_num=100, line_num=15):
    width, height = size
    # 生成白色背景图片
    img = Image.new('RGB', (width, height), color=(255, 255, 255))

    # 生成画布
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font='app/static/font/hanyidishengxiaritifan.ttf', size=50)

    # 书写文字
    valid_code = ''
    for i in range(length):
        random_char = random.choice(str_all)
        draw.text((40 * i + 20, -12), random_char, (0, 0, 0), font=font)
        valid_code += random_char
    print(valid_code)


    for i in range(point_num):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), random_color())

    # 随机划线
    for i in range(line_num):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=random_color())

    # 创建一个内存句柄

    f = BytesIO()

    # 将图片保存到内存句柄中

    img.save(f, 'PNG')

    # 读取内存句柄
    data = f.getvalue()
    return (data, valid_code)


if __name__ == '__main__':
    random_code()
