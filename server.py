import eel
import serial
eel.init('web')

port = "COM6"
cereal = serial.Serial(port, 9600)

def readMhorcel():
    #this is the function to handle the serial thread
    global cereal
    while True:
        print ('In readMhorcel-thread')
        data = cereal.read(256)
        if len(data) > 0:
            print(data)
            eel.renderData(data)
        eel.sleep(5.0)

@eel.expose
def sendMhorcel(data):
    global cereal
    try:
        cereal.write(data)
    except:
        print('an error occurred')



options = {
    'host': 'localhost',
    'port': 8080,
    'block': False
}

eel.spawn(readMhorcel)
eel.start('main.html', options)

while True:
    eel.sleep(2.0)
