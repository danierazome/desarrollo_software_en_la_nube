from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class VideoConversion(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    video = db.Column(db.String(200))
    video_name = db.Column(db.String(40))
    original_format = db.Column(db.String(40))
    upload_date = db.Column(db.Date)
    video_converted = db.Column(db.String(200))
    conversion_format = db.Column(db.String(40))
    conversion_date = db.Column(db.Date)
    state = db.Column(db.String(40))

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(60))
    password = db.Column(db.String(60))
    email = db.Column(db.String(60))
    video_conversions = db.relationship(
        "VideoConversion", backref="usuario", lazy=True)
