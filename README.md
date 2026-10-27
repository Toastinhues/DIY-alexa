# DIY Alexa ( if you have a broken phone or a Raspberry Pi ) <h1>

# Motive of this Project <h3> 

There are a lot of broken phones or tech which are just not being used at all, so I decided to make something to help the cause by designing a simple yet clever Alexa-based device, taking advantage of all the resources of the phone or Raspberry Pi if you want a more custom and private Alexa.
> To Be Honest, I would seriously suggest using a Raspberry Pi only, as it's more beginner-friendly and, on top of that, if the phone has problems flashing the OS or eMMC failures (**as in my case**), the project will have to pivot away from a phone, or it will take a lot more time.

The second biggest reason to consider this project, if you enjoy these kinds of projects, might also be because of how cheap it is if (you already own the Raspberry Pi or phone)

# **What Is This Project** <h3> 

_DIY Alexa is a personal hardware project I built using accessible, affordable components and tried to repurpose electronics. The goal is to create a voice assistant with stereo audio output and a custom enclosure._

# **Why Am I Building It?** <h3>

_I recently got into engineering projects and thought this could be useful in anyone's daily life, giving unused things a second life while teaching about audio systems and operating systems. I also wanted to learn how a smart speaker works by building it through research and picking individual parts._

# **Planned Features** <h4> 

1. Voice input through a microphone
2. A customizable voice-assistant software setup (Alexa and Alexa Ultimate app) 
3. Stereo audio using two full-range drivers
4. A physical volume knob 
5. A custom MDF enclosure
6. An optional display and additional features as the project develops. (if I can get funding)

# Hardware <h4> 

the audio system uses two 3-inch, 10w, 4 ohm full range drivers and a PAM8610 stereo amplifier. I will also be looking to use a USB sound card, AUX cables, and reused things if possible

The Lenovo Vibe k5+ was my original computing platform. But due to the massive eMMC failures the phone reported, I have pivoted from using a phone to a Raspberry Pi 4 Model B 4gb/8gb ram version. 

# Current progress <h2>

I have dismantled an old Compaq laptop to look for reusable components, recovered a PCB from some old Bluetooth headphones, researched the audio hardware, and experimented with powering the Lenovo K5+ using an alternative battery arrangement.

I also tried opeing and using TWRP, LineageOS, and working SD card-based Linux booting. These attempts have not produced a reliable working system, and the Internal eMMC failure has led me to reconsider the original approach.

## Documentation <h2>

>1. [Bill of Materials](BOM%20DIY%20alexa.xlsx)
>2. [Development Timeline](docs/PROJECT_TIMELINE_NOTES.md)
>3. [Build Notes](docs/BUILD_NOTES_TEMPLATE.md)
>4. [Photos](docs/PHOTO_EVIDENCE_CHECKLIST.md)
>5. [Software For Raspberry Pi (not the app)](https://github.com/Toastinhues/DIY-alexa/tree/main/software)

# How to build it with diagrams <h2> 

well the complete smart speaker has not been assembled because I dont have parts, so there are no verified instructions for operating a finished device. According to the design, I will connect a microphone and sound interface to Phone or Raspberry Pi, with audio output routed through a stereo amplifier to the speakers.

## Photos of diagrams <h2>

<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/57694eb8-439d-4e20-86fd-70279ef0d0a4" />
<img width="1421" height="1291" alt="image" src="https://github.com/user-attachments/assets/ef1a6f1c-4edf-43bb-9928-7723c29fbd8e" />


## Wiring Diagram (I'm sorry this was made in Paint)

<img width="1536" height="1024" alt="DIY Voice Assistant Wiring diagram" src="https://github.com/user-attachments/assets/ee1ce14d-a9fd-4c8b-a0d8-1cbb5d2c9897" />

>Wiring plan for lights; the wiring for the touch buttons is the same as arduino ones, so no need to add that

<img width="672" height="280" alt="image" src="https://github.com/user-attachments/assets/e38e5316-e345-414e-bcab-491ac0dc0882" />

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
