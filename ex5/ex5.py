import argparse

parser = argparse.ArgumentParser(description='sth like [cat] command.')
parser.add_argument(
    'input_file', nargs='*', help='The name of input file(s)'
)
parser.add_argument(
    '->', '--output_file', nargs='?', help='The name of output file'
)
parser.add_argument(
    '-cl', '--clear', nargs='?', help='Clear the file.'
)
argv = parser.parse_args()

def print_file(file_name):
    with open(file_name) as f:
        for line in f:
            print(line)

def cat_file(file_list, output_file):
    with open(output_file, 'a') as out_f:
        for file in file_list:
            with open(file) as in_f:
                content = in_f.read()
            out_f.write(content + '\n')

def clear_file(file_name):
    with open(file_name, 'w') as f:
        f.write('')

file_list = argv.input_file
output_file = argv.output_file
cl_file = argv.clear

if cl_file:
    clear_file(cl_file)

elif output_file and file_list:
    cat_file(file_list, output_file)
    print_file(output_file)

elif file_list:
    for file in file_list:
        print_file(file)

else:
    print('Input "python ex5.py -h" to get help.')
