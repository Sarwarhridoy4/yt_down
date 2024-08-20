# import yt_dlp
# import os
# import ffmpeg
# import logging
#
# # Setup logging
# logging.basicConfig(level=logging.DEBUG)
#
#
# class Downloader:
#     def __init__(self, url, format, output_folder, update_progress, download_finished):
#         self.url = url
#         self.format = format
#         self.output_folder = output_folder
#         self.update_progress = update_progress
#         self.download_finished = download_finished
#
#     def start_download(self):
#         try:
#             ydl_opts = {
#                 'format': 'bestvideo+bestaudio/best',
#                 'progress_hooks': [self.progress_hook],
#                 'outtmpl': os.path.join(self.output_folder, '%(title)s.%(ext)s'),
#             }
#
#             # Use postprocessors only if needed for MP3
#             if self.format == "MP3":
#                 ydl_opts['postprocessors'] = [{
#                     'key': 'FFmpegExtractAudio',
#                     'preferredcodec': 'mp3',
#                     'preferredquality': '192',
#                 }]
#             else:
#                 ydl_opts['postprocessors'] = [{
#                     'key': 'FFmpegVideoConvertor',
#                     'preferedformat': self.format.lower(),
#                 }]
#
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([self.url])
#
#         except Exception as e:
#             logging.error(f"Error during download: {e}")
#             raise
#
#     def progress_hook(self, d):
#         if d['status'] == 'downloading':
#             total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
#             if total_bytes:
#                 downloaded_bytes = d['downloaded_bytes']
#                 progress = downloaded_bytes / total_bytes * 100
#                 self.update_progress(progress)
#
#         elif d['status'] == 'finished':
#             self.download_finished()


import yt_dlp
import os
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

class Downloader:
    def __init__(self, url, format, output_folder, update_progress, download_finished):
        self.url = url
        self.format = format
        self.output_folder = output_folder
        self.update_progress = update_progress
        self.download_finished = download_finished

    def start_download(self):
        try:
            ydl_opts = {
                'format': 'best',  # Choose best available format with both video and audio.
                'progress_hooks': [self.progress_hook],
                'outtmpl': os.path.join(self.output_folder, '%(title)s.%(ext)s'),
            }

            if self.format == "MP3":
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])

        except Exception as e:
            logging.error(f"Error during download: {e}")
            raise

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                downloaded_bytes = d['downloaded_bytes']
                progress = downloaded_bytes / total_bytes * 100
                self.update_progress(progress)

        elif d['status'] == 'finished':
            self.download_finished()
