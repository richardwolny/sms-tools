import numpy as np
from scipy.signal import get_window
import matplotlib.pyplot as plt
import os, sys
sys.path.append('../../software/models/')
import utilFunctions as UF
import stft as STFT

inputFile = '../../sounds/flute-A4.wav'
window = 'hamming'
M = 801
N = 1024
H = 480

(fs, x) = UF.wavread(inputFile)

w = get_window(window, M)

mX, pX = STFT.stftAnal(x, fs, w, N, H)
