# DIY Alexa ( if you have a spare broken phone or a Raspberry Pi ) <h1>

# **Motive of this Project** <h3> 

_There are a lot of broken phones or tech which are just not being used at all, so I decided to make something to help the cause by designing a simple yet clever Alexa-based device, taking advantage of all the resources of the phone or Raspberry Pi if you want a more custom and private Alexa._
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

# _Hardware_ <h4> 

_the proposed audio system uses two 3-inch, 10w, 4ohm full range drivers and a PAM8610 stereo amplifier. I will also be looking to use a USB sound card, AUX cables, and reusedthings_

The Lenovo Vibe k5+ was my original computing platform. But due to the massive eMMC failures the phone reported, I have pivoted from using a phone to a Raspberry Pi 4 Model B 4gb/8gb ram version. **The final BOM of your build may change depending on what you choose, and the  same goes for the cost**

# Current progress <h2>

I have dismantled an old Compaq laptop to look for reusable components, recovered a PCB from some old Bluetooth headphones, researched the audio hardware, and experimented with powering the Lenovo K5+ using an alternative battery arrangement.

I also tried opening and using TWRP, LineageOS, and working SD card-based Linux booting. These attempts have not produced a reliable working system, and the Internal eMMC failure has led me to reconsider the original approach.

## Documentation <h2>

>1. [Bill of Materials](BOM%20DIY%20alexa.xlsx)
>2. [Development Timeline](docs/PROJECT_TIMELINE_NOTES.md)
>3. [Build Notes](docs/BUILD_NOTES_TEMPLATE.md)
>4. [Photos](docs/PHOTO_EVIDENCE_CHECKLIST.md)


# How to build it with diagrams <h2> 

_The complete smart speaker has not been assembled due to a lack of parts, so there are no verified instructions for operating a finished device. The intended design will connect a microphone and sound interface to the computing platform, with audio output routed through a stereo amplifier to the speakers._

## Photos of diagrams <h2>

<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/57694eb8-439d-4e20-86fd-70279ef0d0a4" />
<img width="1421" height="1291" alt="image" src="https://github.com/user-attachments/assets/ef1a6f1c-4edf-43bb-9928-7723c29fbd8e" />


## Wiring Diagram (I'm sorry this was made in Paint)

<img width="1536" height="1024" alt="DIY Voice Assistant Wiring Plan" src="https://github.com/user-attachments/assets/2342e556-1e04-4168-8b7b-69334174feab" />

## BOM

[BOM_project_3491.xlsx](https://github.com/user-attachments/files/33730753/BOM_project_3491.xlsx)
