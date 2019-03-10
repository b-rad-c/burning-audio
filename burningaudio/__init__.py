import subprocess


def detect_activity(threshold, index, decay=.5):
    """
    Detect activity on an audio device input
        yield None if no activity over threshold
        else yield decoded audio sample (python int from 24bit unsigned little endian)

    Audio signal is processed at a sample rate of 1khz

    :param threshold: float, used to determine vocal activity from background noise
    :param index: int, the audio device index to read
    :param decay: float, number of seconds after last detected activity to return to no activity state,
        used to smooth out gaps between words
    :returns None
    """
    sample_rate = 1000
    decay_threshold = decay * sample_rate
    decaying = False
    current_decay = 0

    # reference: https://ffmpeg.org/ffmpeg-devices.html#avfoundation
    args = ['ffmpeg', '-loglevel', 'quiet', '-f', 'avfoundation',
            '-i', f':{index}', '-f', 'u24le', '-ac', '1', '-ar', str(sample_rate), '-']

    process = subprocess.Popen(args, stdout=subprocess.PIPE)

    try:
        while True:
            buffer = process.stdout.read(3)
            if buffer:
                value = int.from_bytes(buffer, 'little', signed=False)
                volume = value / 16_777_215
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
                raise ValueError('ffmpeg exited early, you have probably supplied an invalid device index.')
            
    except KeyboardInterrupt:
        process.kill()


def list_devices():
    args = ['ffmpeg', '-f', 'avfoundation', '-list_devices', 'true', '-i', '""']
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    process.wait()
