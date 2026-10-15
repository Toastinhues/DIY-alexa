# Project Timeline Notes <h1>

## Initial Hardware Exploration

- Disassembled an old Compaq laptop to investigate reusable parts.
- Considered using its speakers but rejected the idea because they did not suit the intended use.
-Researched the proper hardware configuration for the audio setup
- Researched what cables to use, a soundcard, MDF wood, and power options
- Disassembled a working Bluetooth headphone to recover its PCB.
- Disassembled a Lenovo K5+ with a non-functional battery
- Experimented with a Motorola battery and a 10 kω resistor
- The phone booted, but the Android was heavily corrupted
- Investigated ROM flashing but did not complete it
- Began designing the enclosure and considering heat management

## Recovery and Linux Experiments

- Attempted to boot TWRP to investigate a LineageOS install
- Tried alternative recovery images
- Suspected internal eMMC storage degradation, but did not confirm the diagnosis.
- InvestigatedLK2ndd 23.1 and possible Linux-on-SD approach
- Prepared an SD card using an Ext2 filesystem
- The phone detected the card, but the Linux boot did not complete

## Component Harvesting and Audio research

- Removed an old computer power supply for component recovery
- Attempted to dismantle an old charger for diodes but failed
- Researched possible ground-loop noise in the audio system
- Retried the Linux boot process without success

## Ubuntu and TWRP Troubleshooting 

- Used an existing Ubuntu Installation to prepare storage.
- It appeared to detect the SD card but became stuck
- The suspected eMMC failure turned out to be true (hence the pivot )
- Later managed to boot TWRP v3.3.1 and access ADB commands
- Further testing did not establish reliable phone operation

## Raspberry Pi Research

- Investigated a Raspberry Pi 4 or above ( with at least 4GB RAM )
- Began developing a new hardware blueprint
- Considered an ESP32 but had concerns about response latency ( more than 20 seconds )
- Continued evaluating the hardware and budget requirements 
