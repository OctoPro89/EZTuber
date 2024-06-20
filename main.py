# Commands: pip install pytube
#           pip install moviepy

import argparse
from pytube import Playlist
from pytube import YouTube
import os

# MP4 to MP3
from moviepy.editor import *


# Fix goofy error when downloading some videos
from pytube.innertube import _default_clients
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

def download_playlist(url, highres, audioonly, output_path='./'):
    playlist = Playlist(url)
    playlist_title = playlist.title
    print(f'Downloading playlist: {playlist_title}')
    
    for video in playlist.videos:
        print(f'Downloading video: {video.title}')
        video.streams.get_highest_resolution().download(output_path) if highres else video.streams.get_lowest_resolution().download(output_path)
        print(f'{video.title} downloaded successfully!')
        
        if audioonly:
            print('Converting video to audio only')
            mp4_to_mp3(video.title, output_path)
            print('Converted video to audio only successfully!')

def download_video(url, highres, audioonly, output_path='./'):
    yt = YouTube(url)
    print(f'Downloading video: {yt.title}')
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').last().download(output_path) if highres else yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download(output_path)
    print(f'{yt.title} downloaded successfully!')

    if audioonly:
        print('Converting video to audio only')
        mp4_to_mp3(yt.title, output_path)
        print('Converted video to audio only successfully!')

def mp4_to_mp3(filename, output_path='./'):
    newname = filename.replace('.', '') # remove periods
    video = VideoFileClip(output_path + "/" + newname + ".mp4")
    video.audio.write_audiofile(output_path + "/" + newname + ".mp3", verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Playlist Downloader")
    parser.add_argument("--video", help="URL of the YouTube video", required=False)
    parser.add_argument("--playlist", help="URL of the YouTube playlist", required=False)
    parser.add_argument("--audio-only", help="URL of the YouTube playlist", action="store_true", required=False)
    parser.add_argument("--highres", help="Sets high resolution", action="store_true", required=False)
    parser.add_argument("--output", help="Output directory", default=os.path.join(os.path.expanduser('~'), 'Downloads'))
    args = parser.parse_args()

    playlist_url = args.playlist
    url = args.video
    audioonly = args.audio_only
    highres = args.highres
    output_dir = args.output
    
    if playlist_url == None and url == None:
        print("usage: ytdownloader.py [--video VIDEO_URL] [--playlist PLAYLIST_URL] [--audio-only] [--highres] [--output OUTPUT_DIRECTORY]")
        exit(0)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if url:
        download_video(url, highres, audioonly, output_dir)
    elif playlist_url:
        download_playlist(playlist_url, highres, audioonly, output_dir)
