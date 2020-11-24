# LoopColors
Simple script to make a video looping colours of a pallette

## What is this?

I made a moving Roicket!:

[[embed url=Rocket.mp4]]


This started to proof my argument to a friend (and others on the net) that the animation in this gif below 
has nothing to do with the animated part on the bottom right, but JUST about **how** the colours loop between borders and main.

https://twitter.com/jagarikin/status/1329610899976437765

[[embed url=https://video.twimg.com/tweet_video/EnO5_78UwAAbWEm.mp4]]

So:
* I just did an svg image with a rocket with three colours. 
* then I made a bmp file with it
* I made a script that replaces each of those colors by one of the looping colors
* created a video with ffmpeg
* voilà 
It looks like two rockets getting closer but also rotating.

## ... (really?)
Well, cmon, it was a hollyday today. 

## yea sure... How I make one with these scripts?

Just be sure you have python and ffmpeg. Then just run:
```
python LoopColours.py ; ffmpeg -i Output_%2d.bmp Output.mp4; ffmpeg -f concat -i files.txt   Rocket.mp4 ; mpv Rocket.mp4
```

## So how exactly works?
There is something to do with border colours w.r.t. main color. Not sure. So Basically it loops over the following 12 colours:

| N  | RGB      | Color                                               |
|----|----------|-----------------------------------------------------|
| 1  | 80 fa 7b | <span style="color:#80fa7b">some *blue* text</span> |
| 2  | bd e6 3b | bde63b                                              |
| 3  | 13 be e6 | 13bee6                                              |
| 4  | 01 7c f9 | 017cf9                                              |
| 5  | 12 3c e9 | 123ce9                                              |
| 6  | 3f 11 bc | 3f11bc                                              |
| 7  | 7f 02 fa | 7f02fa                                              |
| 8  | be 14 3b | be143b                                              |
| 9  | e9 3e 12 | e93e12                                              |
| 10 | fb 7c 03 | fb7c03                                              |
| 11 | e7 bc 10 | e7bc10                                              |
| 12 | bd e6 3b | bde63b                                              |


