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
    
