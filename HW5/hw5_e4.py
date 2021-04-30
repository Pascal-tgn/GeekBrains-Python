import os

input_file = r'e4_infile.txt'
output_file = r'e4_outfile.txt'
my_words = dict(
    One="Один",
    Two="Два",
    Three="Три",
    Four="Четыре"
)
if not os.path.exists(input_file):
    print(f"File {input_file} does not exist!")
    exit()
line = True
my_out = open(output_file, 'w')
with open(input_file, 'r') as my_source:
    while True:
        line = my_source.readline()
        if not line:
            break
        my_key = line.split()[0]
        my_out.write(line.replace(f"{my_key}", my_words.get(my_key)))
my_out.close()
