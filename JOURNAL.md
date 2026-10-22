---
title: "DIY Alexa"
author: "-Toast-"
description: "DIY Alexa using recycled parts custom software, ROM's and broken phones!!!"
created_at: "2026-10-09"
---

# 2026-10-22: Making code (in python because its easier for the all new features to work)  

**Total time spent: 1.5 hours**

I made ( with some help from AI just for debugging because it wasn't working. But I got a simulation to work, and everything else, such as the wiring diagram( Made in Paint :D ) and all the software like the app and everything has now been done so the 3 features should now work when I start builing it 

I also finally updated my GitHub repo, and everything should now be upto date 
![image.png](https://cdn.hackclub.com/01a16454-d242-76f2-bf7c-05b34f890efb/image.png)
![image.png](https://cdn.hackclub.com/01a16455-15ff-70e6-b90f-d3a75a0ec93a/image.png)

# 2026-10-22: Making the first new feature of the DIY Alexa

**Total time spent: 4 hours**

Since this was one of the hardest features of the 3 I decided to make this first only and I will be making new Devlogs and more items to add in the github repo as I move on 

Parts needed -

1. PN532 NFC reader 
2. Passive NFC tag

My first plan and idea was that when I tap my phone on the enclosure it will start playing the last song you played but it was easier said then done. I first wanted to try and use the spotify developer apps and make a new app and connect it to a simple deployed link which could fetch the url and track when tapped ( It requires your approval only on the first tap ) but I quickly realised after making and testing that Every one tapping would need spotify premium for this feature to work. So I decided t code ( I took some help from AI (this was stated in the AI usage declaration) )and made a app *CALLED ALEXA TAP* and It works in almost the same way. On the first tap there is a link telling you to download the alexa tap app and after the dwonload just allow it to access notification 

MAIN WORKING OF THE APP-  

It detects the currect track by the phones media output (when tapped )on almost any app and tracks 3 things  1. the artist 2. song name 3. track the song is from

after this it sends the data over to the raspberry pi which searches the web and plays the song making a almost seemless experience ( after the first time )

Problems needed to fix - 

-the app does not run in the backround when tapped 

-I still need to figure out a way to differenciate between devices with alexa tap or not because it will always to download the app ( i need it to differenciate when to collect data and when to tell you to download the app ) 

![D9B7F669-6A8F-4745-941B-4B07FDBD7CF8_.png](https://cdn.hackclub.com/01a161cf-afdf-76ca-aa1a-bbbde8e05468/D9B7F669-6A8F-4745-941B-4B07FDBD7CF8_.png)

Please be Patient I will add more images later ( NOTE for reviewer )

# 2026-10-20: Making the 3D model  

**Total time spent: 2 hours**

Even though this model was made 3 days ago, I somehow forgot to make a journal about it. I first found that when submitting a project for review, you should always add a 3D model so I decided to make a 3D model in Tinkercad and make it a STEP file in FreeCAD . Even though it takes like half an hour to make these simple models it took me 2 hours since this is my first ever big project 

![image.png](https://cdn.hackclub.com/01a15a58-09ed-77c7-b2cd-6879a48157c3/image.png)
![image.png](https://cdn.hackclub.com/01a15a58-2845-7f56-bc31-ad2525f493f6/image.png)
![image.png](https://cdn.hackclub.com/01a15a58-64d7-719f-ae3c-a4ab48dba3e7/image.png)
![image.png](https://cdn.hackclub.com/01a15a58-7b5c-7e52-bc39-058380748cde/image.png)
![image.png](https://cdn.hackclub.com/01a15a58-b20b-791a-8baf-97d940b5a0a1/image.png)
![image.png](https://cdn.hackclub.com/01a15a58-cf01-7f58-8444-286c05399b5a/image.png)

# 2026-10-20: New features I will add and new parts added to BOM

**Total time spent: 1 hour**

I have been waiting for a week and got a good idea to add to the custom alexa. So I started researching on what parts should be used to make my idea real and got to work.

All the new parts added to the BOM - 
- USB Type-D to HDMI ( needed for the initial setup )
- LED strip ( please only use thw WS2812B ) ( It has the indivisual lighting control we need for the gradients and interactive lights ) 
- 3 touch-sensitive buttons 
- NFC reader (PN532); this specific one has been used for more advanced features

These parts have been selected since I want to create some features that Alexa doesn't have - 

1. Tapping your phone on top plays the last song you were listening to
2. lights under the enclosure so that when the Alexa is listening or talking it glows just like a real Alexa, but instead of it being on top, it will be invisible. Since the lights will turn on under the body and be diffused from the desk 
3. No physical buttons, only invisible touch buttons under the enclosure for a seamless look

After getting approved and buying the parts, I hope to build it. Though I will create the custom firmware for the buttons and NFC sensor later on snd upload it to my git hub repo

![image.png](https://cdn.hackclub.com/01a15901-62e3-7f95-842b-a80bee7f95f4/image.png)
![image.png](https://cdn.hackclub.com/01a15902-0a8e-713b-b15d-8500101e039c/image.png)
![image.png](https://cdn.hackclub.com/01a15903-1918-78a5-bafa-77977eb7190c/image.png)
![image.png](https://cdn.hackclub.com/01a15903-e0cd-7e9c-b02f-a0cceb41bbe9/image.png)

# 2026-10-13: Takiing Out BMS from Lenovo Battery

**Total time spent: 1 hour**

Since I am not quite sure what to do now, when I checked the ADB device,s the phone repeatedly said that the internal eMMC is not responding, even though it is readable and visible by the device; that's why it's stuck in a constant state of read-only mode, where, as soon as I try to write anything, it fails 

This was a really sad discovery, but I still wasted 1 hour painfully taking out the BMS from the original battery and succeeded in doing so.

![image.png](https://cdn.hackclub.com/01a13684-1889-7c02-9a25-d0d6a161b5db/image.png)

# 2026-10-13: Turning on the phone ( Day 5 ) + very little research about the phone

**Total time spent: 2.5 hours**

Well, for starters, I have no clue about why this keeps happening,g but the TWRP is very unstable and opens only sometimes and on top of that, there is one more issue I found which may be causing such problems. The DTBs I extracted from stockboot.img identify as MSM8939 variants, while Fastboot reports MSM8916. The Linux kernel's Qualcomm device-tree bindings treat these as distinct platform identifiers. That raises a possible boot-image or DTB compatibility mismatch that we need to resolve before modifying anything else. It isn't proof of a mismatch by itself, because the QCDT section contains multiple variants, but this may still be an issue of future concern. I also found that some versions of this Lenovo phone report the wrong variant, even though my specific variant is the Lenovo K5+ MSM8939V3 (Snapdragon 616).

Also started having USB failure issues as of today only, but that happens only sometimes. I also noted that the phone's bootloader refuses to provide certain variables for unknown reasons

![image.png](https://cdn.hackclub.com/01a13679-f09b-742e-8d09-2525c9b9316c/image.png)
![image.png](https://cdn.hackclub.com/01a1367a-127b-7ff3-9bfa-6818a00967da/image.png)
![image.png](https://cdn.hackclub.com/01a1367a-3869-75df-98eb-c9c6ebe78ffc/image.png)

# 2026-10-13: Research + trying to fix the TWRP issue

**Total time spent: 2.5 hours**

I worked on that godforsaken phone again today for only about 2 hours and did some research for only half an hour. I got the TWRP running again and found that if I run LS2ND 23.1 and put the SD card in the phone so that it can boot using the SD card only, and once it restarts immediately, run fastboot boot twrp331.img, which sometimes works and sometimes fails; it really depends on my luck.

As for the research part, I still haven't truly found a solution for the ground loop problem, so I can't get the Hack Club auth team to help. I will have to buy parts myself, and I don't have a soldering iron, so it's going to be hella difficult for me. I also accessed ADB devices commands and made it so that the phone does not refer to the failed eMMC and boots using the SD card only

![image.png](https://cdn.hackclub.com/01a13674-108e-771c-8964-b7b9f28965eb/image.png)

# 2026-10-13: Trying to boot The phone ( day 4)

**Total time spent: 2 hours**

So today, I wasted another 2 hours just trying to get that phone to turn on, and this timeI didn'tt even make any progress. On top of that, TWRP stopped working,g which caused some problems, ms as ADB was not available. I tried making a custom img to boot using fastboot, but that also failed, so I'm getting really desperate about what I should do I am not really sure .


![image.png](https://cdn.hackclub.com/01a13672-8e98-7969-843a-ed9517138061/image.png)

# 2026-10-13: Basic Research work on how to use the Raspberr pi + trying to boot the Phone 

**Total time spent: 2.5 hours**

Today I really was confused since, well,l the main brain of the project and the motivation to recycle something destroyed into something useful is slowly crumbling apart. I already knew that ls2nd supports the Lenovo K5k5 family to be able to boot from an SD card,d but for some unknown reason the phone refuses to go past the boot screen,n even though the day before yesterday I was able to get TWRP running on the phone,ne which gave me way too much false hope, op e but now the project might need to pivot away from it. So I got on the internet and started doing my thing and started searching Google using other people's work as reference and trying to make my own method. Methods, I got to the point yesterday in my research and designing that I completely replaced the phone with the Raspberry Pi 3 or above. Even though it was far simpler than before, I still have the ground loop issue to fix, but I'm decidingI'lll do that tomorrow and focus on trying to fix the Lenovo itself, as I'm determined to fix it.

![image.png](https://cdn.hackclub.com/01a1366f-67af-7556-b921-9104bcad2a28/image.png)


# 2026-10-13: Raspberry Pi Research & Redesigning the Smart Speaker Blueprint

**Total time spent: 2 hours**

Today, I spent around 2 hours researching on how to rebuild my DIY Alexa project around a raspberry pi 4 B as well after  realising yesterday that getting the lenovo running reliable is EXTREMELY difficult and is not that worth it as the phone doesnt have enough ram to effectively run sll rogrammes. So, I began developing new blueprints based on the Raspberry Pi as the main brain, which could allow me to add a better display, more features, a nd, most importantly,y it would be faster than an ESP32-based Alexa, but it takes around 15- 20 seconds to respond, which is far too much for a conventionalAlexaa. Hence, the pivot from the phone to the Raspberry Pi was necessary.

![image.png](https://cdn.hackclub.com/01a13668-8e93-742d-9118-564cfbd0f395/image.png)

# 2026-10-13: Ubuntu-Based Recovery, eMMC Failure Investigation & TWRP Access

**Total time spent: 5.5 hours**

Today, I was motivated to get the Lenovo K5+ running, so I continued troubleshooting using Ubuntu, which I had set up for app development. Instead of purchasing DiskGenius, I decided to use the Ubuntu disk management tools and,d with assistance,ce reformatted the drive and prepared the SD card for anoth2nd2nd boot attempt. The phone appeared to read the SD card but became stuck on the splash screen. After further investigation, I have concluded the phone's internal eMMC might have completely failed, meaning I would need to boot the system entirely from an SD card, which is considerably more complicated. I modified the relevant files and transferred them to the card, and tried booting, but that also failed. Unexpectedly, when I tried booting TWRP, it finally worked, giving me access to ADB commands for troubleshooting. So I took full advantage of this situation to test the device and look for possible solutions, but I don't think that the phone can actually run the software due to hardware constraints. I mean, the phone is almost 10 years old. 
Because of these reasons, I began considering using a raspberry pi 4 B 4gb/8gb ra,m as this could become a more reliable base for Alexa and for future upgrades (IT will save me a ton of time from fighting with the boot partitions) 

![image.png](https://cdn.hackclub.com/01a1365c-2db0-7769-b9fa-4a42bd1fa397/image.png)
![image.png](https://cdn.hackclub.com/01a1365c-4d8b-7f8e-b918-9a3b767408c4/image.png)
![image.png](https://cdn.hackclub.com/01a1365c-6421-75c0-a9b0-ecc305b15e4b/image.png)
![image.png](https://cdn.hackclub.com/01a1365c-78bc-7b7a-abe9-e1060035952b/image.png)

https://lapse.hackclub.com/timelapse/UAdOdxDdPDhr

# 2026-10-13: Component Harvesting, Audio Noise Research, and Linux Troubleshooting

**Total time spent: 6.5 hours**

Today, I started working at around 4 pmm to salvage useful components from old electronics around the house to reduce the overall cost of my DIY Alexa build. I successfully dismantled an old computer power supply. And with the help of online resources, I explored any other possible reusable components. However, my attempt to take a part from an old charger for some diodes failed really miserably, a nd I didn't even make a dent in it. By around 7 pm, I moved on to researching the electrical side of the project and discovered that,while sharing a common power line can cause ground loop noise, causing an annoying buzzing and humming noise from the speakers or microphone. Since my budget is limited, I began looking for other cheaper solutions without adding expensive isolation hardware that might interfere with the microphone 

I also continued trying to boot the phone using the previously prepared SD card, but the attempt failed. Although I did not resolve the issues entirely, I still made progress and prevented an issue from happening. These tasks did take me a lot of time to complete, so I really didn't have time to plan for tomorrow in detail.

![image.png](https://cdn.hackclub.com/01a13641-063c-724a-996b-bdea6f4ce5fd/image.png)![image.png](https://cdn.hackclub.com/01a13641-159f-7d32-8c97-57f645076de6/image.png)![image.png](https://cdn.hackclub.com/01a13641-2de0-7ab8-97c2-c0a90fbe05be/image.png)![image.png](https://cdn.hackclub.com/01a13641-a71d-7d14-9f58-78a9270f6fa4/image.png)![image.png](https://cdn.hackclub.com/01a13641-bac9-73c7-b569-4ea3cb215d63/image.png)

# 2026-10-13: Lenovo K5+ Recovery Experiments and Linux Boot Research

**Total time spent: 7 hours**

Today, since it was a holiday, I had more time to work on my DIY Alexa project. I continued trying to repurpose my Lenovo K5+ (A6020a46), which has a corrupted Android 5.1 installation and problems booting reliably. I attempted to boot TWRP recovery so I could replace Android 5.1 with LineageOS 14.1. However, the recovery images repeatedly failed to load properly. I also suspected that some partitions of the phones eMMC NAND might have degrade which could just as well make  the phone useless and lead to the problems I am having right now. After trying many different TWRP images without success, I decided to explore another approach instead of repeating the same process. I managed to open LS2nd 23.1, which gave a new direction to my research, but I would have to access ADB device commands to get more info about it. With some help from AI models and online research, I discovered a possible way to run Linux on the Lenovo phone using an SD card. I quickly went and purchased an SD card adapter and started preparing the files by changing the card's file system from FAT32 to Ext2 to match LS2nd requirements. 

After inserting the SD card,d the phone successfully detected it, but the process failed, leaving me with more problems to find solutions for. I still need to determine whether the issue is caused by the filesystem, boot config, compatibility, or the suspected internal storage problem.

![image.png](https://cdn.hackclub.com/01a13632-5485-7093-a753-51569e6c8d6a/image.png)
![image.png](https://cdn.hackclub.com/01a13632-6948-7e49-9560-e7cb2ff62ff4/image.png)![image.png](https://cdn.hackclub.com/01a13632-7f36-72b6-92c4-b99f18a5fa46/image.png)![image.png](https://cdn.hackclub.com/01a13632-8e1b-7b94-830d-aca90a9becd5/image.png)
![Uploading image.png...]()


# 2026-10-13: Physical Blueprint, Component Arrangement, and Thermal Planning

**Total time spent: 3.5 hours**

After yesterday's research and failure, I may or may not have failed to get the required result, so I shifted my focus toward designing the physical structure of the DIY Alexa. I think this should be a good step, as the parts would eventually need to fit inside an enclosure, remain accessible for maintenance,e and be arranged in a way that it feels like a true stereo setup. I began developing a blueprint for the overall arrangement. The plan needed to account for the fairly big speakers, amplifier, the available connections, and the space required for the other parts. But I soon realised just how big a problem heat would become. The amplifier, LM2596, and the phone would be running in an enclosed space, so I wanted to avoid designing an enclosure that would trap excessive heat. So,o I considered component placement and airflow while working on the layout. I think the main intention of all this was to account for the thermal concerns during the design phase rather than waiting until everything had been assembled

Part list -

1. Old Lenovo Vibe K5+
2. 3-inch 10 W full-range drivers (4 ohm), 2 in number for that stereo effect
3. PAM8610 amplifier board 10w + 10W with DC jack, 3.5 mm aux port and knob
4. Soundcard
5. Micro USB cable
6. 2 Aux cables
7. MDF wood
8. a old router adapter 9v
9. An old other phone (JIO) used just as a display (Optional)
10. LM2596 buck converter 
11. BMS of lenovo K5+
12. Vinyl and cloth for style
13. Denim
14. soundcard
15. USB to micro USB OTG

![image.png](https://cdn.hackclub.com/01a13613-0a38-7e8e-b8e9-8197b397694a/image.png)
![image.png](https://cdn.hackclub.com/01a13613-2d7c-79d0-9e80-d8778c18a4e3/image.png)
![image.png](https://cdn.hackclub.com/01a13617-96bd-79f1-aeb1-0ead124152ef/image.png)

# 2026-10-13: Android ROM Research and Software Troubleshooting

**Total time spent: 3.5 hours**

After successfully powering on the Lenovo phone, I began investigating whether its corrupted Android installation could be repaired or replaced. The phone's software is a major dependency for the project because the phone would need to operate reliably before it could be configured for its intended role. Well, simply getting the phone on wasn't enough to run the operating system,m and it remained unusable. Spent time researching the possibility of flashing the ROM onto the phone. This requires some more investigation on the software side of the phone (only for this part did I use some help from AI models), since I really was not experienced in this area. I had to learn and tried to adapt [failed: it's way too complicated] to do so. I worked through every common and possible approach, reading different git hub posts on the way to try and fix it,t but to no avail. Flashing the ROM is no joke and is taking a considerable amount of time. Since this phone uses a Qualcomm processor, I tried using QFIL, L but it also showed a Sahara error, so there might be a possibility of the eMMC not working, but I am not really sure.

![image.png](https://cdn.hackclub.com/01a135f3-9b3c-7115-b729-bcbe95f67630/image.png)

 

# 2026-10-13: Lenovo Vibe K5+ Disassembly and Battery-Related Experimentation

**Total time spent: 3.5 hours**

Once I had a more defined idea of the hardware setup, I turned my attention to the main brain and backbone of the project: the old Lenovo K5+, which I intended to repurpose for the project. But it presented a problem before I even began working on it because it had been kept for so long that the battery had discharged a bit too much beyond the minimum, causing it to become useless. So before even fixing the software, I kinda needed to find out whether the phone even works or turns on . I began disassembling the Lenovo phone and looking at its internal arrangement. Doing this expose the batter pin so that gave a way to hook up a external battery which I had it is a 1700 mah battery at 3.8v which is more than enough for the phone to turn on but to noones surprose it didnt work but after some research and searching around I found out without any thing in the middle pin the phone thinks the battery is too clod so I found a wa out of this by putting a 10kΩ resister between the negeive and middle pin of the phone pins by using a jumper wire and finally after hours it showed signs of life turning on. But let's just say I soon realised this is just the beginning of my problems with this phone, since from what I remember,mber the Android on this phone is HEAVILY corrupted, so it's going to be a hell of a lot of trouble ahead.

![image.png](https://cdn.hackclub.com/01a135c2-3d11-7e28-a108-c18bcf6bcbcb/image.png)
![image.png](https://cdn.hackclub.com/01a135c2-6463-78bb-98f9-6da9af7aa0d1/image.png)
![image.png](https://cdn.hackclub.com/01a135c2-c92d-758d-908a-35d7cc4e9100/image.png)

# 2026-10-13: Component Hunting + Audio-System Research

**Total time spent: 3 hours**

After the initial hardware exploration, I moved on to researching and identifying the components needed to create the intended audio system. Rather than selecting parts randomly,y which would just be stupid, I researched how different components would work with each other and what each part would contribute to the final build, because I really don't want to waste my money or the funds provided on useless things. The main goal is making a setup capable of producing stereo sound while remaining compact enough to fit inside a custom enclosure. I searched online for some CHEAP suitable speaker drivers and came across these3-inch 10 W full-range 4-ohmm drivers. I  also identified the PAM8610 amplifier board as a good candidate, featuring a volume knob, a 3.5 mm aux port, and,d most importantly, it was rated for 1ow in each channel, exactly what I need. I continued with the research work and made a BOM (I think not exactly,u but close enough) including a sound card, microUSB cable, aux cable, MDF wood for the enclosure and a 9V power adapter. I think all these parts should work nicely together and prove to be of good quality (hopefully)

![image.png](https://cdn.hackclub.com/01a135b5-c911-7e1e-a8f6-5349db414292/image.png)

# 2026-10-13: Initial Hardware Exploration  and Laptop Disassembly 

**Total time spent: 3 hours**

Today is the first day of one of my actual big projects; it's 28 September (I started my devlog a bit late, to say the least,t since I didn't actually know about Hack Club and was having account verification problems ) 

I began my project by trying to use any old electronic hardware I could find which could be useful in making the DIY Alexa. I have an old Compaq laptop, which was quite annoying to open up, but after some struggle, I got it open, but soon found that, except for the USD 2.0 daughterboard, almost everything was useless for the project. Initially, I  was thinking of using the laptop's internal speakers as the audio output, but I tested them, and the sound sounded horrible, to say the least, so to provide a reasonable stereo sound system, I decided it would be easier to just use some good speaker drivers. I soon realised that if I wanna actually make progress, ss I'd have to prioritise using compatible parts instead of using anything that's just available. I also opened up an old Bluetooth headset because I thought that the Bluetooth module might come in handy in the future. 

![image.png](https://cdn.hackclub.com/01a1359f-14f9-7d3e-a22c-9005e20b982f/image.png)
![image.png](https://cdn.hackclub.com/01a135a0-0f7b-7c71-abe9-42362e4f1018/image.png)
![image.png](https://cdn.hackclub.com/01a135a2-8383-7bc1-bb0f-ee93cd66eded/image.png)

