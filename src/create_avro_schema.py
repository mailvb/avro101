
import json
from fastavro import parse_schema



def load_avro_schema_from_file(file_name : str):
    with open(file_name, "r") as schema_file:
        schema_dict = json.load(schema_file)
    schema = parse_schema(schema_dict)
    return schema


def print_avro_schema(schema):
    print(schema)




if __name__ == "__main__":
    schema = load_avro_schema_from_file("employee.json")
    print_avro_schema(schema)





