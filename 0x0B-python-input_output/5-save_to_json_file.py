#!/usr/bin/python3
"""writes Object to text file, using a JSON """
def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, """
    with open(filename, "w") as f:
        json.dumps(my_obj ,f)

