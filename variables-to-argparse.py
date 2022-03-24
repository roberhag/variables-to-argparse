from sys import stdin, argv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--no-underscore-to-dash", action="store_true", help="Use this if you wish to preserve underscores "
                                                                         "in the argument name (default uses dash).")
parser.add_argument("-i", "--input", type=str, default=None, help="Input filename (default use standard input)")
parser.add_argument("-o", "--output", type=str, default=None, help="Output filename (default print to standard output)")
args = parser.parse_args()

underscore_to_dash = not args.no_underscore_to_dash
input_file = args.input

arguments_str = ""
assignment_str = ""
global_whitespace = None

if input_file:
    input_file = open(input_file)
else:
    print("Input the section of Python code with variable assignments.\nReads input until EOF or two newlines.")
    input_file = stdin

break_next = False
for line in input_file:
    stripped_line = line.strip()
    if len(stripped_line) == 0:  # Logic to identify two consecutive newlines
        if break_next:
            break
        else:
            break_next = True
    else:
        break_next = False
    if "#" in stripped_line:
        code, comment = stripped_line.split("#")
    else:
        code = stripped_line
        comment = ""
    if "=" not in code:  # Not an assignment, leave line as it is.
        assignment_str += line
        continue
    
    # Preserve whitespace
    len_diff = len(line.rstrip()) - len(stripped_line)
    whitespace = line[:len_diff]
    if global_whitespace is None:
        global_whitespace = whitespace
    else:
        if global_whitespace != whitespace:
            print(f"Warning: Encountered line with different whitespace {whitespace} (length {len(whitespace)}) != "
                  f"global {global_whitespace} (length {len(global_whitespace)})")
    
    variable, default = (x.strip() for x in code.split("="))
    if underscore_to_dash:
        argname = variable.replace("_", "-")
    else:
        argname = variable
    
    arguments_str += f"{whitespace}parser.add_argument('--{argname}', default={default}, " \
                     f"type={type(eval(default)).__name__}, help='{comment.strip()}')\n"
    assignment_str += f"{whitespace}{variable} = args.{variable}\n"

if global_whitespace is None:
    global_whitespace = ""

output_str = f"""
{global_whitespace}import argparse\n
{global_whitespace}parser = argparse.ArgumentParser()
{arguments_str}\n
{global_whitespace}args = parser.parse_args()\n
{assignment_str}
"""

if args.output:
    with open(args.output, "w") as output_file:
        output_file.write(output_str)
else:
    print(output_str)
