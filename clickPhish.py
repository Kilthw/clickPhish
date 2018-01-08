import pyautogui
pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True

from time import sleep

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
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/AddNewAccount.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/Back.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Security Alert
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/SecurityAlert.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/No.png')
	pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
	#waiting for Check Green Light
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/checkGreen.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/Back_Grey_Underline.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Security Alert
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('C:/clickPhish/SecurityAlert_Light.png')
	image = pyautogui.locateOnScreen('C:/clickPhish/No.png')
	pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
	
print('Sleeping for 15 to wait for Outlook')
sleep(15)
#Initial Outlook Setup wait
print('Looking for Outlook setup page...')
setupCheck = None
while setupCheck == None:
	setupCheck = pyautogui.locateOnScreen('C:/clickPhish/outlookSetup.png')

print('Outlook setup located. Waiting for autopopulation to complete...')
sleep(5)
pyautogui.click(pyautogui.center(setupCheck))
setupOutlook()
