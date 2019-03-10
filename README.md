# Burning Audio
#### A utility to detect when there is activity from an audio input.

The purpose of this project is to control art installations when someone is talking on a microphone, I'll be using it in a burning man project; hence the name.

### Requirements
python3, ffmpeg, microphone

This has only been tested on a raspberry pi but will probably work on other linux distros with arecord

references

    https://ffmpeg.org/ffmpeg-devices.html#alsa
    https://trac.ffmpeg.org/wiki/Capture/ALSA
    
### Installation
    
    sudo apt-get install ffmpeg
    sudo pip install git+https://bitbucket.org:B_rad_C/burning-audio.git
    

### CLI Usage
(useful for testing)

    python -m burningaudio
    
    not talking
    not talking
    not talking
    talking
    talking
    talking
    not talking
    talking
    talking
    not talking
    not talking
    not talking
    not talking
    talking
    talking
    
This is an infinite loop, use control+c to exit.
    
### API usage
See inline documentation for explanation of arguments.
    
    for sample in burningaudio.detect_activity():
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
    python -m burningaudio -l
    
    null
        Discard all samples (playback) or generate zero samples (capture)
    default:CARD=VF0790
        Live! Cam Chat HD VF0790, USB Audio
        Default Audio Device
    sysdefault:CARD=VF0790
        Live! Cam Chat HD VF0790, USB Audio
        Default Audio Device
    front:CARD=VF0790,DEV=0
        Live! Cam Chat HD VF0790, USB Audio
        Front speakers
        
    ...
    
    dsnoop:CARD=VF0790,DEV=0
        Live! Cam Chat HD VF0790, USB Audio
        Direct sample snooping device
    hw:CARD=VF0790,DEV=0
        Live! Cam Chat HD VF0790, USB Audio
        Direct hardware device without any conversions
    plughw:CARD=VF0790,DEV=0
        Live! Cam Chat HD VF0790, USB Audio
        Hardware device with all software conversions
    
In this example the name of our device is:

    hw:CARD=VF0790,DEV=0
    
### Specify device
Using the default device input is fine for testing but for real world use it is recommended to specify the device name to ensure repeatability, as the default device may change unpredictably.
    
    for sample in burningaudio.detect_activity('hw:CARD=VF0790,DEV=0'):
        pass
use --input (-i) on the command line

    python -m burningaudio -i hw:CARD=VF0790,DEV=0

### Decay

Decay is used to smooth out gaps between words and other short pauses, it can be a float or int representing the number of seconds of silence to return to a no activity state.

    python -m burningaudio --decay 0
    not talking
    not talking
    talking
    talking
    not talking
    not talking
    talking
    talking
    not talking
    not talking
    talking
    talking
    talking
    talking

    python -m burningaudio --decay .5
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    not talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    talking
    
