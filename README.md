# DIY Alexa ( if you have a broken phone or a Raspberry Pi ) 

# Motive of this Project 

There are old phones or even Raspberry Pis from other projects which are just lying around and I wanted to build something around that only. Something which has more features than any alexa on the market and something which is more customizable and privaate than a usual alexa due to you being able to tweak every little component and software (It's also more safe since all the touch buttons on the top of the enclosure are directly cuts off  power to the mic only. ) 

>If I would have to suggest honestly, just bite the bullet and use the Raspberry Pi for better features easier setup and more accessible additional features since it has GPIO pins 

The second biggest reason to consider this project, if you enjoy these kinds of projects, might also be because of how cheap it is if (you already own the Raspberry Pi or phone)

# **What Is This Project**  

DIY Alexa is a personal hardware project I built using accessible, affordable components and tried to repurpose electronics. The goal is to create a voice assistant with stereo audio output and a custom enclosure and add features that isnt available in anything on the market this project also as one of the cleanest and most minimalist designs with no flashy features like big screens just a small display used for just for displaying the time and current media output.

# **Why Am I Building It?** 

I recently got into making such projects and thought this could honestly be useful in anyone's daily life giving unused things a second life while teaching me about audio systems and operating systems( Im kinda new to this) . I also wanted to learn how a smart speaker works by building it through research and picking individual parts. 

# **Planned Features**  

1. Voice input through a microphone
2. A customizable voice-assistant software setup (Alexa and Alexa Ultimate app) 
3. Stereo audio using two full-range drivers
4. A physical volume knob 
5. A custom MDF enclosure
6. An optional display and additional features as the project develops. (if I can get funding)
7. 3 touch sensitive buttons for the following features - Mute mic, Start listening and bluetooth mode
8. By touching the top of the alexa it can automatically start playing your last played song by using the AlexaTap app
9. Lights under the enclosure to show interactive lights when the Alexa is speaking and listening ( It can also act as a lamp at night ) 

# Hardware 

the audio system uses two 3-inch, 10w, 4 ohm full range drivers and a PAM8610 stereo amplifier. I will also be looking to use a USB sound card, AUX cables,PN532 NFC/RFID Reader, TTP223 Capacitive Touch Sensor, RGB LED Strip, and reused things if possible

The Lenovo Vibe k5+ was my original brain of the project and the real motive of all the original designs. But due to the massive eMMC failures the phone reported, I have pivoted from using a phone to a Raspberry Pi 4 Model B 4gb/8gb ram version. 

# **Why I cant use a esp32 even though its the cheapest option?**

The main problem of the Esp is that it does not have enough processing power or ram to run the programmes at once the main problem is ram only since there will be the Diy Alexa Player will constantly be running and checking the website and on top of that the esp would also need tp host a website. If I even manage to run all this on a Esp then it wont have enough power to run the AVS and detech the wake word which takes alot of processing power to filter all that microphone data 

These are the main reasons to why the Esp would just not work. At the end of the day its just a micro controller and not a full computer and running so much on it just not possible since on top of all the existing aoftware I will also have to add apps like YouTube, Spotify, Google services and weather 

Nut I do plan to use esp32 to make my own smart appliances to wrok with the alexa ( This is abetter use of the Esp32 ) 

>Thanks for the suggestion to add this in the readme @a_bot 

# Current progress 

I have dismantled an old Compaq laptop to look for reusable components, recovered a PCB from some old Bluetooth headphones, researched the audio hardware, and experimented with powering the Lenovo K5+ using an alternative battery arrangement.

I also tried opeing and using TWRP, LineageOS, and working SD card-based Linux booting. These attempts have not produced a reliable working system, and the Internal eMMC failure has led me to reconsider the original approach. leading to the project pivoting from a small scale project to a project requiring custom software and much more. 

in the current phase I have designed many new features which only the raspi could have as it has GPIO pins, which opens a whole new world of sensors and features as compared to the phone

## Documentation 

>1. [Bill of Materials](https://github.com/Toastinhues/DIY-alexa/blob/main/BOM_project_3491.xlsx)
>2. [Development Timeline](docs/PROJECT_TIMELINE_NOTES.md)
>3. [Build Notes](docs/BUILD_NOTES_TEMPLATE.md)
>4. [Photos](docs/PHOTO_EVIDENCE_CHECKLIST.md)
>5. [Software For Raspberry Pi (not the app)](https://github.com/Toastinhues/DIY-alexa/tree/main/software)
>6. [Build Instuctions](https://github.com/Toastinhues/DIY-alexa/blob/main/Build_Instructions.md)

# How to build it with diagrams <

well the complete smart speaker has not been assembled because I dont have parts, so there are no verified instructions for operating a finished device. According to the design, I will connect a microphone and sound interface to Phone or Raspberry Pi, with audio output routed through a stereo amplifier to the speakers.

# How to flash the software on the Raspberry Pi in steps- 

- take the micro SD card you have At least 32gb should be okay or you can maybe do it in a 16gb card but I dont recommend it
- open the raspberry Pi website and download the image file for the specific Pi version ( PI 4 4 gb )
- follow the steps on the website and download the files on the micro sd card
- insert the ready microSD card in the Pi
- insert a temporary keyboard, mouse and dislay for the intitial setup
- download all the necessary drivers for your specific Pi 
- after that, download all the software given in the repository for both the lights and Alexa player
- after downloading the code and source files, go on the web and download any python IDE you like
- download all the requirements such as yt-dip
- Finally, run the code using the terminal and writing py main.py
- after all this you can finally test wheather your app and other features are working and dont forget to test if the mic and speakers are woring
- If you are at this point you are almost done and can continue with the other stpes in Build_instructions

[Download the Raspberry sotware from here](https://www.raspberrypi.com/software/operating-systems/)

**If you want some more instructions, go check out the Build_instructions on this repo only ;D**

[Build Instuctions](https://github.com/Toastinhues/DIY-alexa/blob/main/Build_Instructions.md)


## Photos of diagrams 

<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/57694eb8-439d-4e20-86fd-70279ef0d0a4" />
<img width="1421" height="1291" alt="image" src="https://github.com/user-attachments/assets/ef1a6f1c-4edf-43bb-9928-7723c29fbd8e" />


## Wiring Diagram 

<img width="967" height="605" alt="image" src="https://github.com/user-attachments/assets/1fcb60d6-31d3-4f90-9348-26ea3e51e2f2" />

>Wiring plan for lights; the wiring for the touch buttons is the same as arduino ones, so no need to add that

<img width="875" height="585" alt="image" src="https://github.com/user-attachments/assets/aedd2660-188f-4988-8a71-3bed50ad9fd1" />

## BOM

| No. | Component | Quantity | Price (INR) | Price (USD) | Purchase Link |
|---:|---|---:|---:|---:|---|
| 1 | Raspberry Pi 4 Model B (4GB) | 1 | ₹11,000 | $115.90 | [Robu.in](https://robu.in/product/raspberry-pi-4-model-b-with-4-gb-ram/?src=raspberrypi) |
| 2 | 3-inch Full-Range Speakers (10W, 4Ω) | 2 | ₹199 | $2.10 | [Amazon India](https://www.amazon.in/Electronic-spices-Inch-Speaker-Power/dp/B07MF1CPCJ/) |
| 3 | PAM8610 Stereo Amplifier (10W + 10W) | 1 | ₹299 | $3.15 | [ElectroPi](https://www.electropi.in/pam8610-stereo-audio-amplifier-board-with-switch-potentiometer) |
| 4 | AUX Cables | 2 | ₹200 | $2.11 | [Amazon India](https://www.amazon.in/Ambrane-Compatible-Smartphones-Headphone-Speakers/dp/B09DSYD7WS) |
| 5 | USB Sound Card | 1 | ₹130 | $1.37 | [Amazon India](https://amazon.in/Channel-External-Converter-Microphone-Earphone/dp/B0H3PX15BG) |
| 6 | Insulated Copper Wires | 2 metres | ₹60 | $0.63 | [MakerBazar](https://makerbazar.in/products/1-5mm-pvc-insulated-single-core-flexible-copper-wire-roll) |
| 7 | DC Power Adapter / Power Connection | 2 | ₹900 | $9.48 | [Flipkart](https://www.flipkart.com/v-antiques-12v-5a-dc-power-adapter-supply-smps-pc-lcd-monitor-tv-led-strip-cctv-12-w-adapter/p/itm83ea5251e8b66) |
| 8 | Microphone | 1 | ₹150 | $1.58 | [Amazon India](https://www.amazon.in/CERLINK-Microphone-Compatible-Smartphones-Interviews/dp/B0H5CQ6QJ7/) |
| 9 | LM2596 Buck Converter | 2 | ₹80 | $0.84 | [Quartz Components](https://quartzcomponents.com/products/lm2596-buck-converter-power-supply-module) |
| 10 | Raspberry Pi Heatsink with Fan | 1 | ₹800 | $8.43 | [Robocraze](https://robocraze.com/products/raspberry-pi-metal-aluminum-case-with-double-fans-for-raspberry-pi-4b-gold) |
| 11 | Raspberry Pi-Compatible Display | 1 | ₹900 | $9.48 | [Robocraze](https://robocraze.com/products/3-5in-lcd-display-for-raspberry-pi) |
| 12 | MDF Wood Panels (3mm, 10-inch) | 6 | ₹160 | $1.69 | [Amazon India](https://www.amazon.in/AUREWOOD-Boards-Surface-Painting-Mandala/dp/B0GYFD97LY/) |
| 13 | MicroSD Card (32GB) | 1 | ₹699 | $7.37 | [Amazon India](https://amazon.in/BRYT-Memory-Camera-Smartphone-Tablets/dp/B0D1QSH8FW) |
| 14 | RGB LED Strip | 10 cm | ₹300 | $3.16 | [Amazon India](https://www.amazon.in/XERGY-Flexible-Changing-Controller-Multicolour/dp/B079KF3J6D) |
| 15 | PN532 NFC/RFID Reader | 1 | ₹300 | $3.16 | [Quartz Components](https://quartzcomponents.com/products/pn532-rfid-reader-nfc-read-write-module) |
| 16 | TTP223 Capacitive Touch Sensor Modules | 4 | ₹115 | $1.21 | [Robocraze](https://robocraze.com/products/ttp223-touch-switch-module) |
| 17 | USB Type-C to HDMI Adapter | 1 | ₹400 | $4.21 | [Amazon India](https://www.amazon.in/India-Adapter-Ethernet-Compatible-Raspberry/dp/B08PW6W54V) |
| | **Grand Total (as listed)** | | **₹16,482** | **$173.67** | |

[BOM_project_3491.xlsx](https://github.com/user-attachments/files/33730753/BOM_project_3491.xlsx)

[BOM_project_3491.csv](https://github.com/user-attachments/files/33760308/BOM_project_3491.csv)

## Website and app for NFC features to work 

[Website and App code ](https://github.com/Toastinhues/diy-alexa-website)
