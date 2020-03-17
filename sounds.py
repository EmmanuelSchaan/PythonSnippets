from pyaudio import PyAudio   # to play sounds
from scipy.io import wavfile  # to save wav files
import numpy as np

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
#number of frames per second
bitRate = 44100
# freq in Hz
# choose freq between 100Hz and 5000Hz
freq = 2.e2
# duration of sound in seconds
duration = 2.

# number of useful / empty frames
nFrame = int(bitRate * duration)
nEmptyFrame = nFrame % bitRate


##################################################################
# generate sound wave

frame = np.arange(nFrame)  # in Hz
time = frame.astype(float) / bitRate  # in sec
amplitude = np.sin(2.*np.pi*freq*frame/bitRate) # between -1 and 1


##################################################################
# save to wav file

# convert to int32, in [-2147483648, 2147483647]
amplitude = - 0.5 + 2147483647.5 * amplitude
amplitude = np.int32(amplitude)
wavfile.write('./test.wav', bitRate, amplitude)


##################################################################
# play sound
#
## convert amplitude to [0, 255]
#amplitude = (127.5 + 127.5*amplitude).astype(int)
## get string from sound wave
#soundString = ''
#for i in range(nFrame):
#   soundString += chr(amplitude[i])
#for i in range(nEmptyFrame):
#   soundString = soundString+chr(128)
#
## play the sound
#p = PyAudio()
#stream = p.open(format = p.get_format_from_width(1), 
#                channels = 1, 
#                rate = bitRate, 
#                output = True)
#stream.write(soundString)
#stream.stop_stream()
#stream.close()
#p.terminate()












