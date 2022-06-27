from Newsletter import db


class Users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(45), unique=True, nullable=False)
    role = db.Column(db.String(100))

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"{self.email, self.password, self.role}"
