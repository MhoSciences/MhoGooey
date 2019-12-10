import eel
import serial

# port = "/dev/tty.usbserial-00000000"
# cereal = serial.Serial(port, 9600)

@eel.expose
def readMhorcel():
    #this is the function to handle the serial thread
    #global cereal
    while True:
        data = 'hi'#cereal.read(256)
        if len(data) > 0:
            print(data)
            eel.renderData(data)
        sleep(1)

def sendMhorcel(data):
    #global cereal
    try:
        print('hello')
        #cereal.write(data)
    except:
        print('an error occurred')

eel.init('web')

options = {
    'host': 'localhost',
    'port': 80,
    'block': False
}

eel.start('web/main.html', options)

while True:
    eel.sleep(10);
