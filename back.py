import random
from flask import Flask, render_template, request, send_from_directory, jsonify

app = Flask(__name__, template_folder='template', static_folder='static')


# Sample audio files (replace with your own)
audio_files = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3', 'song5.mp3', 'song6.mp3', 'song7.mp3', 'song8.mp3',
               'song9.mp3', 'song10.mp3', 'song11.mp3', 'song12.mp3', 'song13.mp3', 'song14.mp3', 'song15.mp3',
               'song16.mp3', 'song17.mp3', 'song18.mp3', 'song19.mp3', 'song20.mp3', 'song21.mp3', 'song22.mp3',
               'song23.mp3', 'song24.mp3', 'song25.mp3', 'song26.mp3', 'song27.mp3', 'song28.mp3', 'song29.mp3',
               'song30.mp3', 'song31.mp3', 'song32.mp3', 'song33.mp3', 'song34.mp3', 'song35.mp3', 'song36.mp3',
               'song37.mp3', 'song38.mp3', 'song39.mp3', 'song40.mp3', 'song41.mp3', 'song42.mp3', 'song43.mp3',
               'song44.mp3', 'song45.mp3', 'song46.mp3', 'song47.mp3', 'song48.mp3', 'song49.mp3', 'song50.mp3']
current_index = 0
is_playing = False
is_shuffling = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('static/audio', filename)

@app.route('/play')
def play():
    global is_playing
    is_playing = True
    return jsonify(result='success')

@app.route('/pause')
def pause():
    global is_playing
    is_playing = False
    return jsonify(result='success')

@app.route('/next')
def next():
    global current_index
    current_index = (current_index + 1) 
    next_audio = audio_files[current_index]
    return jsonify(result='success', audio=next_audio)

@app.route('/previous')
def previous():
    global current_index
    current_index = (current_index - 1) 
    next_audio = audio_files[current_index]
    return jsonify(result='success', audio=next_audio)

@app.route('/shuffle')
def shuffle():
    global is_shuffling
    global current_index
    is_shuffling = not is_shuffling
    if is_shuffling:
        # Generate a shuffled order of indexes
        shuffled_indexes = list(range(len(audio_files)))
        random.shuffle(shuffled_indexes)
        # If the current index is in the shuffled order, remove it
        if current_index in shuffled_indexes:
            shuffled_indexes.remove(current_index)
        # Insert the current index at the beginning
        shuffled_indexes.insert(0, current_index)
        # Update the audio files order based on shuffled indexes
        shuffled_audio_files = [audio_files[i] for i in shuffled_indexes]
        audio_files[:] = shuffled_audio_files
        return jsonify(result='success')
    else:
        # If shuffling is turned off, revert to the original order
        audio_files.sort()
        return jsonify(result='success')
if __name__ == '__main__':
    app.run(debug=True)

