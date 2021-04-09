from PIL import Image
import numpy as np
import webcolors
import math
import json
from colorthief import ColorThief
"""
list_of_colors = [["Black","#000000","(0,0,0)"],["White","#FFFFFF","(255,255,255)"],["Red","#FF0000","(255,0,0)"],["Lime","#00FF00","(0,255,0)"]
,["Blue","#0000FF","(0,0,255)"],["Yellow","#FFFF00","(255,255,0)"],["Cyan","#00FFFF","(0,255,255)"],["Magenta","#FF00FF","(255,0,255)"]
,["Maroon","#800000","(128,0,0)"]
,["Green","#008000","(0,128,0)"],["Purple","#800080","(128,0,128)"]]
"""

def mainFunc(xmax):
    xinput = int(xmax)
    print("Im here", xmax)
    cname = []
    ccode, ffname = [], []
    list_of_colors = [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,0,255),(128,0,0),(0,128,0),(128,0,128)]
    result =[]
    pdata, xlist, ylist =[], [], []
    count = 0
    img = Image.open("./static/png/img2.png")
    pixels = img.load()
    width, height = img.size
    # print(width, height)

    for x in range(width//20):  # this row
        for y in range(height//3):  # and this row was exchanged
            r, g, b, a = pixels[x*20, y*3]
            color = (r,g,b)
            if a == 0 or color == (0,0,0) or color == (255,255,255):
                continue
            elif a == 255 or color != (0,0,0) or color != (255,255,255):
                pass
                color = (r,g,b)
                def closest(colors, color):
                    colors = np.array(colors)
                    color = np.array(color)
                    distances = np.sqrt(np.sum((colors - color) ** 2, axis=1))
                    index_of_smallest = np.where(distances == np.amin(distances))
                    smallest_distance = colors[index_of_smallest]
                    return smallest_distance

                closest_color = closest(list_of_colors, color)
                num_list = closest_color.tolist()
                if num_list == [[255,255,255]] or num_list == [[0,0,0]]:
                    continue
                elif num_list != [[255,255,255]] or num_list != [[0,0,0]]:
                    pass
                    # ccode.append(num_list[0])
                    fx = ((x*20)/width)*xinput
                    fy = 1 - (((y*3)/height))
                    cname = webcolors.rgb_to_name(num_list[0])
                    ffname.append(cname)
                    list = [round(fx,2), round(fy,2),cname]
                    count+=1
                    result.append(list)
    fname = set(ffname)
    fname = [ x for x in iter(fname) ]
    # print(fname,count)
    #print(count, result)

    dic = {}
    for i in fname:
        dic[i] = []
    for i in result:
        dic[i[2]].append([i[0],i[1]])
    # print(dic)
    for i in dic.keys():
        print()
        print(i, dic[i])
    return dic




    """
                    with open('rgbval.json', 'w') as f:
                        json.dump(list, f)
    print('File Saved')


            hexcode = f"#{r:02x}{g:02x}{b:02x}"
            if hexcode == "#ffffff" or hexcode == "#000000":
                continue
            elif hexcode != "#ffffff" or hexcode != "#000000":
                pass
                """


            # print(x, y, f"#{r:02x}{g:02x}{b:02x}")
















    """
    def rgb2hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    img = Image.open('crop.png')

    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        pixels = img.convert('RGBA').load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                print(x, y)

                # , rgb2hex(r, g, b)
                
                """