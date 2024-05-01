from flask import Flask, render_template, request , url_for,session , redirect
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
app.secret_key = 'sjpa&@012'


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

from cloudinary.uploader import upload

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith(('.mp4', '.avi', '.mov')):
            result = cloudinary.uploader.upload(file, resource_type="video")
            video_id = result['public_id']
            print("Video ID: ", video_id)
            session['video_id'] = video_id

            # Split the video into chunks
           

            # Upload the video chunks to Cloudinary
            
            return redirect(url_for('convertToAudio', video_id=video_id))
@app.route('/convertToAudio/<video_id>')
def convertToAudio(video_id):
    audio_path = convertToWav(video_id)
    session['audio_path'] = audio_path
    print("Audio Path: ", audio_path)
    return redirect(url_for('convertToSubtitle'))

@app.route('/convertToSubtitle/')
def convertToSubtitle():

    audio_path = session.get('audio_path')
    

    subtitle_url = audioToSubtitle(audio_path , session.get('video_id'))
    session['subtitle_url'] = subtitle_url
    

    # print("Subtitle URL: ", subtitle_url)
    # session['subtitle_url'] = subtitle_url 

    return redirect(url_for('play_video', video_id=session.get('video_id')))
        

@app.route('/play_video/<video_id>')
def play_video(video_id):
    # subtitle_url = session.get('subtitle_url')
    # return render_template('play_video.html', video_id=video_id, subtitle_url=subtitle_url)
    return render_template('play_video.html', video_id=video_id ,subtitle_url = session.get('subtitle_url'))

if __name__ == '__main__':
    app.run(debug=True)


            




         

            
            
            
            
