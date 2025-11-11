<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Catch the Ball - Upgraded</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      font-family: Arial, sans-serif;
      background: #000;
    }

    #score {
      position: absolute;
      top: 10px;
      left: 10px;
      font-size: 24px;
      color: #fff;
      font-weight: bold;
      z-index: 10;
    }

    canvas {
      display: block;
      margin: 0 auto;
      background: linear-gradient(to bottom, #0a0a0a, #1a1a1a);
    }
  </style>
</head>
<body>
  <div id="score">Score: 0</div>
  <canvas id="gameCanvas" width="500" height="600"></canvas>

  <audio id="catchSound" src="https://www.soundjay.com/button/beep-07.wav"></audio>

  <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const catchSound = document.getElementById('catchSound');

    // Paddle
    const paddle = {
      width: 120,
      height: 20,
      x: canvas.width / 2 - 60,
      y: canvas.height - 40,
      speed: 8,
      dx: 0
    };

    // Balls
    let balls = [];
    const ballCount = 3;
    for (let i = 0; i < ballCount; i++) {
      balls.push({
        x: Math.random() * (canvas.width - 20),
        y: Math.random() * -300,
        radius: 15,
        speed: 3 + i
      });
    }

    let score = 0;

    // Stars background
    const stars = [];
    for (let i = 0; i < 100; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 2 + 1,
        speed: Math.random() * 1 + 0.2
      });
    }

    function drawPaddle() {
      ctx.fillStyle = '#ff4757';
      ctx.fillRect(paddle.x, paddle.y, paddle.width, paddle.height);
    }

    function drawBalls() {
      balls.forEach(ball => {
        ctx.beginPath();
        ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
        ctx.fillStyle = '#1e90ff';
        ctx.fill();
        ctx.closePath();
      });
    }

    function drawStars() {
      ctx.fillStyle = '#fff';
      stars.forEach(star => {
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
        ctx.fill();
        star.y += star.speed;
        if (star.y > canvas.height) star.y = 0;
      });
    }

    function drawScore() {
      document.getElementById('score').textContent = 'Score: ' + score;
    }

    function movePaddle() {
      paddle.x += paddle.dx;
      if (paddle.x < 0) paddle.x = 0;
      if (paddle.x + paddle.width > canvas.width) paddle.x = canvas.width - paddle.width;
    }

    function moveBalls() {
      balls.forEach(ball => {
        ball.y += ball.speed;

        // Collision with paddle
        if (
          ball.y + ball.radius >= paddle.y &&
          ball.x >= paddle.x &&
          ball.x <= paddle.x + paddle.width
        ) {
          score++;
          ball.y = Math.random() * -200;
          ball.x = Math.random() * (canvas.width - ball.radius * 2);
          ball.speed += 0.2; // Increase speed after catch
          catchSound.play();
        }

        // Missed ball
        if (ball.y > canvas.height) {
          alert('Game Over! Your Score: ' + score);
          document.location.reload();
        }
      });
    }

    function update() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawStars();
      drawPaddle();
      drawBalls();
      drawScore();
      movePaddle();
      moveBalls();
      requestAnimationFrame(update);
    }

    // Controls
    function keyDownHandler(e) {
      if (e.key === 'ArrowRight') paddle.dx = paddle.speed;
      else if (e.key === 'ArrowLeft') paddle.dx = -paddle.speed;
    }

    function keyUpHandler(e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') paddle.dx = 0;
    }

    document.addEventListener('keydown', keyDownHandler);
    document.addEventListener('keyup', keyUpHandler);

    update();
  </script>
</body>
</html>
