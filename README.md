# Burning Audio
#### A utility to detect when there is activity from an audio input.

The purpose of this project is to control art installations when someone is talking on a microphone, I'll be using it in a burning man project; hence the name.

Currently this is just a proof of concept, the plan is to eventually use this on a razz pi but I don't have a mic to plug into my raspberry right now so it is only compatible with the built in microphone on an osx laptop.


### Requirements
python 3.6+ (i use f-strings and you should too)

ffmpeg

osx w/ built in microphone

### CLI Usage
(useful for testing)

    python -m burningaudio -t .05
    
    talking: 9071651
    talking: 8533222
    talking: 9080982
    talking: 8510622
    no talking
    no talking
    no talking
    talking: 7357233
    talking: 7458738
    talking: 8606625
    no talking
    no talking
    no talking
    
This is an infinite loop, use control+c to exit.
    
### API usage

    for sample in burningaudio.detect_activity(.05, 1, .5):
        if sample is None:
            # no activity
            pass

        else:
            # we have activity (or have not decayed since last activity)
            # sample is a non negative int representing the decoded audio sample,
            # see in-line doc string for more details
            do_something(sample)
            
This is an infinite loop, kill process or use control+c to exit.
    
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

### Decay

Decay is used to smooth out gaps between words and other short pauses, it can be a float or int representing the number of seconds of silence to return to a no activity state.

##### no decay
    no talking
    talking: 6587313
    talking: 8184261
    talking: 9345084
    talking: 8674720
    talking: 9518083
    talking: 8586311
    talking: 9114550
    talking: 8034957
    no talking
    talking: 6504780
    talking: 8255085
    talking: 9071651
    talking: 8533222
    talking: 9080982
    talking: 8510622
    no talking
    no talking
    no talking
    talking: 7357233
    talking: 7458738
    talking: 8606625
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    talking: 7663601
    talking: 8537540


##### decay .5

    talking: 8413999
    talking: 8412464
    talking: 8400578
    talking: 8405452
    talking: 8369224
    talking: 8364918
    talking: 8402994
    talking: 8380329
    talking: 8381758
    talking: 8389155
    talking: 8350598
    talking: 8355324
    talking: 8393194
    talking: 8401350
    talking: 8357656
    talking: 8406096
    talking: 8435959
    talking: 8453743
    talking: 8424528
    talking: 8377140
    talking: 8398663
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    no talking
    
