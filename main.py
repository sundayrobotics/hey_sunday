#!/usr/bin/env python3

# import the neccesary packages
import struct #unpacks audio input
import pyaudio #create an audio stream from mic connected to raspberrypi
import pvporcupine # Engine allows us to listen to hotwords

#create vars to store handles for porcupine
porcupine = None
pa = None
audio_stream = None

access_key="LJAhNEy++D83aj0clU0fN67MJnAnyWhEKW+dC4efSBaHD5VkaZKKXA=="

try:
    porcupine = pvporcupine.create(
        access_key=access_key,
        keywords=["computer","porcupine"]    
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    while True:
        pcm=audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("active...")

finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.delete()

    if pa is not None:
        pa.terminate()