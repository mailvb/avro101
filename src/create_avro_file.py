
import os
import fastavro

from src import create_avro_schema
from src import file_utils

# Sample data
data = [
    {"id": 1, "name": "Alice", "age": 25, "department": "Sales", "salary": 50000.0,
     "address": {"street": "123 Main St", "city": "Anytown", "zip": "12345"},
     "manager": {"id": 2, "name": "Bob", "age": 30, "department": "Marketing", "salary": 60000.01}, "manager": None},
    {"id": 2, "name": "Bob", "age": 30, "department": "Marketing", "salary": 60000.02,
     "address": {"street": "456 Elm St", "city": "Anycity", "zip": "67890"},
     "manager": None},
    {"id": 3, "name": "Charlie", "age": 35, "department": "Engineering", "salary": 70000.0,
     "address": {"street": "789 Oak St", "city": "Anystate", "zip": "54321"},
     "manager": {"id": 1, "name": "Alice", "age": 25, "department": "Sales", "salary": 50000.1}, "manager": None},
    {"id": 4, "name": "David", "age": 40, "department": "HR", "salary": 80000.0,
     "address": {"street": "987 Pine St", "city": "Anycity", "zip": "13579"},
     "manager": None},
    {"id": 5, "name": "Eve", "age": 45, "department": "Finance", "salary": 90000.1,
     "address": {"street": "654 Cedar St", "city": "Anystate", "zip": "24680"},
     "manager": {"id": 2, "name": "Bob", "age": 30, "department": "Marketing", "salary": 60000.1}, "manager": None}
]







def create_avro_file(schema, data, file_name : str):
    fn = file_utils.getFileLocation(file_name)
    with open(fn, "wb") as out:
        fastavro.writer(out, schema, data)

if __name__ == "__main__":
    my_schema = create_avro_schema.load_avro_schema_from_file("employee.json")
    # output avro file in project target folder
    create_avro_file(my_schema, data, "employees_2.avro")
    print("Avro file created successfully")


