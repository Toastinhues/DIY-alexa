## AlexaTap 

It is an app developed just for one thing, and that is sending 
- the artist name
- the song title
- the name of the track
- where it is playing from
- Send all that data to the Render website
  
## _BUT HOW DOES THE SPEAKER KNOW WHAT TO PLAY FROM JUST A TAP_

I have set up a very lightweight, simple server from Render and Flask, which has a last-played API system. When you open that web link it redirects you to the app AlexaTap and that automatically sends the data 

An example of it capturing the last played song 

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/16056ef2-3b8e-41e7-b511-50e07cb79a1b" />

<img width="1917" height="543" alt="image" src="https://github.com/user-attachments/assets/5991d3f6-ab9a-4113-9cb6-2660e9205082" />

>match score 22 is highest 


The main problem wasn't playing that song from the title (it still was a pain); it was getting the title and data itself because new Androids and iPhones do not actually share any data, such as notifications to a random NFC tag, for obvious reasons. So the completely seamless option was dead before it even began, hence why AlexaTap was made

When you download AlexaTap, it just asks for one permission: enable notification access, and that is how it is able to send the data over to the endpoint that is https://diy-alexa-website.onrender.com/ it then checks youtube for that song and the song with the highest match score gets played through VLC without any ads ;D

## but what if you don't have the app 

then the app does not get redirected from the link hence it stays on the link only and from there you can install the app 

## Thanks for staying with me through this process. If you wanna check out the software, feel free to do so, and don't forget to give me feedback at toastinroast.dgdts@gmail.com 








