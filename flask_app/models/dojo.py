from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint


class Dojo:
    _db = "dojos_and_ninjas"
    """THIS CONSTRUCTOR FUNCTION ACCEPTS A DICTIONARY AS INPUT"""

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    """ CREATE A CLASS METHOD FOR EACH CRUD QUERY"""

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        list_of_dicts = connectToMySQL(Dojo._db).query_db(query)
        pprint(list_of_dicts)
        dojos = []
        for each_dojo in list_of_dicts:
            dojo = Dojo(each_dojo)
            dojos.append(dojo)
        return dojos

    @classmethod
    def find_by_id_with_ninjas(cls, dojo_id):
        """FINDS ONE DOJO BY ID AND RELATED CHILD NINJAS IN THE DATABASE"""
        query = """
        SELECT * FROM dojos
        JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(dojo_id)s;
        """
        data = {"dojo_id": dojo_id}
        list_of_dicts = connectToMySQL(Dojo._db).query_db(query, data)

        if not list_of_dicts:
            return []

        pprint(list_of_dicts)

        dojo = Dojo(list_of_dicts[0])
        print(dojo.name)
        for each_dict in list_of_dicts:
            ninja_data = {
                "id": each_dict["ninjas.id"],
                "first_name": each_dict["first_name"],
                "last_name": each_dict["last_name"],
                "age": each_dict["age"],
                "dojo_id": each_dict["dojo_id"],
                "created_at": each_dict["ninjas.created_at"],
                "updated_at": each_dict["ninjas.updated_at"],
            }
            ninja = Ninja(ninja_data)
            dojo.ninjas.append(ninja)
        return dojo

    @classmethod
    def find_by_id(cls, dojo_id):
        """FINDS ONE NINJA BY ID IN THE DATABASE"""
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        data = {"dojo_id": dojo_id}
        list_of_dicts = connectToMySQL(Dojo._db).query_db(query, data)
        dojo = Dojo(list_of_dicts[0])
        return dojo

    @classmethod
    def create_dojo(cls, form_data):
        """CREATES A NEW NINJA FROM A FORM"""
        query = """
        INSERT INTO dojos
        (name)
        VALUES
        (%(name)s);
        """
        dojo_id = connectToMySQL(Dojo._db).query_db(query, form_data)
        return dojo_id
