import drawsvg as draw
import random

pixels = []
width = 5
height = 3

for i in range(0,width*height):
    pixels.append(random.randint(0,255))

pixelSize = 80
gridPadding = 0
outsidePadding = 20

primaryColor = "#10BB9E"
secondaryColor = "#257265" 

svgWidth = width*pixelSize + (width-1)*gridPadding + 2*outsidePadding
svgHeight = height*pixelSize + (height-1)*gridPadding + 2*outsidePadding

d = draw.Drawing(svgWidth, svgHeight)

def rgbToHex(r,g,b):
    def clamp(x): 
        return max(0, min(x, 255))

    return "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))

def drawImage(d):
    y=-1
    for i in range(0,len(pixels)):
        x = i % width
        if(x == 0): y+=1

        r = draw.Rectangle(x*pixelSize + x*gridPadding + outsidePadding, y*pixelSize + y*gridPadding + outsidePadding, pixelSize, pixelSize, fill=rgbToHex(pixels[i],pixels[i],pixels[i]))

        d.append(r)

def drawTConstruction(d):
    for y in range(0,height+1):
        for x in range(0,width+1):
            # Vertice position
            vx = x*(pixelSize+gridPadding) + outsidePadding - 1/2*gridPadding
            vy = y*(pixelSize+gridPadding) + outsidePadding - 1/2*gridPadding

            if(x!=width and y!=height):
                r = draw.Rectangle(
                    vx, vy,
                    pixelSize+gridPadding, pixelSize+gridPadding,
                    fill=primaryColor, fill_opacity=0.4
                )
                d.append(r)

                imgCoord = x+y*width;
                d.append(draw.Text(
                    str(pixels[imgCoord]),
                    10,
                    vx + 1/2*(pixelSize + gridPadding), vy + 1/2*(pixelSize + gridPadding),
                    fill="white",
                    dominant_baseline="central", text_anchor="middle",
                    font_family="JetBrains Mono",
                    stroke=secondaryColor,
                    stroke_width=3,
                    paint_order="stroke fill markers",
                    stroke_linejoin="round"
                ))

            if(x!=width):
                l1 = draw.Line(
                    vx, vy,
                    vx + (pixelSize+gridPadding), vy,
                    stroke=primaryColor,
                    stroke_width="6"
                )
                d.append(l1)

                pixelVals = []

                if(y!=0):
                    pixelVals.append(pixels[x+(y-1)*width])
                    
                if(y<height):
                    pixelVals.append(pixels[x+y*width])

                d.append(draw.Text(
                    str(min(pixelVals)),
                    10,
                    vx + 1/2*(pixelSize + gridPadding), vy,
                    fill="white",
                    dominant_baseline="central", text_anchor="middle",
                    font_family="JetBrains Mono",
                    stroke=secondaryColor,
                    stroke_width=3,
                    paint_order="stroke fill markers",
                    stroke_linejoin="round"
                ))

            if(y!=height):
                l2 = draw.Line(
                    vx, vy,
                    vx, vy + (pixelSize+gridPadding),
                    stroke=primaryColor,
                    stroke_width="6"
                )
                d.append(l2)

                pixelVals = []

                if(x!=0):
                    pixelVals.append(pixels[(x-1)+y*width])
                    
                if(x<width):
                    pixelVals.append(pixels[x+y*width])

                d.append(draw.Text(
                    str(min(pixelVals)),
                    10,
                    vx, vy + 1/2*(pixelSize + gridPadding),
                    fill="white",
                    dominant_baseline="central", text_anchor="middle",
                    font_family="JetBrains Mono",
                    stroke=secondaryColor,
                    stroke_width=3,
                    paint_order="stroke fill markers",
                    stroke_linejoin="round"
                ))

            c = draw.Circle(vx, vy, 6, fill=primaryColor, stroke=secondaryColor, stroke_width="2")
            d.append(c)

            pixelVals = []

            if(x!=0):
                if(y<height): pixelVals.append(pixels[(x-1)+y*width])
                if(y!=0): pixelVals.append(pixels[(x-1)+(y-1)*width])
            if(x<width):
                if(y<height): pixelVals.append(pixels[x+y*width])
                if(y!=0): pixelVals.append(pixels[x+(y-1)*width])

            d.append(draw.Text( 
                str(min(pixelVals)),
                8,
                vx, vy,
                fill="white",
                dominant_baseline="central", text_anchor="middle",
                font_family="JetBrains Mono",
                stroke=secondaryColor,
                stroke_width=3,
                paint_order="stroke fill markers",
                stroke_linejoin="round"
            ))


