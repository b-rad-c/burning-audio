import subprocess


def detect_activity(input_device, threshold=.05, decay=.5, debug=False):
    """
    Detect activity on an audio device input
        yield None if no activity over threshold
        else yield decoded audio sample (python int from 24bit unsigned little endian)

    Audio signal is processed at a sample rate of 1khz

    :param input_device: str, name of input device to capture from, use list_devices to find name
    :param threshold: float, used to determine vocal activity from background noise
    :param decay: float, number of seconds after last detected activity to return to no activity state,
        used to smooth out gaps between words
    :param debug: bool, if True do not suppress ffmpeg logging, do not use unless actively debugging this will cause
        unexpected results when detecting audio activity
    :returns None
    """
    sample_rate = 1000
    decay_threshold = decay * sample_rate
    decaying = False
    current_decay = 0

    input_device = get_default_input() if input_device is None else input_device

    args = ['ffmpeg']
    if not debug:
        # suppress ffmpeg logging unless actively debugging
        args += ['-loglevel', 'quiet']
    args += ['-f', 'alsa', '-i', input_device, '-f', 'u24le', '-ac', '1', '-ar', str(sample_rate), '-']

    process = subprocess.Popen(args, stdout=subprocess.PIPE)

    try:
        while True:
            buffer = process.stdout.read(3)
            if buffer:
                value = int.from_bytes(buffer, 'little', signed=False)
                volume = value / 16777215
                if abs(.5 - volume) > threshold:
                    yield value
                    decaying = True

                elif decaying:
                    yield value
                    current_decay += 1
                    if current_decay > decay_threshold:
                        decaying = False
                        current_decay = 0
                else:
                    yield None

            else:
                raise ValueError('ffmpeg exited early, you probably supplied an invalid device, try debug mode')

    except KeyboardInterrupt:
        process.kill()


def list_devices():
    """list available audio devices
    :returns: string, result of running command 'arecord -L'
    """
    process = subprocess.Popen(['arecord', '-L'], stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read().decode('utf-8')


def get_default_input():
    """find default device input
    :returns: str, name of input device
    """

    for line in list_devices().splitlines():
        if line.startswith('default:'):
            return line.strip()

    raise ValueError('Could not find default input device.')
