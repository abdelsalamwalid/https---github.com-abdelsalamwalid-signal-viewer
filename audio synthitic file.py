import numpy as np
import simpleaudio as sa
F_1 = 4200
F_2 = 100
F_3 = 2000
fs = 44100
seconds = 4
t = np. linspace(0,seconds, seconds*fs, False)
note_1 = 2*np.cos(F_1*t*2*np.pi)
note_2 = 5*np.sin((F_2*t*2*np.pi)+ np.pi/2)
note_3 = 1.4*np.cos((F_3*t*2*np.pi)- np.pi/5)
sum = note_1 + note_2 + note_3
audio = (sum * (2**15 -1)) / np.max(np.abs(sum))
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj. wait_done()