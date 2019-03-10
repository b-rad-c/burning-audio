import argparse
import burningaudio

parser = argparse.ArgumentParser()
parser.add_argument('--threshold', '-t', type=float, default=.05)
args = parser.parse_args()

for sample in burningaudio.main(args.threshold):
    if sample == -1:
        print('no talking')
    else:
        print(f'talking: {sample}')
