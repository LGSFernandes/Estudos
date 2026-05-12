from datetime import datetime, timezone
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, nullable = False)
    sobrenome = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = False)
    senha = db.Column(db.String, nullable = False)
    posts = db.relationship('Post', backref = 'user', lazy = True)
    post_comentarios = db.relationship('Comentario', backref = 'user', lazy = True)


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_envio = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    nome = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    assunto = db.Column(db.String, nullable = False)
    mensagem = db.Column(db.String, nullable = False)
    respondido = db.Column(db.Integer, default = 0)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_criacao = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    mensagem = db.Column(db.String, nullable = False)
    imagem = db.Column(db.String, nullable=False, default='default.png')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    comentarios = db.relationship('Comentario', backref = 'post', lazy = True)

    def msg_resumo(self):
        return f'{self.mensagem[:20]}...'


class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_criacao = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    comentario = db.Column(db.String, nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)