import drawsvg as draw
import random

pixels = []
width = 5
height = 3

for i in range(0,width*height):
    pixels.append(random.randint(0,255))

pixelSize = 80
gridPadding = 20

svgWidth = width*pixelSize + (width+1)*gridPadding
svgHeight = height*pixelSize + (height+1)*gridPadding

d = draw.Drawing(svgWidth, svgHeight)

def rgbToHex(r,g,b):
    def clamp(x): 
        return max(0, min(x, 255))

    return "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))

y=-1
for i in range(0,len(pixels)):
    x = i % width
    if(x == 0): y+=1

    r = draw.Rectangle(x*pixelSize + (x+1)*gridPadding, y*pixelSize + (y+1)*gridPadding, pixelSize, pixelSize, fill=rgbToHex(pixels[i],pixels[i],pixels[i]))

    d.append(r)

# --- T-construction ---

# Draw vertices
for y in range(0,height+1):
    for x in range(0,width+1):
        # Vertice position
        vx = x*(pixelSize+gridPadding) + 1/2*gridPadding
        vy = y*(pixelSize+gridPadding) + 1/2*gridPadding

        if(x!=width and y!=height):
            r = draw.Rectangle(
                vx, vy,
                pixelSize+gridPadding, pixelSize+gridPadding,
                fill="lightgreen", fill_opacity=0.4
            )
            d.append(r)

            imgCoord = x+y*width;
            d.append(draw.Text(
                str(pixels[imgCoord]),
                10,
                vx + 1/2*(pixelSize + gridPadding), vy + 1/2*(pixelSize + gridPadding),
                fill="white",
                dominant_baseline="central", text_anchor="middle",
                font_family="JetBrains Mono"
            ))

        if(x!=width):
            l1 = draw.Line(
                vx, vy,
                vx + (pixelSize+gridPadding), vy,
                stroke="lightgreen",
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
                stroke="green",
                stroke_width=3,
                paint_order="stroke fill markers",
                stroke_linejoin="round"
            ))

        if(y!=height):
            l2 = draw.Line(
                vx, vy,
                vx, vy + (pixelSize+gridPadding),
                stroke="lightgreen",
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
                stroke="green",
                stroke_width=3,
                paint_order="stroke fill markers",
                stroke_linejoin="round"
            ))

        c = draw.Circle(vx, vy, 6, fill="lightgreen", stroke="green", stroke_width="2")
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
            stroke="green",
            stroke_width=3,
            paint_order="stroke fill markers",
            stroke_linejoin="round"
        ))

d.save_svg('ccv.svg')