def drawVConstruction(d): 
    for y in range(0,height):
        for x in range(0,width):
            # Vertice position
            vx = x*pixelSize + 1/2*pixelSize + x*gridPadding + outsidePadding
            vy = y*pixelSize + 1/2*pixelSize + y*gridPadding + outsidePadding

            if(x<width-1 and y<height-1):
                r = draw.Rectangle(
                    vx, vy,
                    pixelSize+gridPadding, pixelSize+gridPadding,
                    fill=primaryColor, fill_opacity=0.4
                )
                d.append(r)

                pixelVals = [
                    pixels[x+y*width],
                    pixels[(x+1)+y*width],
                    pixels[x+(y+1)*width],
                    pixels[(x+1)+(y+1)*width]
                ]

                d.append(draw.Text(
                    str(max(pixelVals)),
                    10,
                    vx + 1/2*(pixelSize + gridPadding), vy + 1/2*(pixelSize + gridPadding),
                    fill="white",
                    dominant_baseline="central", text_anchor="middle",
                    font_family="JetBrains Mono",
                    stroke=secondaryColor,
                    stroke_width=3,
                    paint_order="stroke fill markers",
                    stroke_linejoin="round"
                ))

            if(x<width-1):
                l1 = draw.Line(
                    vx, vy,
                    vx + (pixelSize+gridPadding), vy,
                    stroke=primaryColor,
                    stroke_width="6"
                )
                d.append(l1)

                pixelVals = [pixels[x+y*width], pixels[(x+1)+y*width]]

                d.append(draw.Text(
                    str(max(pixelVals)),
                    10,
                    vx + 1/2*(pixelSize + gridPadding), vy,
                    fill="white",
                    dominant_baseline="central", text_anchor="middle",
                    font_family="JetBrains Mono",
                    stroke=secondaryColor,
                    stroke_width=3,
                    paint_order="stroke fill markers",
                    stroke_linejoin="round"
                ))

            if(y<height-1):
                l2 = draw.Line(
                    vx, vy,
                    vx, vy + (pixelSize+gridPadding),
                    stroke=primaryColor,
                    stroke_width="6"
                )
                d.append(l2)

                pixelVals = [pixels[x+y*width], pixels[x+(y+1)*width]]

                d.append(draw.Text(
                    str(max(pixelVals)),
                    10,
                    vx, vy + 1/2*(pixelSize + gridPadding),
                    fill="white",
                    dominant_baseline="central", text_anchor="middle",
                    font_family="JetBrains Mono",
                    stroke=secondaryColor,
                    stroke_width=3,
                    paint_order="stroke fill markers",
                    stroke_linejoin="round"
                ))

            c = draw.Circle(vx, vy, 6, fill=primaryColor, stroke=secondaryColor, stroke_width="2")
            d.append(c)

            imgCoord = x+y*width
            d.append(draw.Text( 
                str(pixels[imgCoord]),
                8,
                vx, vy,
                fill="white",
                dominant_baseline="central", text_anchor="middle",
                font_family="JetBrains Mono",
                stroke=secondaryColor,
                stroke_width=3,
                paint_order="stroke fill markers",
                stroke_linejoin="round"
            ))

drawImage(d)
drawTConstruction(d)

d.set_pixel_scale(2)
d.save_svg('ccv.svg')