

import json 
import pypot.robot
import time
import pypot.primitive
import contextlib

config_file = 'config2.json'

with open(config_file) as f:
	robot_config = json.load(f)
print ('#####_____Configuration chargee_____#####')
test_robot = pypot.robot.from_json('config2.json')
print ('#####_____Synchronisation en cours ..._____#####')
time.sleep(3)
test_robot.start_sync()
print ('#####_____Synchronisation effectuee !_____#####')

for m in test_robot.motors:
	m.compliant = False
	m.goal_speed = 70; #vitesse globale des moteurs
	m.goal_position = 0 # initialisation des moteurs a 0
	print m 
	print m.present_position
#____________________Sequence de test 


test_robot.close()
