# aboutbea


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beatrice's Dance & Piano Journey</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body {
            background: linear-gradient(180deg, #d8b4fe, #fbcfe8, #a5b4fc);
            font-family: 'Poppins', sans-serif;
            overflow-x: hidden;
            margin: 0;
        }
        header {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            padding: 15px;
            text-align: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            transition: background 0.3s;
        }
        nav ul {
            list-style: none;
            padding: 0;
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        nav a {
            text-decoration: none;
            color: #6a0572;
            font-weight: bold;
            transition: 0.3s;
        }
        nav a:hover {
            color: #ff8fab;
        }
        .section {
            padding: 100px 50px;
            text-align: center;
            position: relative;
            background: rgba(255, 255, 255, 0.9);
            margin: 80px auto;
            border-radius: 15px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
            max-width: 800px;
            opacity: 0;
            transform: translateY(50px);
            transition: opacity 0.8s, transform 0.8s;
        }
        .visible {
            opacity: 1;
            transform: translateY(0);
        }
        h1, h2 {
            text-shadow: 3px 3px 5px rgba(0,0,0,0.2);
        }
        .profile-img {
            width: 150px;
            border-radius: 50%;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        }
        .progress {
            width: 80%;
            height: 10px;
            background: #e9d5ff;
            border-radius: 5px;
            margin: 10px auto;
            overflow: hidden;
            position: relative;
        }
        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #c4b5fd, #fbcfe8);
            border-radius: 5px;
            transition: width 1s ease-in-out;
        }
        .gallery-img {
            width: 200px;
            border-radius: 10px;
            transition: transform 0.3s;
        }
        .gallery-img:hover {
            transform: scale(1.1);
        }
        .performance iframe {
            border-radius: 15px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#summary">Summary</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#achievements">Achievements</a></li>
                <li><a href="#piano">Piano Performances</a></li>
            </ul>
        </nav>
    </header>

    <section id="summary" class="section">
        <h1>Beatrice's Dance and Piano Journey</h1>
        <p>"All in, full out!" – A motto that defines my dynamic leadership, creativity, and adaptability in both dance and music.</p>
        <img src="beatrice_photo.jpg" alt="Beatrice" class="profile-img">
    </section>

    <section id="skills" class="section">
        <h2>Key Skills</h2>
        <ul>
            <li>🎬 Leadership <div class="progress"><div class="progress-bar" style="width: 90%;"></div></div></li>
            <li>⏰ Time Management <div class="progress"><div class="progress-bar" style="width: 85%;"></div></div></li>
            <li>🎨 Creativity <div class="progress"><div class="progress-bar" style="width: 95%;"></div></div></li>
            <li>🤝 Collaboration <div class="progress"><div class="progress-bar" style="width: 88%;"></div></div></li>
        </ul>
    </section>

    <section id="achievements" class="section">
        <h2>Achievements</h2>
        <div class="gallery">
            <img src="disneyland_photo.jpg" alt="Disneyland Tour" class="gallery-img">
            <img src="competition_photo.jpg" alt="CSTD Competition" class="gallery-img">
            <a href="video_url" target="_blank">Watch Performance Video</a>
        </div>
    </section>

    <section id="piano" class="section">
        <h2>Piano Performances</h2>
        <div class="performance">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/videoID" frameborder="0" allowfullscreen></iframe>
            <p>Performance at Kawai Recital Hall</p>
        </div>
    </section>

    <footer>
        <p>Contact me: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
    </footer>

    <script>
        $(document).ready(function() {
            $(window).on("scroll", function() {
                $(".section").each(function() {
                    let pos = $(this).offset().top;
                    let winTop = $(window).scrollTop();
                    if (pos < winTop + $(window).height() - 100) {
                        $(this).addClass("visible");
                    }
                });
            });
        });
    </script>
</body>
</html>
