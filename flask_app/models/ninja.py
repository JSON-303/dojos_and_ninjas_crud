from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class Ninja:
    _db = "dojos_and_ninjas"
    """THIS CONSTRUCTOR FUNCTION ACCEPTS A DICTIONARY AS INPUT"""

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at_id = data["created_at"]
        self.updated_at = data["updated_at"]

    """CREATE A CLASS METHOD FOR EACH CRUD QUERY"""

    @classmethod
    def all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        list_of_dicts = connectToMySQL(Ninja._db).query_db(query)
        pprint(list_of_dicts)
        ninjas = []
        for each_dict in list_of_dicts:
            ninja = Ninja(each_dict)
            ninjas.append(ninja)
        return ninjas

    @classmethod
    def find_by_id(cls, ninja_id):
        """FINDS ONE NINJA BY ID IN THE DATABASE"""
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        data = {"ninja_id": ninja_id}
        list_of_dicts = connectToMySQL(Ninja._db).query_db(query, data)
        ninja = Ninja(list_of_dicts[0])
        return ninja

    @classmethod
    def create(cls, form_data):
        """CREATES A NEW NINJA FROM A FORM"""
        query = """
        INSERT INTO ninjas
        (first_name, last_name, age, dojo_id)
        VALUES
        (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        ninja_id = connectToMySQL(Ninja._db).query_db(query, form_data)
        return ninja_id
