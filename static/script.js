function initSocketIO() {
    const socket = io();

    document.getElementById('startButton').addEventListener('click', function () {
        socket.emit('start loading');
    });

    document.getElementById('stopButton').addEventListener('click', function () {
        socket.emit('stop loading');
    });

    document.getElementById('interruptButton').addEventListener('click', function () {
        socket.emit('stop loading');
        socket.emit('update score', {player: 1});
    });

    document.getElementById('resetButton').addEventListener('click', function () {
        socket.emit('reset scores');
    });

    socket.on('loading started', function () {
        startLoading();
    });

    socket.on('loading stopped', function () {
        stopLoading();
    });

    socket.on('score updated', function (data) {
        incrementScore(data.player);
    });

    socket.on('scores reset', function () {
        resetScores();
    });
}
