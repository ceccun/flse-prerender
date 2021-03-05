import time
import os
import shutil
import glob
from distutils.dir_util import copy_tree

time.sleep(2)


def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


def renderAll():
    shutil.rmtree("files/dist")
    os.mkdir("files/dist")
    fromDir = "files/src"
    toDir = "files/dist"
    copy_tree(fromDir, toDir)
    files = get_filepaths("files\dist")
    for file in files:
        print("hi")
    print(arr)


print("===================================================================")
print("")
print("FLSE Prerender 1.5.1")
print("")
print("")
print("Before you start, make sure you know the following:")
print("- flseimports must not contain '../' (relative references), if they do, it will render the prerender unstable. All references must either be from root or with their full URL.")
print("- This is supported with FLSE v1.5.1, if you need a later version, check GitHub (stel-la/flse-prerender) for a later version.")
print("- Languages cannot be prerendered, instead, we will inject miniFLSE to handle languages.")
print("")
print("Choose what you want to do?")
print("[1] Prerender all files in files/src/ now")
print("[2] About this tool")
answer1 = input("Enter an option: ")
if (answer1 == '2'):
    print("Developed at Ceccun by Ejaz Ali & Nathaniel Hofer \nSupports FLSE 1.5.1\nFLSE is a web framework project making it easier for vanilla developers to get to market faster with an engine designed to be fast.")
if (answer1 == '1'):
    renderAll()
