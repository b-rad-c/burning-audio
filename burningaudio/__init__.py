import subprocess


def main(threshold):
    duration = None
    args = ['ffmpeg', '-loglevel', 'quiet', '-f', 'avfoundation']

    if duration:
        args += ['-t', str(duration)]

    args += ['-i', ':1', '-f', 'u24le', '-ac', '1', '-ar', '1000', '-']

    process = subprocess.Popen(args, stdout=subprocess.PIPE)

    while True:
        buffer = process.stdout.read(3)
        if buffer:
            volume = int.from_bytes(buffer, 'little', signed=False) / 16_777_215
            if abs(.5 - volume) > threshold:
                yield volume
            else:
                yield -1.0

        else:
            break
