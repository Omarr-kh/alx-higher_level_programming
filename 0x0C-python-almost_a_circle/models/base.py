#!/usr/bin/python3
"""Class definition for Base"""
import json


class Base:
    """Base Model
    Represents the base for all other classes in project

    private Class Attribute:
        __nb_objects: (int) Number of Instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base
        Args:
            id: (int) id of new Base
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries: (list) A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fname = cls.__name__ + ".json"
        with open(fname, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                temp = cls(1)
            else:
                temp = cls(1, 2)
            temp.update(**dictionary)
            return temp

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []
