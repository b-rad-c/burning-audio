# Burning Audio
#### A utility to detect when there is activity from an audio input.

The purpose of this project is to control art installations when someone is talking on a microphone, I'll be using it in a burning man project; hence the name.

Currently this is just a proof of concept, the plan is to eventually use this on a razz pi but I don't have a mic to plug into my raspberry right now so it is only compatible with the built in microphone on an osx laptop.

Later versions will send signals to microcontrollers (or pass in arbitrary callback functions) rather than print info to stdout.

### Requirements
python 3.6+ (i use f-strings and you should too)

ffmpeg

osx w/ built in microphone

### Usage
    python -m burningaudio -t .05
    
    talking: 0.4126607425606693
    talking: 0.38853766849861554
    talking: 0.5841856947055873
    talking: 0.4328830500175387
    talking: 0.5600863432935681
    talking: 0.5549066397492075
    no talking
    no talking
    talking: 0.43062701407831994
    talking: 0.4137211092544263
    no talking
    no talking
    no talking
    talking: 0.5537803503143996
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    
### Discover devices
    (venv) Brads-MBP:burningaudio brad$ python -m burningaudio -l
    ffmpeg version 4.0 Copyright (c) 2000-2018 the FFmpeg developers
      built with Apple LLVM version 9.1.0 (clang-902.0.39.1)
      configuration: --prefix=/usr/local/Cellar/ffmpeg/4.0 --enable-shared --enable-pthreads --enable-version3 --enable-hardcoded-tables --enable-avresample --cc=clang --host-cflags= --host-ldflags= --enable-gpl --enable-libmp3lame --enable-libx264 --enable-libxvid --enable-opencl --enable-videotoolbox --disable-lzma
      libavutil      56. 14.100 / 56. 14.100
      libavcodec     58. 18.100 / 58. 18.100
      libavformat    58. 12.100 / 58. 12.100
      libavdevice    58.  3.100 / 58.  3.100
      libavfilter     7. 16.100 /  7. 16.100
      libavresample   4.  0.  0 /  4.  0.  0
      libswscale      5.  1.100 /  5.  1.100
      libswresample   3.  1.100 /  3.  1.100
      libpostproc    55.  1.100 / 55.  1.100
    [AVFoundation input device @ 0x7ffe8450f880] AVFoundation video devices:
    [AVFoundation input device @ 0x7ffe8450f880] [0] FaceTime HD Camera
    [AVFoundation input device @ 0x7ffe8450f880] [1] Capture screen 0
    [AVFoundation input device @ 0x7ffe8450f880] AVFoundation audio devices:
    [AVFoundation input device @ 0x7ffe8450f880] [0] AirBeamTV Audio
    [AVFoundation input device @ 0x7ffe8450f880] [1] Built-in Microphone
    "": Input/output error
    
We want the 'Built-in Microphone' device, the [1] before its name indicates it is audio device index 1.

The default device index for the CLI is 1, if you need to specify another use the -i option

    python -m burningaudio -t .05 -i 0
