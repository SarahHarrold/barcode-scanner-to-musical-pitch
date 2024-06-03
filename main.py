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

print(findHertz(scannedCodeList, maximumScanValue, percentScanValue, sumScannedChars, hertzValue))
