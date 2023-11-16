#!/usr/bin/python3
""" base module """
import json
import csv


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ doc """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ doc """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ doc """
        filename = cls.__name__ + ".json"
        listDic = []
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                for instance in list_objs:
                    listDic.append(instance.to_dictionary())
                f.write(cls.to_json_string(listDic))

    @staticmethod
    def from_json_string(json_string):
        """ doc """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ doc """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ doc """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                dics = cls.from_json_string(f.read())
                instances = []
                for dic in dics:
                    instances.append(cls.create(**dic))
                return instances
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ doc """
        filename = cls.__name__ + ".csv"
        listDic = []
        with open(filename, 'w') as f:
            fd = csv.writer(f, delimiter=',')
            if list_objs is None:
                fd.writerow([])
            else:
                fd.writerow(list(list_objs[0].to_dictionary().keys()))
                for instance in list_objs:
                    fd.writerow(list(instance.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """ doc """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                fd = csv.reader(f, delimiter=',')
                instances = []
                sw = 0
                for row in fd:
                    if sw == 0:
                        keys = row
                        sw = 1
                    else:
                        row = map(lambda x: int(x), row[:])
                        instances.append(cls.create(**dict(zip(keys, row))))
                return instances
        except:
            raise
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ doc """
