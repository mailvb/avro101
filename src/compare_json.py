
import json
from src import file_utils

from deepdiff import DeepDiff
from pprint import pprint

def load_json_file(file_name : str, abs_loc : bool):
    fn = file_name
    if not abs_loc:
        fn = file_utils.getFileLocation(file_name)
    # time to read json file
    with open(fn, "r") as data_file:
        data = json.load(data_file)
        return data
    
def readFiles(file_name_1, file_name_2, abs_loc : bool):
    # load employees_1.avro file
    data_1 = load_json_file(file_name_1, abs_loc)
    pprint("========= Data 1 =========")
    pprint(data_1, indent=2, width=180)
    # read second file
    data_2 = load_json_file(file_name_2, abs_loc)
    pprint("========= Data 2 =========")
    pprint(data_2, indent=2, width=180)

    # load ignore
    ignore = load_json_file("excludes.json", False)

    pprint("========= Ignore =========")
    print("Ignore: ", ignore)
    # now let's compare data 1 and data 2
    diff = DeepDiff(data_1, data_2, exclude_paths=ignore, ignore_order=True)
    pprint("========= Difference =========")
    pprint(diff, indent=2, width=180)
    pprint("========= End =========")

if __name__ == "__main__":
    # accept locations of two json files to compare as program input args
    #file_name_1 = "widget_1.json"
    #file_name_2 = "widget_2.json"
    #readFiles(file_name_1, file_name_2, False)

    file_name_1 = input("Enter first json file loc: ")
    file_name_2 = input("Enter second json file loc: ")
    readFiles(file_name_1, file_name_2, True)
