my_str = ' '
with open(r'e1_outfile.txt', 'w') as my_file:
    while my_str != '':
        my_str = input("Please enter new line. Press without entering to stop >>>")
        my_file.write(f"{my_str}\n")
