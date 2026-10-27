## Build Instructions for building the DIY Alexa ( Raspberry Pi )  <h1>

This guide explains how to assemble and set up the DIY Alexa speaker. Follow the steps in order, checking each connection before powering on the device.

## Step 1: Gather the Components

>Prepare the following components:

- Raspberry Pi 4 4/8gb	
- Speakers 10w 4Ω 3in	
- PAM8610 10w + 10w 	
- AUX cables	
- Soundcard	
- Wires	
- DC jack (power supply)	
- Microphone	
- LM2596		
- Heatsink with fan (for PI)		
- Display (Pi-compatible)		
- MDF wood 3mm, 10 in		
- Micro SD card 32 GB		
- LED strip RGB		
- PN532 NFC RFID		
- TTP223		
- Type D USB to HDMI	

**This has been copied from BOM of the project refer to the README for the BOM**

## Step 2: Prepare the Speaker Enclosure

Before even building anything, firstly size all the things we need to mount inside the enclosure before bulding( trust me its easier this way ).Make sure there is plenty of head room or well space in general for future upgrades and cooling fans and ventilation. After the planning is done cut and assemble the enclosre accordingly please use acrylic glue only use screw for parts not for sealing the encloure. and be sure not to seal the box permanently or else it will become really challenging for you to troubleshoot the alexa.

**Try to keep the wiring a bit accessible since there are many things which could need testing**

## Step 3: Install the Speakers

after making the mounting holes for the speaker fit the speakers into its respecive hole and screw it down tightly to avoid those nasty vibrations. wrie the speakers to the amplifier ( Please check the polarity or both your speakers WILL fry ). Insulate all the loose wiring. 
>TBH, you might need to verify and test everything yourself since I dont currently have the parts right now

## Step 4: Set Up the Power Supply

Insert the 9V DC wall wort into your main power line. Provide the amp with proper voltage (PAM8610 prefers 7-15V). With a buck converter, reduce power to whatever the Pi demands (mostly 5V). Before you connect the Pi, find a multimeter and verify output voltage and polarity. Insulate everything-exposed wiring is a no-go. Forbid 9V directly on 5V line powering the Pi. Use a power supply, converter, and cables able to supply whatever current your amp consumes.

**Do not connect 9V directly to the Raspberry Pi's 5V input. Confirm that the adapter, converter, and wiring can safely supply the required current. trust me I did this in an Arduino Uno and its not good**

## Step 5: Connect the Audio Hardware

Connect the aux cable to the sound card to the Pi, and connect the Mic to the sound card. Connect the audio output of the sound card to the input of the amp using 3.5mm to 3.5mm aux cable. Please be sure to keep power and audio wires apart. amp input should be the same as the sound card output.

>If you're at this point, it's high time to check for the ground loop issue

## Step 6: Connect the Three-Button Controls

Mount the 3 buttons on the enclosure. Attach them to the right GPIO pin from your Pi. Setup your code and GPIOs. Map your buttons: mute, listen, Bluetooth. Test all the buttons before you close the enclosure. Do not forget to copy the 3 Python files to your Pi (to run the code).Or else it's not gonna work.

## Step 7: Install the Raspberry Pi Operating System

Get the Raspberry Pi Imager for your PC. Write the Raspberry Pi OS onto the microSD card using the right version. Set up your network and user. Put the microSD in the Pi and turn it on. Connect to the internet and update everything. Check both the sound card and mic are being detected by the Raspberry Pi.

[Download Raspberry Pi OS](https://www.raspberrypi.com/software/)

## Step 8: Set Up the Alexa Software

Set your default microphone and speaker out. Set your Amazon Alexa Voice Service (AVS) if enabled. Register a developer account with Amazon and complete the registration and provisioning steps for your device. Load the startup and controls software for your project. Test the microphone, speaker and all controls.

>Test microphone input, audio playback, and listening controls.

## Step 9: Test the Complete System

**Before closing the enclosure, verify the following:**

- Raspberry Pi boots successfully.
- Microphone input is detected.
- Alexa software starts and responds when configured.
- Both speakers produce sound.
- Left and right audio channels work correctly.
- Mute and listening controls behave as intended.
- Bluetooth pairing and audio playback work.
- Underglow LEDs operate correctly, if installed.

>well if you did everything correctly there should be no problems

**thansk for reading hope you have fun building if you are ready to take the challenge ;D**

**Happy Building**

