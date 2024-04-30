
import json
from src import file_utils

from deepdiff import DeepDiff
from deepdiff.helper import CannotCompare
from pprint import pprint

# create a dict to hold file name to element name
id_elem = "idnameplaceholder"

# ANSI escape code for red color
red_color_code = '\033[91m'
green_color_code = '\033[92m'

# ANSI escape code to reset color to default
reset_color_code = '\033[0m'


def compare_func(x, y, level=None):
    try:
        #print(x)
        return x[id_elem] == y[id_elem]
    except Exception:
        raise CannotCompare() from None

def load_json_file(file_name : str, abs_loc : bool):
    fn = file_name
    if not abs_loc:
        fn = file_utils.getFileLocation(file_name)
    # time to read json file
    with open(fn, "r") as data_file:
        data = json.load(data_file)
        return data


# load ignore
ignore = load_json_file("excludes.json", False)


def readFiles(file_name_1, file_name_2, abs_loc : bool, use_compre_dict = False):
    is_error = False
    # load employees_1.avro file
    try:
        data_1 = load_json_file(file_name_1, abs_loc)
    except Exception as e:
        is_error = True

    # read second file
    if not is_error:
        try:
            data_2 = load_json_file(file_name_2, abs_loc)
        except Exception as e:
            is_error = True

    if is_error:
        print(red_color_code )
        print("Error reading files")
        print(reset_color_code)
    else:
        # now let's compare data 1 and data 2
        if use_compre_dict:
            diff = DeepDiff(data_1, data_2, exclude_paths=ignore, ignore_order=True, iterable_compare_func=compare_func)
        else:
            diff = DeepDiff(data_1, data_2, exclude_paths=ignore, ignore_order=True)
        pprint("============================ DIFF ============================")
        if diff:
            print(red_color_code )
        else:
            print(green_color_code)
        pprint(diff, indent=2, width=180)
        print(reset_color_code)
        


if __name__ == "__main__":
    # accept locations of two json files to compare as program input args
    #file_name_1 = "widget_1.json"
    #file_name_2 = "widget_2.json"
    #readFiles(file_name_1, file_name_2, False)

    file_name_1 = input("Enter first json file loc: ")
    file_name_2 = input("Enter second json file loc: ")
    readFiles(file_name_1, file_name_2, True)