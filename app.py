from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'
db = SQLAlchemy(app)


# music_list = [
#     {
#         "id": 1,
#         "music_image": "/static/images/Sia 2_.jpg",
#         "music_title": "Elastic Heart",
#         "music_artist": "Sia"
#     },
#     {
#         "id": 2,
#         "music_image": "/static/images/Sia 2_.jpg",
#         "music_title": "Never Give Up",
#         "music_artist": "Sia"
#     },
#     {
#         "id": 3,
#         "music_image": "/static/images/Sia 2_.jpg",
#         "music_title": "Never Give Up",
#         "music_artist": "Sia"
#     },
#     {
#         "id": 4,
#         "music_image": "/static/images/Sia 2_.jpg",
#         "music_title": "Never Give Up",
#         "music_artist": "Sia"
#     },
#     {
#         "id": 5,
#         "music_image": "/static/images/Sia 2_.jpg",
#         "music_title": "Never Give Up",
#         "music_artist": "Sia"
#     }
# ]

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    album_image = db.Column(db.String, nullable=False)

@app.route('/')
def index():
    music_list = Music.query.all()
    return render_template('index.html', music_item=music_list)

@app.route('/add_music', methods=['POST', 'GET'])
def add_music():
    if request.method == "POST":
        title =request.form.get("title")
        artist =request.form.get("artist")
        album_image =request.form.get("album_image")

        new_music = Music(title=title, artist=artist, album_image=album_image)
        db.session.add(new_music)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template ("add_music.html")       



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
