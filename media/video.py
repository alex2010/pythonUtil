import os
import subprocess


def convert_video_to_mp4(filename):
    # 获取文件名和文件路径
    file_path, file_name = os.path.split(filename)
    # 获取文件名和扩展名
    name, ext = os.path.splitext(file_name)

    # 新文件名和路径
    new_name = f"{name}.mp4"
    new_path = os.path.join(file_path, new_name)

    # FFmpeg命令
    command = f"ffmpeg -i {filename} -c:v libx264 -preset slow -crf 22 -c:a copy {new_path}"

    # 执行命令
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"{filename} 转换为 {new_path}")
    except subprocess.CalledProcessError as e:
        print(f"转换 {filename} 出错: {e}")


def extract_video(video_path, start_time, duration):
    """
    从视频中截取指定时间段的视频，并压缩为适合网络播放的格式
    :param video_path: 视频文件路径
    :param start_time: 起始时间，格式为"00:00:00"（时:分:秒）
    :param duration: 视频长度，单位为秒
    :return: 无返回值，生成的视频保存在当前文件夹下
    """
    output_path = os.path.splitext(video_path)[0] + "_output.mp4"
    cmd = f"ffmpeg -ss {start_time} -i {video_path} -t {duration} \
           -c:v libx264 -preset slow -crf 28 -c:a aac -b:a 128k -movflags +faststart {output_path}"
    os.system(cmd)


# path = '/Users/alexwang/Downloads/iAccept/23-4-1/DJI_0625.MP4'
# start_time = '00:00:10'
# duration = '00:00:05'
#
extract_video('/Users/alexwang/Projects/Headspace1.mp4', '00:00:05',  '00:18:28')
#
# convert_video_to_mp4('/Users/alexwang/Projects/Headspace1.flv')