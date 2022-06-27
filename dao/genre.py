from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        ent = Genre(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, data):
        genre = self.get_one(data.get("id"))
        genre.name = data.get("name")

        self.session.add(genre)
        self.session.commit()
