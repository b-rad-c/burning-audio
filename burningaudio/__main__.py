import argparse
import burningaudio

parser = argparse.ArgumentParser()
parser.add_argument('--list_devices', '-l', action='store_true', help='List available devices and exit')
parser.add_argument('--input', '-i', help='name of input device to capture from, use --list_devices for discovery, '
                                          'system default is used if not supplied')
parser.add_argument('--default', action='store_true', help='print default device and exit.')
parser.add_argument('--threshold', '-t', type=float, default=.05, help='The volume threshold for signalling activity')
parser.add_argument('--decay', '-d', type=float, default=.5, help='number of seconds after last detected activity to '
                                                                  'return to no activity state, used to smooth out '
                                                                  'gaps between words')
parser.add_argument('--debug', action='store_true', help='Do not suppress ffmpeg logging, '
                                                         'do not use unless actively debugging')
args = parser.parse_args()

if args.list_devices:
    print(burningaudio.list_devices())

elif args.default:
    print(burningaudio.get_default_input())

else:
    for sample in burningaudio.detect_activity(args.input, args.threshold, args.decay, args.debug):
        if sample is None:
            print('not talking')

        else:
            print('talking')
