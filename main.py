
import os
import sys
from shutil import copyfile
import argparse



def find_files(source_dir):
    """
    function to traverse source dir for all files
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
    func to copy files to target dir
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


def get_filter_list(filter_txt):
    filter_list = []
    with open(filter_txt) as f:
        for l in f:
            l_parsed = l.rstrip().replace('-', '')
            filter_list.append(l_parsed)
    
    return filter_list

def move_filtered_files(source_dir, target_dir, filter_str):
    all_files = find_files(source_dir)
    found_files = filter_files(filter_str, all_files)
    copy_files(found_files, target_dir)


def copy_filtered_files_multi(source_dir, target_dir, filter_list):
    for filter_str in filter_list:
        move_filtered_files(source_dir, target_dir, filter_str)


# def main(source_dir, target_dir, filter_str):
#     # move_filtered_files(source_dir, target_dir, filter_str)
#     # move_filtered_files(
#     #     r"C:\Users\jandl\OneDrive\Documents\Python Projects\File searcher",
#     #     r'C:\Users\jandl\OneDrive\Documents\Python Projects\File searcher\feed_me',
#     #     "apple"
#     # )

def main():
    filter_list = get_filter_list(r"\\group.iqep.com\ma\user\ajandl\My Documents\Data\For customer\Lasertel\19-05-15 More Surfscan\filter_list.txt")
    print(filter_list)

    
if __name__ == '__main__':
    main()
    # parser = argparse.ArgumentParser()
    # parser.add_argument('source_dir', help="Define the directory with files to work on")
    # parser.add_argument('target_dir', help="Define the target directory")
    # parser.add_argument('filter_str')
    # args = parser.parse_args()
    # main(args.source_dir, args.target_dir, args.filter_str)
