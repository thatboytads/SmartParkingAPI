from gpiozero import MotionSensor
from gpiozero import LED
import time
from datetime import datetime

class CarSensor:
	def __init__(self):        
		self.cnt1= False
		self.cnt2= False
		self.parked=0

	def motion_detect(self,pir1, pir2,buzz):
		try:
			current_time=[]
			#sensed_time=""
			while True:
				cnt=pir1.motion_detected
				if cnt==True and self.parked==0:
					print("Front wheel has been sensed by 1st")
					print("Waiting for back wheel to be sensed by 1nd")
					time.sleep(2)
					if pir1.wait_for_motion(2):
						print("back wheel sensed by 1st ")
						print("Waiting for the front tip to be sensed by 2nd")
						if pir2.wait_for_motion(2):
							print("tip sensed by 2nd")
							print("Car in")
							buzz.on()
							time.sleep(3)
							buzz.off()
							self.parked=1
							message= "car parked"
							return message
							continue
				#if cnt==True and self.parked==1:
				#	now= datetime.now()
				#	current_time.append(now.strftime("%H:%M:%S"))
				#	sensed_time = ' '.join([str(elem)for elem in current_time])
				#	time.sleep(2)
				#	message= "car parked"
				#	return message, sensed_time
				cnt2=pir2.motion_detected
				if cnt2==True and self.parked==1:
					print("Tip sensed moving back by 2nd")
					print("Waiting for back wheel to be sensed 1st")
					if pir1.wait_for_motion(2):
						print("back wheel been sensed by 1st")
						print("waiting for front wheel to be sensed by 1st")
						time.sleep(2)
						if pir1.wait_for_motion(2):
							print("front wheel sensed by 1st")
							print("car out")
							buzz.on()
							time.sleep(3)
							buzz.off()
							self.parked=0
							message= "car not parked"
							return message
							continue
		except KeyboardInterrupt:
			pass


