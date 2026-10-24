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

1.Measure the speakers and electronic components.

2.Plan the enclosure layout, leaving room for the Raspberry Pi, amplifier, wiring, and ventilation.

3.Cut and assemble the MDF panels.

4.Make openings for both speakers, buttons, power input, and any required ports.

5.Check that all components fit before permanently mounting them.

**Try to keep the wiring a bit accessible since there are many things which could need testing**

## Step 3: Install the Speakers

- Position the two speaker drivers in the enclosure.
- After positioning, cut all the appropriate holes in the wood.
- Secure them using appropriate screws and mounting points.
- Connect the left speaker to the amplifier's left-channel output.
- Connect the right speaker to the amplifier's right-channel output.
- Verify polarity and ensure that no bare wires can touch each other.

>TBH, you might need to verify and test everything yourself since I dont currently have the parts right now

## Step 4: Set Up the Power Supply

- Connect the 9V DC adapter to a suitable power-distribution arrangement.
- Supply the PAM8610 amplifier using a voltage within its specified operating range.
- Feed the Raspberry Pi through a correctly rated buck converter set to the Pi's required input voltage.
- Verify output voltage and polarity using a multimeter before connecting the Pi.
- Secure all power connections and insulate exposed conductors.

**Do not connect 9V directly to the Raspberry Pi's 5V input. Confirm that the adapter, converter, and wiring can safely supply the required current**

## Step 5: Connect the Audio Hardware

- Connect the USB sound card to a Raspberry Pi USB port.
- Connect the microphone to the appropriate input on the sound card.
- Connect the sound card's audio output to the amplifier's AUX input using a 3.5mm AUX cable.
- Keep audio wiring away from power wiring where practical.
- Check that the amplifier input and sound card output are compatible.

>If you're at this point, it's high time to check for the ground loop issue

## Step 6: Connect the Three-Button Controls

- Mount the three buttons on the enclosure.
- Connect each button to its designated Raspberry Pi GPIO input according to the project's wiring diagram.
- Ensure that the GPIO pins are configured correctly in software.
- Configure the buttons for their intended functions: mute, listening control, and Bluetooth mode.
- Test each button individually before cloing the enclosure.
- Also put the given python files on the Raspberry Pi
  
## Step 7: Install the Raspberry Pi Operating System

- Install Raspberry Pi Imager on a computer.
- Prepare a compatible microSD card with a supported Raspberry Pi OS version.
- Configure the required network settings and user account.
- Insert the card into the Raspberry Pi and boot i.
- Connect the Pi to the internet and install available updates.
- Confirm that the USB sound card and microphone are detected.

[Download Raspberry Pi OS](https://www.raspberrypi.com/software/)

## Step 8: Set Up the Alexa Software

- Configure the microphone and audio output devices.
- Follow the official Amazon Alexa Voice Service (AVS) setup requirements if AVS is being used.
- Complete any required Amazon developer registration, authentication, and device configuration.
- Configure the project's startup and control software.

>Test microphone input, audio playback, and listening controls.
_While rereading this entire I realised I used configure a bit too much sorry about that :D_

## Step 9: Test the Complete System

- Before closing the enclosure, verify the following:
- Raspberry Pi boots successfully.
- Microphone input is detected.
- Alexa software starts and responds when configured.
- Both speakers produce sound.
- Left and right audio channels work correctly.
- Mute and listening controls behave as intended.
- Bluetooth pairing and audio playback work.
- Underglow LEDs operate correctly, if installed.

>No loose connections, excessive heating, or persistent electrical hum are present.

**thansk for reading hope you have fun building if you are ready to take the challenge ;D**

# Happy Building 

