#this may show errors in python3, change accordingly
from twython import Twython
from twython import TwythonStreamer
import time
import RPi.GPIO as GPIO
class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			a1=data['text']
			a=a1.lower()
			username=data['user']['screen_name']
			id=data['id']
			#print(a)
			#print(username)
			#print(id)
			st.create_favorite(id=id)
			if (a.find('led1')!=-1):
				if (a.find('on')!=-1):
					GPIO.output(11,GPIO.HIGH)
					print("LED - 1 has been turned on")
					st.update_status(status='LED-1 has been turned on @'+username, in_reply_to_status_id=id)
	  		      	elif (a.find('off')!=-1):
        		    		GPIO.output(11,GPIO.LOW)
					print("LED - 1 has been turned off")
					st.update_status(status='LED-1 has been turned off @'+username, in_reply_to_status_id=id)
			elif (a.find('led2')!=-1):
					ind=a.find('led2')
					timeb=a[ind+5:ind+9]
					try:
						timeb=float(timeb)
					except:
						timeb=100
					print('Blink duration'),
					print(timeb/1000),
					print('sec')
					for i in range(20):
						GPIO.output(13,GPIO.HIGH)
						time.sleep(timeb/1000)
						GPIO.output(13,GPIO.LOW)
						time.sleep(timeb/1000)
					st.update_status(status='LED-2 has been blinked succesfully @'+username, in_reply_to_status_id=id)
			elif(a.find('help')!=-1):
					st.update_status(status='Input in format- \n LED1 *on/off* \n LED2 *time in milliseconds 0-9999* \n LED3 *intensity 0-100* @'+username, in_reply_to_status_id=id)
					print("Input in format- \n LED1 *on/off* \n LED2 *time in milliseconds 0-9999* \n LED3 *intensity 0-100*") 
			elif(a.find('led3')!=-1):
					ind=a.find('led3')
					per=a[ind+5:ind+7]
					try:
						per=float(per)
					except:
						per=50
					print('LED-3 Intesity percentage'),
					print(per),
					print('%')
					pwm.ChangeDutyCycle(per)
					st.update_status(status='LED-3 has been turned on succesfully with given percentage @'+username, in_reply_to_status_id=id)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
api_k='##########'	#this is private key
api_secret_k='##########'
access_t='##########'
access_secret_t='##########'
api=MyStreamer(api_k,api_secret_k,access_t,access_secret_t)
st=Twython(api_k,api_secret_k,access_t,access_secret_t)

GPIO.output(12,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(11,GPIO.LOW)

GPIO.output(12,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
GPIO.output(11,GPIO.HIGH)
time.sleep(0.5)

GPIO.output(12,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(11,GPIO.LOW)

pwm=GPIO.PWM(12,1000)
pwm.start(0)
keyword=raw_input("Enter keyword to track: ")
api.statuses.filter(track=keyword)
