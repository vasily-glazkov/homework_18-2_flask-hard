from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from container import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        director = director_service.get_one(rid)
        return director_schema.dump(director), 200
