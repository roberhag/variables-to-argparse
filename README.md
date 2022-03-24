# Variables to Argparse
Given a Python code with variable assignments, turn each assignment into argparse command line arguments with a default value.

Have you ever created a wonderful Python script where all the parameters are defined in the code and thought
"Hey, it would be really nice if there was a way to translate hardcoded variable assignments into pretty command line arguments"?
Look no further.

## Usage

```shell script
python variables-to-argparse.py [-i inputfile.py] [-o outputfile.py] [--no-underscore-to-dash]
```

If the input file is not given, will read from standard input until EOF or until two consecutive empty lines.
If the output file is not given, will print to standard output. 

## Notes and details

Turns #comments into argument help text.

The type of the argument is inferred from the provided default.
Remember to add a dot `.` at the end of numbers that can be floats.

Tries to preserve whitespace, newlines and indentation.
Preserves lines that do not contain the "=" sign as they are.

All lines containing "=" will be attempted converted to an argparse argument. 
Hence this script can interfere with the structure and logic of your code.

Not good for running on your whole Python file, because variables-to-argparse does not identify
the area of variable assignments. I suggest you copy-paste the lines where you assign variables.


## Example

```shell script
$ python variables-to-argparse.py
Input the section of Python code with variable assignments.
Reads input until EOF or two newlines.

# Here follows example input:

fs = 48000  # Sample rate (Hz)

base_freq = 100.  # Base frequency (Hz)
bpm = 120  # Beats per minute


# Here follows the output:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--fs', default=48000, type=int, help='Sample rate (Hz)')
parser.add_argument('--base-freq', default=100., type=float, help='Base frequency (Hz)')
parser.add_argument('--bpm', default=120, type=int, help='Beats per minute')


args = parser.parse_args()

fs = args.fs

base_freq = args.base_freq
bpm = args.bpm

```
