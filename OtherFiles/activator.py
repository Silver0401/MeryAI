import subprocess
import time
import InitialAI 

if InitialAI.MeryActivated() == "success":
	
	AI = subprocess.call(["python3","{}".format("AI.py")])
	time.sleep(1)
	AI_Animation = subprocess.call(["python3","{}".format("AI_animation.py")])
	
else:
	print ("not ready")


# AI_Initializer = subprocess.call(["python3","{}".format("Initial-AI.py")])

# print (AI_Initializer)

