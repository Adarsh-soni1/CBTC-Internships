#using libraries sounddevice, scipy , wavio

from scipy.io.wavfile import write
import wavio as wo
import sounddevice as sd

#setting frequency
freq=44100

#time duration in seconds.
time_duration=10

#recording started
print("\n=============================RECORDING STARTED==========================\n")
voice_recording=sd.rec(int(time_duration*freq),samplerate=freq,channels=2)

#hold of 10 seconds
sd.wait()

#recording is saved on your device
write("recordvoice.wav",freq,voice_recording)

print("\n=============================RECORDING STOPPED==========================\n")