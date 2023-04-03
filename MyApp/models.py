from MyApp import db


class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    count = db.Column(db.Integer)

    def __repr__(self):
        return f"Details('{self.name}', '{self.score}')"

class Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

    def __repr__(self):
        return f"Number('{self.number}')"
    