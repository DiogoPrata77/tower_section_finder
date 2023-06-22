import sqlite3

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    from app.models import TowerSection, Shell
    db.create_all()
   
    if not TowerSection.query.all():
        # Initialize the database with some sample data
        section1 = TowerSection(section_code='TS003', length = 25)
        shell1 = Shell(shell_number=1, height=10, top_diameter=5, bottom_diameter=5, thickness=1, steel_density=7.8)
        shell2 = Shell(shell_number=2, height=15, top_diameter=5, bottom_diameter=7, thickness=1, steel_density=7.8)
        section1.shells.append(shell1)
        section1.shells.append(shell2)

        section2 = TowerSection(section_code='TS004', length = 30)
        shell3 = Shell(shell_number=3, height=12, top_diameter=7, bottom_diameter=7, thickness=1, steel_density=7.8)
        shell4 = Shell(shell_number=4, height=18, top_diameter=7, bottom_diameter=9, thickness=1, steel_density=7.8)
        section2.shells.append(shell3)
        section2.shells.append(shell4)

        db.session.add(section1)
        db.session.add(section2)
        db.session.commit()
