# DEFINING VARIABLES
scannedCodeList = []
maximumScanValue = 0
percentScanValue = 0
sumScannedChars = 0
hertzValue = 0

# NOTES #
# central 3 octaves range from 16.35Hz to 130.81Hz
# the differece between the two is 114.46
# the higher the barcode value, the higher the pitch between three octaves, C0-C3

# FUNCTION TO CONVERT SCANNED CODE INTO NUMBERS
def Convert(scannedCodeList):
  scannedCode = str(input("Scan code: "))
  for char in scannedCode:
    if str(char).isdigit():
      scannedCodeList.append(int(char))
    elif str(char).isalpha():
      scannedCodeList.append(int((ord(char))-97))
  return(scannedCodeList)
  
convertedScan = Convert(scannedCodeList)



# FUNCTION TO CONVERT INTEGER CODE INTO HERTZ
def findHertz(scannedCodeList, maximumScanValue, percentScanValue, sumScannedChars, hertzValue):
  maximumScanValue = (len(scannedCodeList))*25
  
  for char in scannedCodeList:
    sumScannedChars += char
  percentScanValue = (sumScannedChars/(maximumScanValue))
  
  
  
  hertzValue = (percentScanValue*114.46)+16.35
  #print(percentScanValue)
  #print(scannedCodeList)
  
  return(hertzValue)

#print(findHertz(scannedCodeList, maximumScanValue, percentScanValue, sumScannedChars, hertzValue))

# SINE WAVE STUFF, lovingly nicked from stack overflow

import time

import numpy as np
import pyaudio

p = pyaudio.PyAudio()

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 1.0  # in seconds, may be float
f = findHertz(scannedCodeList, maximumScanValue, percentScanValue, sumScannedChars, hertzValue)  # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

# per @yahweh comment explicitly convert to bytes sequence
output_bytes = (volume * samples).tobytes()

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
              channels=1,
              rate=fs,
              output=True)

# play. May repeat with different volume values (if done interactively)
start_time = time.time()
stream.write(output_bytes)
#print("Played sound for {:.2f} seconds".format(time.time() - start_time))

stream.stop_stream()
stream.close()
p.terminate()