from PIL import Image

def hide_qr_in_image(carrier_path, qr_path, output_path):
    """
    将二维码图片隐藏到载体图片的蓝色通道中。
    """
    carrier_img = Image.open(carrier_path).convert("RGB")
    qr_img = Image.open(qr_path).convert("1") # 转换为1位黑白图像

    if qr_img.size[0] > carrier_img.size[0] or qr_img.size[1] > carrier_img.size[1]:
        raise ValueError("二维码图片尺寸大于载体图片尺寸！")

    for x in range(qr_img.width):
        for y in range(qr_img.height):
            carrier_pixel = list(carrier_img.getpixel((x, y)))
            r, g, b = carrier_pixel
            qr_pixel = qr_img.getpixel((x, y))
            # LSB 编码逻辑
            # 如果二维码像素是黑色(0)，则将蓝色通道的LSB设为0
            if qr_pixel == 0:
                carrier_pixel[2] = b & 254 # AND 11111110
            # 如果二维码像素是白色(255)，则将蓝色通道的LSB设为1
            else:
                carrier_pixel[2] = b | 1   # OR 00000001

            carrier_img.putpixel((x, y), tuple(carrier_pixel))

    carrier_img.save(output_path)
    print(f"二维码已成功隐藏到 {output_path}！")

hide_qr_in_image("carrier.png", "my_qrcode.png", "output.png")