# # Python下载B站视频
# import os
# import re
# import json
# import click
# import requests
# from contextlib import closing


# class bilibili():
# 	def __init__(self):
# 		self.infoheaders = {
# 						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
# 						'accept-encoding': 'gzip, deflate, br',
# 						'accept-language': 'zh-CN,zh;q=0.9',
# 						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
# 					}
# 		self.downheaders = {
# 						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
# 						'accept': '*/*',
# 						'accept-encoding': 'gzip, deflate, br',
# 						'accept-language': 'zh-CN,zh;q=0.9',
# 						'Referer': 'https://search.bilibili.com/all?keyword='
# 					}

                
# 	def _GetVideoInfos(self, url):
# 		res = requests.get(url=url, headers=self.infoheaders)
# 		pattern = '.__playinfo__=(.*)</script><script>window.__INITIAL_STATE__='
# 		re_result = re.findall(pattern, res.text)[0]
# 		temp = json.loads(re_result)
# 		download_url = temp['durl'][0]['url']
# 		if 'mirrork' in download_url:
# 			vid = download_url.split('/')[6]
# 		else:
# 			vid = download_url.split('/')[7]
# 			if len(vid) >= 10:
# 				vid = download_url.split('/')[6]
# 		Vurlinfos = [download_url, vid]
# 		return Vurlinfos



# 	def _Download(self, Vurlinfos, savepath):
# 		if not os.path.exists(savepath):
# 			os.mkdir(savepath)
# 		name = Vurlinfos[1]
# 		download_url = Vurlinfos[0]
# 		with closing(requests.get(download_url, headers=self.downheaders, stream=True, verify=False)) as res:
# 			total_size = int(res.headers['content-length'])
# 			if res.status_code == 200:
# 				label = '[FileSize]:%0.2f MB' % (total_size/(1024*1024))
# 				with click.progressbar(length=total_size, label=label) as progressbar:
# 					with open(os.path.join(savepath, name+'.flv'), "wb") as f:  
# 						for chunk in res.iter_content(chunk_size=1024):
# 							if chunk:
# 								f.write(chunk)
# 								progressbar.update(1024)
# 			else:
# 				print('[ERROR]:Connect error...')
				


# 	def get(self, url, savepath='./videos'):
# 		Vurlinfos = self._GetVideoInfos(url)
# 		self._Download(Vurlinfos, savepath)
		


# if __name__ == '__main__':
# 	print('[Wecome]: Bilibili视频下载器 V1.0')
# 	url = input('请输入视频链接:\n(例如https://www.bilibili.com/video/av26431038/?spm_id_from=333.334.chief_recommend.16)\n')
# 	bilibili().get(url)


# from pytube import YouTube

# # 视频链接
# video_url = 'https://www.bilibili.com/video/av607072762'
# # video_url = 'https://www.bilibili.com/bangumi/play/ep717018?spm_id_from=autoNext&from_spmid=666.25.episode.0'

# # 创建YouTube对象
# yt = YouTube(video_url)

# # 获取视频的最高质量的视频流
# stream = yt.streams.get_highest_resolution()

# # 视频下载到指定路径
# stream.download('/path/to/save/video/')

# import json
# class BiliBili:# 构造请求头
#     __headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36","referer": "https://www.bilibili.com/",}
#     def __init__(self, url):self.url = url
#     # 获取BVID
#     def __bvid(self):
#         bvid = self.url.split('/')[len(self.url.split('/')) - 1]
#         if '?' in bvid:bvid = bvid.split('?')[0]
#         return bvid
#     # 获取CID
#     def __cid(self):
#         url = f"https://api.bilibili.com/x/player/pagelist?bvid={self.__bvid()}&jsonp=jsonp"
#         req = request.Request(url, headers=self.__headers, method="GET")
#         reponse = request.urlopen(req).read().decode("utf-8")
#         return json.loads(reponse)['data'][0]["cid"]
#     # 设置cookie
#     def set_cookie(self, cookie):
#         self.__headers['cookie'] = cookie
    
#     # 获取视频url
#     def video_url(self):
#         url = f"https://api.bilibili.com/x/player/playurl?avid=&cid={self.__cid()}&bvid={self.__bvid()}&qn=120&type=&otype=json"
#         req = request.Request(url, headers=self.__headers, method="GET")
#         response = request.urlopen(req).read().decode("utf-8")
#         return json.loads(response)['data']['durl'][0]['url']


import asyncio
from bilibili_api import video
def download_bilibili_video(url):
    try:
        video_id = video.get_video_id(url)
        video_info = video.get_video_info(video_id)
        video_url = video_info['durl'][0]['url']
        video.download_video(video_url, file_name=f"{video_id}.mp4")
        print("视频下载完成！")
    except Exception as e:
        print("视频下载失败！", e)


async def main() -> None:
    # 实例化 Video 类
    v = video.Video(bvid="BV1uv411q7Mv")
    # 获取信息
    info = await v.get_info()
    
    durl = v.get_download_url()
    print(durl)
    # 打印信息
    print(info)

    # # 调用函数下载视频
    # video_url = "https://www.bilibili.com/video/BV1aE41137jZ"  # 替换为你要下载的视频链接
    # download_bilibili_video(video_url)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())



 