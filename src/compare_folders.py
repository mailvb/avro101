import os

from src import compare_json as cj

# ANSI escape code for red color
red_color_code = '\033[91m'
green_color_code = '\033[92m'

# ANSI escape code to reset color to default
reset_color_code = '\033[0m'

# return dict files in the folder
# file name starts with 1_ or 2_ etc.
def list_files(folder_name : str) -> dict[str, str]:
    file_names = os.listdir(folder_name)
    # extract string before the first occurrence of _
    file_dict : dict[str,str] = {file_name.split("_")[0]: file_name for file_name in file_names}
    return file_dict
    
    


if __name__ == "__main__":
    # accept folder locations

    folder_name_1 = input("Enter first folder loc: ")
    folder_name_2 = input("Enter second folder loc: ")
    folder_dict_1 = list_files(folder_name_1)
    folder_dict_2 = list_files(folder_name_2)
    for key in sorted(folder_dict_1, key=lambda x: int(x)):
        file_name_1 = folder_dict_1[key]
        file_name_2 = folder_dict_2[key]
        print("============================ START ============================")
        if file_name_1 != file_name_2:
            print(red_color_code )
            print(f"File Names Not the same!!! => {folder_dict_1[key]} and {folder_dict_2[key]} ")
            print(reset_color_code)
        else:
            print(f"|| comparing {file_name_1} ||")
            if key == '11':
                cj.readFiles(folder_name_1 + file_name_1, folder_name_2 + file_name_2, True, True)
            else:
                cj.readFiles(folder_name_1 + file_name_1, folder_name_2 + file_name_2, True)
        print("============================ END ============================")
