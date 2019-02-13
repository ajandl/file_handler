
import os
import sys
from shutil import copyfile
import argparse


def find_files(source_dir):
    """
    function to travers source dir for all files
        input: string with search dir path
        return: list with all file names
    """
    file_list = []
    for dir_path, _, file_name in os.walk(source_dir):
        for f in file_name:
            file_list.append(os.path.join(dir_path, f))
    
    return file_list


def filter_files(search_str, file_list):
    """
    func to search list of files for files with matching string
        input: list of all file names
        return: list with file names containing the search string
    """

    found_list = []
    for elem in file_list:
        _, file_name = os.path.split(elem)
        if search_str.lower() in file_name.lower():
            found_list.append(elem)
    
    return found_list


def copy_files(found_files, targ_dir):
    """
    func to copy files to targe dir
        input: list of filtered file names 
        return: null
    """
    # if not os.path.isdir(targ_dir):
    os.makedirs(targ_dir, exist_ok=True)

    for f in found_files:
        new_path = os.path.join(targ_dir, os.path.basename(f))
        try:
            copyfile(f, new_path)
        except:
            print("Could not copy: ", f)


def move_filtered_files(source_dir, target_dir, filter_str):
    all_files = find_files(source_dir)
    found_files = filter_files(filter_str, all_files)
    copy_files(found_files, target_dir)


def main():
    move_filtered_files(args.source_dir, args.target_dir, args.filter_str)
    # move_filtered_files(
    #     r"C:\Users\jandl\OneDrive\Documents\Python Projects\File searcher",
    #     r'C:\Users\jandl\OneDrive\Documents\Python Projects\File searcher\feed_me',
    #     "apple"
    # )

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source_dir')
    parser.add_argument('target_dir', help="Define the target directory")
    parser.add_argument('filter_str')
    args = parser.parse_args()
    main()
