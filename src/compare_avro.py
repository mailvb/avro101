



import fastavro

import json
from src import file_utils

from deepdiff import DeepDiff
from pprint import pprint

def load_avro_data_file(file_name : str, abs_loc : bool):
    fn = file_name
    if not abs_loc:
        fn = file_utils.getFileLocation(file_name)
    with open(fn, "rb") as data_file:
        reader = fastavro.reader(data_file)
        # convert avro data to dict
        data = [d for d in reader]
        metadata = reader.metadata
        schema_from_file = json.loads(metadata['avro.schema'])
    return (data, schema_from_file)  # return tuple of


def readFiles(file_name_1, file_name_2, abs_loc : bool):
    # load employees_1.avro file
    result_1 = load_avro_data_file(file_name_1, abs_loc)
    data_1 = result_1[0]
    schema_1 = result_1[1]
    # read second file
    result_2 = load_avro_data_file(file_name_2, abs_loc)
    data_2 = result_2[0]
    schema_2 = result_2[1]
    # now let's compare schema 1 and schema 2

    # compare schema
    diff = DeepDiff(schema_1, schema_2, ignore_order=True)
    print("Schema difference")
    pprint(diff, indent=2)

    #now compare data
    diff = DeepDiff(data_1, data_2, ignore_order=True)
    print("Data difference")
    pprint(diff, indent=2)


if __name__ == "__main__":
    # accept locations of two avro files to compare as program input args
    file_name_1 = input("Enter first avro file name: ")
    file_name_2 = input("Enter second avro file name: ")
    readFiles(file_name_1, file_name_2, True)
    print("Done comparing avro files")