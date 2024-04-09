from moviepy.editor import VideoFileClip
import os
video_path = os.path.join("Videos","testvid.mp4" )
audio_path = os.path.join("Audio","my_audio.wav")
video = VideoFileClip(video_path)
audio = video.audio

audio.write_audiofile(audio_path, codec='pcm_s16le')
