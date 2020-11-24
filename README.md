# LoopColors
Simple script to make a video looping colours of a pallette

## What is this?

I made a gif with looping colours that seems its moving:

![Rocket](mpv-shot0001.jpg)
[Check here!](https://github.com/monticellifernando/LoopColors/blob/main/Rocket.mp4?raw=true)


This started to proof my argument to a friend (and others on the net) that the animation in this gif below 
has nothing to do with the animated part on the bottom right, but JUST about **how** the colours loop between borders and main.

https://twitter.com/jagarikin/status/1329610899976437765


So:
* I just did an svg image with a rocket with three colours. 
* then I made a bmp file with it
* I made a script that replaces each of those colors by one of the looping colors
* created a video with ffmpeg
* voilà 
It looks like two rockets getting closer but also rotating.

## ... (really?)
Well, cmon, it was a holiday! I had to do smth to stop working a bit!

## yea sure... How I make one with these scripts?

Just be sure you have python and ffmpeg. Then just run:
```
python LoopColours.py ; ffmpeg -i Output_%2d.bmp Output.mp4; ffmpeg -f concat -i files.txt   Rocket.mp4 ; mpv Rocket.mp4
```

## So how exactly works?
There is something to do with border colours w.r.t. main color. Not sure. So Basically it loops over the following 12 colours:

| N  | RGB                                                      |
|----|----------------------------------------------------------|
| 1  | <span style="background-color:#80fa7b"> 80 fa 7b </span> |
| 2  | <span style="background-color:#bde63b"> bd e6 3b </span> |
| 3  | <span style="background-color:#13bee6"> 13 be e6 </span> |
| 4  | <span style="background-color:#017cf9"> 01 7c f9 </span> |
| 5  | <span style="background-color:#123ce9"> 12 3c e9 </span> |
| 6  | <span style="background-color:#3f11bc"> 3f 11 bc </span> |
| 7  | <span style="background-color:#7f02fa"> 7f 02 fa </span> |
| 8  | <span style="background-color:#be143b"> be 14 3b </span> |
| 9  | <span style="background-color:#e93e12"> e9 3e 12 </span> |
| 10 | <span style="background-color:#fb7c03"> fb 7c 03 </span> |
| 11 | <span style="background-color:#e7bc10"> e7 bc 10 </span> |
| 12 | <span style="background-color:#bde63b"> bd e6 3b </span> |

Then the loop is like:
* Main area is color N
* One border is color N+3 (in the "forward" part)
* Other border is Color N-3 (in the "rear" part)



## And WHY it  works?
No F%$ng clue...
