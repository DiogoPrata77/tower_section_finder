from flask import Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.models import TowerSection, Shell
from app.database import db
from main import app
import sys

# Create a blueprint for the tower section endpoints
tower_section_bp = Blueprint('tower_section_bp', __name__)
api = Api(tower_section_bp)

# Define the fields for serialization using Flask-RESTful's marshal_with decorator
shell_fields = {
    'id': fields.Integer,
    'shell_number': fields.Integer,
    'height': fields.Float,
    'top_diameter': fields.Float,
    'bottom_diameter': fields.Float,
    'thickness': fields.Float,
    'steel_density': fields.Float
}

tower_section_fields = {
    'id': fields.Integer(attribute='id'),
    'section_code': fields.String,
    'length' :fields.Float,
    'shells': fields.List(fields.Nested(shell_fields))
}

# Define the TowerSectionResource class to handle the tower section endpoints
class TowerSectionResource(Resource):
    # GET method to retrieve a tower section by its ID
    @marshal_with(tower_section_fields, envelope='data')
    def get(self, id):
        #print(" GET METHOD")
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='Section_id is required')
        args = parser.parse_args(strict=True)

        id = args['id']
        #print(id)
       
        app.logger.info(id)
        tower_section = TowerSection.query.get(id)
        if not tower_section:
            return {'message': 'Tower section not found'}, 404
        return tower_section

    # POST method to create a new tower section
    @marshal_with(tower_section_fields, envelope='data')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('section_code', type=str, required=True, help='Section code is required')
        parser.add_argument('length', type = float, required = True, help='Length  is required')
        parser.add_argument('shells', action='append', type=dict, required=True, help='Shells are required')
        args = parser.parse_args(strict=True)

        section_code = args['section_code']
        length = args['length']
        shells = args['shells']

        # Create a new TowerSection instance
        tower_section = TowerSection(section_code=section_code, length = length)
        
        # Create and associate Shell instances with the tower section
        for shell_data in shells:
            shell = Shell(**shell_data)
            tower_section.shells.append(shell)
        # Add the tower section to the database
        db.session.add(tower_section)
        db.session.commit()

        return tower_section, 201

    # DELETE method to delete a tower section by its ID
    """ def delete(self, tower_id):
        tower_section = TowerSection.query.get(id)
        if not tower_section:
            return {'message': 'Tower section not found'}, 404

        db.session.delete(tower_section)
        db.session.commit()

        return {'message': 'Tower section deleted successfully'}, 200"""

api.add_resource(TowerSectionResource, '/tower-sections', '/tower-sections/<int:tower_section_id>')
