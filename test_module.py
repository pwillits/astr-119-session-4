def hello_world():
	print("Hello world, we made a module!")
	
#in another script you would import test_module (without the .py) 
#you would then call the functions you defined in your module one by one
#example (in a new script)

import test_module as tm 	#imports this module and all the functions it contains

tm.hello_world()			#runs a function included in the module