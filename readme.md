# mandatory pre-installation ad pisetup

- retrieve card and device number for the microphone
    - arecord -l
        - Raspi's 3.5 mm jack -> labeled as either Analog, Headphones or ALSA

    # modifying ALSA Config file.
    In the Terminal:
    - cd
    - nano /home/pi/.asoundrc
    ----------------------------------------
    pcm.!default {
        type asym
        capture.pcm "mic"
    }

    pcm.mic {
        type plug
        slave {
            pcm "hw:{card_number},{device_number}"
        }
    }
    ----------------------------------------
    - Ctrl+X then Ctrl+Y then Enter

# before running docker container on the raspberry pi terminal do:
- sudo apt install python3-all-dev 
- sudo pip3 install pvporcupine (requirement for firs time development)
- Test Porcupine Wakeword Engine: (run in terminal $ )
    - pvporcupine_mic --keyword porcupine 
    - if successful: detected keyword will be displayed on the $
