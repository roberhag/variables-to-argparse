
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--fs', default=48000, type=int, help='Sample rate (Hz)')
parser.add_argument('--base-freq', default=100., type=float, help='Base frequency (Hz)')
parser.add_argument('--bpm', default=120, type=int, help='Beats per minute')


args = parser.parse_args()

# Here follows example input:

fs = args.fs

base_freq = args.base_freq
bpm = args.bpm

