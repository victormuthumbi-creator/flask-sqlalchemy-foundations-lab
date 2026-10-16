# server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Earthquake(db.Model):
    """A single recorded earthquake event."""

    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def to_dict(self):
        """Serialize the earthquake to a JSON-friendly dict."""
        return {
            "id": self.id,
            "location": self.location,
            "magnitude": self.magnitude,
            "year": self.year,
        }

    def __repr__(self):
        # Example: <Earthquake 1, 9.5, Chile, 1960>
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
