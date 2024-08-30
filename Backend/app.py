from flask import Flask, request, jsonify
import os
from video_processing import process_video
from audio_output import generate_audio_prompt

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'videoFile' not in request.files:
        return jsonify({'message': 'No video file provided'}), 400

    video = request.files['videoFile']
    if video.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    if not video.filename.lower().endswith(('.mp4', '.avi', '.mov')):
        return jsonify({'message': 'Unsupported file format'}), 400

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    try:
        detections = process_video(video_path)
        audio_prompt = generate_audio_prompt(detections)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

    return jsonify({'message': 'Processing complete', 'result': detections, 'audio_prompt': audio_prompt})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
