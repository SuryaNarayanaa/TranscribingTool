from flask import Flask, render_template, request
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import sys
import time
sys.path.append('..')

from videoToText.vid_to_wav.converter import convertToWav
from audioToSubtitle.main import audioToSubtitle
from flask import send_file

app = Flask(__name__)

# Configure Cloudinary
cloudinary.config(
  cloud_name = "djw9xl2nt",
  api_key = "631834537852849",
  api_secret = "sA2jWjTcm9HrIK1piRkirg-OVvo"
)
start_time = time.time()

@app.route('/')
def upload():

    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith(('.mp4', '.avi', '.mov')):
            result = cloudinary.uploader.upload(file, resource_type="video")
            video_id = result['public_id']
            print("Video Id :",video_id)
            audioFile =convertToWav(video_id)
            print("Audio File :",audioFile)
            subtitleFile = audioToSubtitle(audioFile,video_id)
            end_time = time.time()
            time_difference = end_time - start_time
            print(f"Difference in seconds: {time_difference}")



         

            return subtitleFile
            
            
            


        else:
            return "Invalid file type. Please upload a video file."

if __name__ == '__main__':
    app.run(debug=True)
