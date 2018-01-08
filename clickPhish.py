import pyautogui
pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True

from time import sleep

def setupOutlook():
	#waiting for Back/Next button
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('Back_Grey.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Account Configuration
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('AccountConfig.png')
	image = pyautogui.locateOnScreen('Back.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Add New Account
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('AddNewAccount.png')
	image = pyautogui.locateOnScreen('Back.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Security Alert
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('SecurityAlert.png')
	image = pyautogui.locateOnScreen('No.png')
	pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
	#waiting for Check Green Light
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('checkGreen.png')
	image = pyautogui.locateOnScreen('Back_Grey_Underline.png')
	pyautogui.click(pyautogui.center(image)[0]+75,pyautogui.center(image)[1])
	#waiting for Security Alert
	sleep(3)
	image = None
	while image == None:
		image = pyautogui.locateOnScreen('SecurityAlert_Light.png')
	image = pyautogui.locateOnScreen('No.png')
	pyautogui.click(pyautogui.center(image)[0]-80,pyautogui.center(image)[1])
	

#Initial Outlook Setup wait
setupCheck = None
while setupCheck == None:
	setupCheck = pyautogui.locateOnScreen('outlookSetup.png')

#sleep(10)
pyautogui.click(pyautogui.center(setupCheck))
setupOutlook()