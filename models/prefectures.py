from api.database import db

class Prefecture(db.Model):
    __tablename__ = "prefectures"
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    name_kana = db.Column(db.String(80), nullable=False)
    def region_name(self):
        return self.Region.name

class Region(db.Model):
    __tablename__ = "regions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    name_kana = db.Column(db.String(80), nullable=False)