#!env python


Colors = [
        [b'\x80', b'\xfa', b'\x7b'],
        [b'\xbd', b'\xe6', b'\x3b'],
        [b'\x13', b'\xbe', b'\xe6'],
        [b'\x01', b'\x7c', b'\xf9'],
        [b'\x12', b'\x3c', b'\xe9'],
        [b'\x3f', b'\x11', b'\xbc'],
        [b'\x7f', b'\x02', b'\xfa'],
        [b'\xbe', b'\x14', b'\x3b'],
        [b'\xe9', b'\x3e', b'\x12'],
        [b'\xfb', b'\x7c', b'\x03'],
        [b'\xe7', b'\xbc', b'\x10'],
        [b'\xbd', b'\xe6', b'\x3b'],
        ]

TotalLoops = 6


ColorMain = [b'\x55', b'\x55', b'\x55']
ColorPrev = [b'\xaa', b'\xaa', b'\xaa']
ColorNext = [b'\xd7', b'\xd7', b'\xf4']

ColorLoops = len(Colors)


for i in range(ColorLoops):
    f = open('Rocket.bmp', 'r+b')
    outname = str(i)
    if i<10:
        outname='0'+outname

    outname = 'Output_'+outname+'.bmp'


    nextidx = i+3
    if nextidx >= ColorLoops:
        nextidx -= ColorLoops

    previdx = i-3
    if previdx < 0:
        previdx += ColorLoops

    ColorPrevTo = Colors[previdx]
    ColorMainTo = Colors[i]
    ColorNextTo = Colors[nextidx]

    NewImg = f.read().replace(ColorMain[0]+ColorMain[1]+ColorMain[2],ColorMainTo[0]+ColorMainTo[1]+ColorMainTo[2])
    NewImg = NewImg.replace(ColorPrev[0]+ColorPrev[1]+ColorPrev[2],ColorPrevTo[0]+ColorPrevTo[1]+ColorPrevTo[2])
    NewImg = NewImg.replace(ColorNext[0]+ColorNext[1]+ColorNext[2],ColorNextTo[0]+ColorNextTo[1]+ColorNextTo[2])

    o = open(outname,'w+b')
    o.write(NewImg)








