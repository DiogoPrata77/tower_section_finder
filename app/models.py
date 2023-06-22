from app.database import db

# Data Model TowerSection
class TowerSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section_code = db.Column(db.String(50), unique=True, nullable=False)
    length = db.Column(db.Float, nullable=False)
    shells = db.relationship('Shell', backref='tower_section', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<TowerSection {self.section_code}>"

# Data Model Shell
class Shell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shell_number = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    top_diameter = db.Column(db.Float, nullable=False)
    bottom_diameter = db.Column(db.Float, nullable=False)
    thickness = db.Column(db.Float, nullable=False)
    steel_density = db.Column(db.Float, nullable=False)
    tower_section_id = db.Column(db.Integer, db.ForeignKey('tower_section.id'), nullable=False)

    def __repr__(self):
        return f"<Shell {self.shell_number}>"
