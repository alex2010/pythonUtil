import time

from PIL import Image, ImageEnhance, ExifTags
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def add_watermark(image_path, watermark_path, width, opacity, scale, position):
    # 打开图片
    image = Image.open(image_path)

    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    try:
        exif = dict(image._getexif().items())
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # If no exif information is available, do nothing
        pass

    # 获取原图大小
    img_width, img_height = image.size

    # 计算缩放后的宽度
    if img_width > width:
        ratio = width / img_width
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        img_width, img_height = image.size

    # 打开水印图片并计算水印的大小
    watermark = Image.open(watermark_path)
    watermark_width = int(img_width * scale)
    watermark_height = int(watermark_width * watermark.size[1] / watermark.size[0])
    watermark = watermark.resize((watermark_width, watermark_height), Image.LANCZOS)

    # 根据位置参数计算水印位置
    if position == 'tl':
        location = (int(img_width * 0.05), int(img_height * 0.05))
    elif position == 'tr':
        location = (int(img_width * 0.95) - watermark_width, int(img_height * 0.05))
    elif position == 'bl':
        location = (int(img_width * 0.05), int(img_height * 0.95) - watermark_height)
    elif position == 'br':
        location = (int(img_width * 0.95) - watermark_width, int(img_height * 0.95) - watermark_height)
    elif position == 'c':
        location = ((img_width - watermark_width) // 2, (img_height - watermark_height) // 2)
    else:
        raise ValueError("Invalid position parameter.")

    # 创建透明度
    alpha = watermark.convert("RGBA").split()[-1]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)

    # 将水印添加到图片上
    image.paste(watermark, location, mask=alpha)
    image.save(image_path)
    return True


def start_watch_folder(folder_path):
    # 创建Observer对象和事件处理类
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)

    # 启动Observer对象，开始监听
    observer.start()
    print(f"开始监听文件夹：{folder_path}")

    # 循环，保持程序运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


def on_created(event):
    # 新建文件时的处理函数
    if not event.is_directory and event.src_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        # 如果不是文件夹且是图片文件，则调用add_watermark进行处理
        image_path = event.src_path
        print(f"处理图片：{image_path}")
        add_watermark(image_path, watermark_path, width, opacity, scale, position)
        print(f"处理完毕：{image_path}")


# folder = '/Users/alexwang/Downloads/iAccept/23-4-1/'
# watermark_path = '/Users/alexwang/Downloads/iAccept/logo.png'
# width = 1280
# opacity = 1
# scale = 0.1
# position = "br"
#
# start_watch_folder(folder)
