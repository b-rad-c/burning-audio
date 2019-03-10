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
    pi@raspberrypi:~/Code/burningaudio $ python3 -m burningaudio -l
    **** List of CAPTURE Hardware Devices ****
    card 1: VF0790 [Live! Cam Chat HD VF0790], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    
The device index is the card number at the beginning of the line showing your device's name, in this case 'Live! Cam' is device index 1

The default device index for the CLI is 1, if you need to specify another use the -i option

    python -m burningaudio -i 0

### Decay

Decay is used to smooth out gaps between words and other short pauses, it can be a float or int representing the number of seconds of silence to return to a no activity state.

##### no decay
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


##### decay .5

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
    
