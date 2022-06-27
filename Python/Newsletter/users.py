from Newsletter import db


class Newsletter(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    email = db.Column(db.String(100))

    def __init__(self, email):
       self.email = email

    def __repr__(self):
        return f"{self.email}"


