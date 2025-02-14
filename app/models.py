from app import db

class Shortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(255), unique=True, nullable=False)
    original = db.Column(db.String(2048), nullable=False) 
    visits = db.Column(db.Integer, default=0) 

    def __repr__(self):
        return f"<Shortener {self.short} -> {self.original}>"
