my_filename = r"e2_infile.txt"
try:
    with open(my_filename) as my_file:
        my_lines = my_file.readlines()
        print(f"Total lines in file: {len(my_lines)}")
        for my_line in my_lines:
            print(f"{len(my_line.split())} : {my_line}", end='')
except FileNotFoundError:
    print("FILE NOT FOUND!")
    print(f"Please create a file {my_filename} and populate it with text lines")
