from flask import Flask, render_template, jsonify

app = Flask(__name__,template_folder='template',static_folder='static')

# List of audio files (you can customize this)
audio_files = ['audio1.mp3', 'audio2.mp3', 'audio3.mp3']
current_audio_index = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    # You can add code to control audio playback here
    return jsonify({'status': 'playing'})

@app.route('/pause')
def pause():
    # You can add code to pause audio here
    return jsonify({'status': 'paused'})

@app.route('/next')
def next_track():
    global current_audio_index
    current_audio_index = (current_audio_index + 1) % len(audio_files)
    return jsonify({'status': 'next', 'audio_index': current_audio_index})

@app.route('/prev')
def prev_track():
    global current_audio_index
    current_audio_index = (current_audio_index - 1) % len(audio_files)
    return jsonify({'status': 'prev', 'audio_index': current_audio_index})

if __name__ == '__main__':
    app.run(debug=True)

