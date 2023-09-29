from app import db


class User(db.Model):
    uuid = db.Column(db.String, primary_key=True, unique=True, index=True)  # uuid inserts in auth function
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    todo = db.relationship('Todo', backref='user', lazy='dynamic', cascade="all, delete-orphan")


class Todo(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.uuid'))
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    title = db.Column(db.String, default=None)
    text = db.Column(db.String, default=None)
