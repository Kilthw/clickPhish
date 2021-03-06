import pyautogui
pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True

from time import sleep
import socket

def isOpen(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((ip, int(port)))
		s.shutdown(2)
		return True
	except:
		return False

def setupOutlook():
	print('Begin setup...')
	#waiting for Back/Next button
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/Back_Grey.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Account Configuration
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/AccountConfig.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/Back.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Add New Account
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/AddNewAccount.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/Back.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Security Alert
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/SecurityAlert.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/No.png')
	pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
	#waiting for Check Green Light
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/checkGreen.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/Back_Grey.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Security Alert
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/SecurityAlert.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/No.png')
	pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
	sleep(3)
	image = pyautogui.locateOnScreen('C:/clickPhish/JunkEmail.png')
	pyautogui.click(pyautogui.center(image))
	pyautogui.typewrite('o')
	pyautogui.press('up')
	sleep(1)
	pyautogui.press('enter')
	file = open('C:/clickPhish/stage.txt','w')
	file.write('2')
	file.close()
	main()

#functions for email checking and payload  execution
def closeExplorer():
	image = pyautogui.locateOnScreen('c:/clickPhish/explorerOpen.png')
	if image:
		pyautogui.click(pyautogui.center(image))
		sleep(1)
		pyautogui.hotkey('alt','f4')

def focusOutlook():
	image = pyautogui.locateOnScreen('c:/clickPhish/outlookBackground.png')
	if image:
		pyautogui.click(pyautogui.center(image))


def clearInbox():
	focusOutlook()
	print('Clearing the inbox...')
	pyautogui.click(300, 500)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'd')
	print('clearing deleted emails...')
	pyautogui.rightClick(80,320)
	pyautogui.typewrite('y')
	pyautogui.typewrite('y')
	pyautogui.click(60,170)
	return

def executePayload():
	try:
		print('Checking for attachment...')
		image = pyautogui.locateOnScreen('c:/clickPhish/message.png')
		print('Attachment found. saving...')
		pyautogui.rightClick(pyautogui.center(image)[0]+80,pyautogui.center(image)[1])
		pyautogui.typewrite('s')
		image = pyautogui.locateOnScreen('c:/clickPhish/Downloads.png')
		pyautogui.click(pyautogui.center(image))
		sleep(1)
		image = pyautogui.locateOnScreen('c:/clickPhish/Cancel.png')
		pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
		sleep(1)
		print('Found previous payload with same name. Overwriting...')
		if pyautogui.locateOnScreen('c:/clickPhish/replace.png'):
			pyautogui.press('left')
			sleep(1)
			pyautogui.press('enter')
		clearInbox()
		print('Executing payload...')
		image = pyautogui.locateOnScreen('c:/clickPhish/explorer.png')
		pyautogui.click(pyautogui.center(image))
		sleep(1)
		image = pyautogui.locateOnScreen('c:/clickPhish/Downloads.png')
		pyautogui.click(pyautogui.center(image))
		sleep(1)
		pyautogui.click(400,500)
		pyautogui.press('home')
		pyautogui.press('enter')
		pyautogui.hotkey('alt','f4')
		image = pyautogui.locateOnScreen('c:/clickPhish/outlookBackground.png')
		pyautogui.click(pyautogui.center(image))
		
	except TypeError:
		print('No attachent found...')
		clearInbox()
	return


print('Sleeping for 15 to wait for things to finish loading')
sleep(15)

#testing for Exchange server availability
ready = False
while not ready:
	print('Testing for Exchange server availability...')
	if isOpen('10.30.40.21',25):
		ready = True
	else:
		print('Unable to contact Exchange server. Sleeping for 5 before trying again...')
		sleep(5)

def main():
	file = open('C:/clickPhish/stage.txt','r')
	stage = file.read()
	print('Stage: ' + stage)
	file.close()

	if stage == '1':
		print('Waiting 3 minutes for Exchange Server to come online...')
		sleep(180)
		#Waiting for Initial Outlook Setup
		print('Looking for Outlook setup page...')
		image = None
		while image == None:
			image = pyautogui.locateOnScreen('C:/clickPhish/outlookSetup.png')

		print('Outlook setup located...')
		pyautogui.click(pyautogui.center(image))
		setupOutlook()

	if stage == '2':
		try:
			while True:
				print('Ensuring that explorer is closed...')
				closeExplorer()
				print('Ensuring that Outlook is in focus...')
				focusOutlook()
			
				#setup incoming email checking loop
				print('Watching for new incoming emails...')
				image = pyautogui.locateOnScreen('c:/clickPhish/noEmail.png')
				while image != None:
					image = pyautogui.locateOnScreen('c:/clickPhish/noEmail.png')
				print('New email detected. Processing...')
				executePayload()
		except KeyboardInterrupt:
			print('\nDone.')

main()

