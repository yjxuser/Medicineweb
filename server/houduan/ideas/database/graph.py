from ideas import db


class Graph(db.Model):
    __tablename__ = "graph"
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.String(255))
    property = db.Column(db.String(255))
    y = db.Column(db.String(255))

    def __init__(self, x, property, y):
        self.property = property
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Graph %r -> %r>' % (self.x, self.y)

