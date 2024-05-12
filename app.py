from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

scores = [0, 0]
loading = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start loading')
def handle_start_loading():
    global loading
    loading = True
    emit('loading started', broadcast=True)

@socketio.on('stop loading')
def handle_stop_loading():
    global loading
    loading = False
    emit('loading stopped', broadcast=True)

@socketio.on('give point')
def handle_give_point():
    global loading, scores
    if loading:
        scores[1] += 1  # Assign point to Kicker if loading
    else:
        scores[0] += 1  # Assign point to Caster if not loading
    emit('update scores', scores, broadcast=True)

@socketio.on('reset scores')
def handle_reset_scores():
    global scores
    scores = [0,0]
    emit('scores reset', broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
