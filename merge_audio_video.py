import glob
import subprocess
import os

def merge_audio_video(input_audio_path, input_video_path, output_mp4_path):
    # 构建 FFmpeg 命令
    ffmpeg_cmd = [
        'ffmpeg',                  # FFmpeg 执行文件
        '-i', input_audio_path,    # 输入音频 M4S 文件路径
        '-i', input_video_path,    # 输入视频 M4S 文件路径
        '-c', 'copy',              # 使用 copy 编码方式，保持原始编码
        output_mp4_path            # 输出 MP4 文件路径
    ]

    # 执行 FFmpeg 命令
    subprocess.run(ffmpeg_cmd)

def get_subdirectories(directory):
    subdirectories = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            subdirectories.append(dir_path)
    return subdirectories

def get_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list



if __name__ == "__main__":


    # 指定目录路径
    root_path = "C:\\Video\\B站源\\户晨风\\视频处理"



    subDirs = get_subdirectories(root_path)

    for sDir in subDirs:
        # 指定文件扩展名
        file_extension = ".m4s"  # 替换为您要获取的文件类型，例如 .txt、.jpg 等

        # 构建文件路径模式
        file_pattern = os.path.join(sDir, '**', f'*{file_extension}')
        # 获取文件列表
        files = glob.glob(file_pattern, recursive=True)
        # 首发
        # 输入的音频和视频 M4S 文件路径
        input_video_m4s_path = files[0]
        input_audio_m4s_path = files[1]
        # 输出的合并后的 MP4 文件路径
        dirBasename = os.path.basename(sDir)
        output_merged_mp4_path = os.path.join(sDir,dirBasename) + "Toutput.mp4"
        # 确保输出文件夹存在
        os.makedirs(os.path.dirname(output_merged_mp4_path), exist_ok=True)
        merge_audio_video(input_audio_m4s_path, input_video_m4s_path, output_merged_mp4_path)

        print(output_merged_mp4_path + "合并完成！")
    

