import cv2
import numpy as np
from PIL import Image
import operator
import os
flist, fdlist = [], []
UPLOAD_FOLDER = os.path.join('static', 'img')
path = os.path.join(UPLOAD_FOLDER, 'current.png')
# cv2.imwrite('cropped_sw_corner-canny.png', edges)


def axisFunc():
    print(path)
    img = cv2.imread(path, 1)
    edges = cv2.Canny(img, 100, 200)
    lines = cv2.HoughLinesP(image=edges, rho=0.8, theta=np.pi/180, threshold=100, lines=np.array([]), minLineLength= 100, maxLineGap= 5)
    # print(lines)
    for l in lines:
        for x1, y1, x2, y2 in l:
            # cv2.line(img,(x1,y1),(x2,y2),(0,0,255), 1)
            line_val = [x1,y1,x2,y2]
            #cv2.imwrite('houghlines.jpg', gray)
            x_co = abs(x2-x1)
            y_co = abs(y2-y1)
            del_value = [x_co, y_co]
        flist.append(line_val)
        fdlist.append(del_value)
    # print(flist, fdlist, len(flist))
    for max_valx, max_valy in enumerate(fdlist):
        value1 = max(fdlist, key = lambda x: x[0])
        value2 = max(fdlist, key = lambda x: x[1])
    ixval= fdlist.index(value1)
    iyval = fdlist.index(value2)
    finalx = flist[ixval]
    finaly = flist[iyval]
    fline = [flist[ixval], flist[iyval]]
    # print(fline)
    # print(ixval, iyval, fline, type(fline))

    for i in range(len(fline)):
        x11 = fline[i][0]
        y11 = fline[i][1]
        x22 = fline[i][2]
        y22 = fline[i][3]
        cv2.line(img, (x11, y11), (x22, y22), (0, 0, 255), 1)
        cv2.imwrite('./static/houghline/houghlines.jpg', img)

    # ROI

    if finalx[0] > finalx[2]:
        bottomright = [finalx[0], finalx[3]]

    elif finalx[2] > finalx[0]:
        bottomright = [finalx[2], finalx[3]]

    if finaly[1] < finaly[3]:
        topleft = [finaly[0], finaly[1]]

    elif finaly[3] < finaly[1]:
        topleft = [finaly[0], finaly[3]]


    image = Image.open(path)
    crop = image.crop((topleft[0],topleft[1],bottomright[0],bottomright[1]))
    crop.save("./static/cropped/crop.png")
    return (topleft, bottomright)