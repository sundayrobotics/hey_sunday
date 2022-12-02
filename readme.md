# mandatory pre-installation ad pisetup

- retrieve card and device number for the microphone
    - arecord -l
        - Raspi's 3.5 mm jack -> labeled as either Analog, Headphones or ALSA

    # modifying ALSA Config file.
    - These lines are what will set up our audio driver and help 
        it know what devices it should be interacting with.

    In the Terminal:
    - cd
    - nano .asoundrc
    ----------------------------------------
    pcm.!default {
        type asym
        capture.pcm "mic"
    }

    pcm.mic {
        type plug
        slave {
            pcm "hw:2,0"
        }
    }
    ----------------------------------------
    - Ctrl+X then Y then Enter

# before running docker container on the raspberry pi terminal do:
- sudo apt install python3-all-dev 
- sudo pip3 install pvporcupine (requirement for firs time development)
- Test Porcupine Wakeword Engine: (run in terminal $ )
    - pvporcupine_mic --keyword computer
    # say computer to the mic 
    - if successful: detected keyword will be displayed on the $
