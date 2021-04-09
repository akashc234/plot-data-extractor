from static.main import mainFunc
from static.axis import axisFunc
from static.pngcon import pngConversion

def predictor(xmax):
    axisFunc()
    pngConversion()
    return mainFunc(xmax)