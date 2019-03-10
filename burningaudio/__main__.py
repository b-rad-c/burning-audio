import argparse
import burningaudio

parser = argparse.ArgumentParser()
parser.add_argument('--list_devices', '-l', action='store_true', help='List devices available to ffmpeg and exit')
parser.add_argument('--threshold', '-t', type=float, default=.05, help='The volume threshold for signalling activity')
parser.add_argument('--index', '-i', default='1', help='The index of the audio input, use --list_devices to discover')
args = parser.parse_args()

if args.list_devices:
    burningaudio.list_devices()

else:
    for sample in burningaudio.main(args.threshold, args.index):
        if sample == -1:
            print('no talking')
        else:
            print(f'talking: {sample}')
