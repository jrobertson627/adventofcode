import csv
import re

def add_path(file_path, file_size):
    file_dict = {'path': file_path, 'size': file_size}
    return file_dict

def find_dirs_at_given_size():
    pass

def read_input(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        curr_path = ''
        all_dir = []
        all_files = []
        for row in csv_reader:
            # check if $
            if '$' in row:
                if 'cd' in row:
                    # check to see if going forward or back
                    # if going back then remove dir from the path
                    if '..' in row:
                        pass

                    # if forward add dir to curr path 
                    else:
                        dir = ''
                        curr_path += dir
                        # check if dir already in all_dir
                        if dir not in all_dir:
                            all_dir.append(dir)
                x = 0

            # check if size
            else:
                file_path = ''
                file_size = 0
                new_dict = add_path(file_path, file_size)
                all_files.append(new_dict)
    return all_dir, all_files

def main():
    read_input("input.txt")

if __name__ == "__main__":
    main()