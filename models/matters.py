from api.database import db

class Matter(db.Model):
    __tablename__ = "matters" 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    unit_price = db.Column(db.String(120), unique=True, nullable=False)
    format = db.Column(db.String(80), nullable=False)
    area = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    operation_time = db.Column(db.String(80), nullable=False)
    payday = db.Column(db.String(80), nullable=False)
    details = db.Column(db.String(80), nullable=False)
    nearest_station = db.Column(db.String(80), nullable=False)
    negotiations = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Matter {self.name}>'

class MatterProgrammingLanguage(db.Model):
    __tablename__ = "matters_programming_languages"
    id = db.Column(db.Integer, primary_key=True)
    matter_id = db.Column(db.Integer, db.ForeignKey("matters.id"), nullable=False)
    programming_language_id = db.Column(db.Integer, db.ForeignKey("programming_languages.id"), nullable=False)


class MatterTitleChip(db.Model):
    __tablename__ = "matters_title_chips"
    id = db.Column(db.Integer, primary_key=True)
    matter_id = db.Column(db.Integer, db.ForeignKey("matters.id"), nullable=False)
    title_chip_id = db.Column(db.Integer, db.ForeignKey("title_chips.id"), nullable=False)


class ProgrammingLanguage(db.Model):
    __tablename__ = "programming_languages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class TitleChip(db.Model):
    __tablename__ = "title_chips"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
