from PIL import Image


def add_watermark(image_path, watermark_path, opacity, scale, position):
    """
    将水印图片添加到原始图片上，返回执行状态
    :param image_path: 原始图片的路径
    :param watermark_path: 水印图片的路径
    :param opacity: 水印图片的透明度，范围是0-1
    :param scale: 水印图片的缩放比例，范围是0-1
    :param position: 水印图片的位置，是一个字符串，例如"left_top"
    :return: 执行状态，True表示成功，False表示失败
    """
    try:
        # 打开原始图片和水印图片
        image = Image.open(image_path)
        watermark = Image.open(watermark_path)

        # 计算水印图片的大小和透明度
        watermark_size = (int(watermark.width * scale), int(watermark.height * scale))
        watermark = watermark.resize(watermark_size, Image.ANTIALIAS)
        watermark_opacity = int(255 * opacity)
        watermark.putalpha(watermark_opacity)

        # 计算水印图片的位置
        positions = {
            'left_top': (0, 0),
            'center_top': (image.width // 2 - watermark.width // 2, 0),
            'right_top': (image.width - watermark.width, 0),
            'left_center': (0, image.height // 2 - watermark.height // 2),
            'center': (image.width // 2 - watermark.width // 2, image.height // 2 - watermark.height // 2),
            'right_center': (image.width - watermark.width, image.height // 2 - watermark.height // 2),
            'left_bottom': (0, image.height - watermark.height),
            'center_bottom': (image.width // 2 - watermark.width // 2, image.height - watermark.height),
            'right_bottom': (image.width - watermark.width, image.height - watermark.height),
        }
        watermark_position = positions[position]

        # 将水印图片添加到原始图片上
        image.paste(watermark, watermark_position, watermark)

        # 保存结果图片
        image.save(image_path)

        return True

    except:
        return False
