import eel
import serial
eel.init('web')

port = "COM6"
cereal = serial.Serial(port, 9600, timeout=0)

def readMhorcel():
	#this is the function to handle the serial thread
	global cereal
	while True:
		print('In readMhorcel-thread')
		data = cereal.read(256).decode('ascii')
		print('after read')
		if len(data) > 0:
			print(data)
			eel.renderData(data)
		eel.sleep(5)

@eel.expose
def sendMhorcel(data):
	global cereal
	try:
		cereal.write(data.encode())
	except Exception as e:
		print(e)



options = {
        'host': 'localhost',
        'port': 8080,
        'block': False
}

eel.start('main.html', options, block=False)
eel.spawn(readMhorcel)

while True:
	print('in main thread')
	eel.sleep(2)
