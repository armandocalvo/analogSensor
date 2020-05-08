#We import the spidev and time libraries and open the SPI bus with the command spi.open(0, CHIP_SELECT_0_OR_1)
import spidev
from time import sleep

spi = spidev.SpiDev()
spi.open(0, 0)                              #

sleepTime = 1

#Funtions to read the channel from the MCP3008, convert the reading to voltage and then convert the voltage to pressure

def getReading(channel):
  rawData = spi.xfer([1, (8 + channel) << 4, 0])            #Takes the raw value of the MCP3008
  processedData = ((rawData[1] & 3) << 8) + rawData[2]      #Process the raw value
  return processedData                                      #Return the process value
  
def convertVoltage(bitValue, decimalPlaces = 2):
  voltage = (bitValue * 3.3) / float(1023)                  #Formula to convert the bit value to voltage
  voltage = round(voltage, decimalPlaces)                   #Round the data to two decimals
  return voltage                                            #Return the value in terms of voltage

def convertPressure(voltage, decimalPlaces = 2):
  pressure = ((voltage * 1.2) / 3.3)                        #Formula to convert the voltage to pressure
  pressure = round(pressure, decimalPlaces)                 #Round the data to two decimals
  return pressure                                           #Return the value in terms of pressure

#Reads the value all the time, needs to be modified according the application
while True:
  sensor1Data = getReading(sensor1Channel)
  #sensor2Data = getReading(sensor2Channel)
  #sensor3Data = getReading(sensor3Channel)
  #sensor4Data = getReading(sensor4Channel)
  
  sensor1Voltage = convertVoltage(sensor1Data)
  #sensor2Voltage = convertVoltage(sensor2Data)
  #sensor3Voltage = convertVoltage(sensor3Data)
  #sensor4Voltage = convertVoltage(sensor4Data)
  
  pressure1 = convertPressure(sensor1Voltage)
  #pressure2 = convertPressure(sensor2Voltage)
  #pressure3 = convertPressure(sensor3Voltage)
  #pressure4 = convertPressure(sensor4Voltage)
  
  print("FP1: {}V --> {}MPa".format(sensor1Voltage, pressure1))
  #print("FP2: {}V --> {}MPa".format(sensor2Voltage, pressure2))
  #print("FP3: {}V --> {}MPa".format(sensor3Voltage, pressure3))
  #print("FP4: {}V --> {}MPa".format(sensor4Voltage, pressure4))
  
  sleep(sleepTime)
