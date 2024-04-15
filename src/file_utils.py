


import os


def find_project_root(current_dir):
    """
    Recursively finds the project root directory from the given directory.
    Make sure to place "meta.inf" file in the project root directory.
    """
    if os.path.isfile(os.path.join(current_dir, "meta.inf")):
        return current_dir
    else:
        parent_dir = os.path.dirname(current_dir)
        # Base case: Reached the root directory
        if parent_dir == current_dir:
            raise FileNotFoundError("Project root not found.")
        return find_project_root(parent_dir)

def getFileLocation(fileName : str):
    cur_mod = os.path.dirname(__file__)
    project_root = find_project_root(cur_mod)
    res_path = project_root + "/target/" + fileName
    return res_path