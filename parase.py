from PIL import Image

def extract_qr_from_image(stego_image_path, output_path, original_qr_size):
    """
    从隐写图片中提取二维码。
    """
    stego_img = Image.open(stego_image_path).convert("RGB")
    width, height = original_qr_size

    extracted_qr = Image.new("1", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = stego_img.getpixel((x, y))
            # 提取蓝色通道的LSB
            if b & 1 == 0: # 如果LSB是0
                extracted_qr.putpixel((x, y), 0) # 像素设为黑
            else: # 如果LSB是1
                extracted_qr.putpixel((x, y), 255) # 像素设为白

    extracted_qr.save(output_path)

qr_size = Image.open("my_qrcode.png").size
extract_qr_from_image("output.png", "extracted_qr.png", qr_size)