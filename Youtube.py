from pytube import YouTube

# 视频链接
video_url = 'https://youtube.com/shorts/3cEf69k_8K0?si=nfPtilUJiwQG-2G2'
# video_url = 'https://www.bilibili.com/bangumi/play/ep717018?spm_id_from=autoNext&from_spmid=666.25.episode.0'

# 创建YouTube对象
yt = YouTube(video_url)

# 获取视频的最高质量的视频流
stream = yt.streams.get_highest_resolution()

# 视频下载到指定路径
stream.download('/path/to/save/video/')




 