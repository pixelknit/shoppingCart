import json
import os
from dataclasses import dataclass, field

@dataclass
class Fstream:
    name: str
    path: str
    extension: str
    data_file: str = field(init=False)

    @classmethod
    def load_json_file(cls, path)->dict:
        """
        Reads json files from a directory.

        Args:
            path: the path for the json file to read.
        Returns:
            Returns a hash map with the json structure.
        """
        with open(path, "rb") as data_file:
            cls.data_file = json.load(data_file)

        return cls.data_file

    @staticmethod
    def print_json_structure(data_file):
        for id, item in data_file["Items"].items():
            print(item)
