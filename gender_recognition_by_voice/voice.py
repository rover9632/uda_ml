#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:53:26 2018

@author: wave
"""

def record_voice():
    """Record a 10 seconds of audio and save to a WAVE file."""

    import pyaudio
    import wave
        
    FORMAT = pyaudio.paInt16
    CHANNELS = 5
    RATE = 44100
    RECORD_SECONDS = 10
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
    
    print("* recording")
    
    data = stream.read(RATE*RECORD_SECONDS)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open("./test/voice.wav", 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
    
    
def trans_voice():
    """extract features from wav files to a csv file."""
    
    from rpy2.robjects.packages import importr
    
    base = importr('base')
    base.source('./feature.R')
    
    
if __name__ == '__main__':
    #record_voice()
    trans_voice()
