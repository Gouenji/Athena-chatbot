import aiml
import os
#from flask import render_template,Flask, request
def chatbot():
	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
	    print (kernel.respond(input("--> ")))


if __name__ == '__main__':
    c=input("Remove brn: ").lower()
    if 'y' in c:
        os.remove("bot_brain.brn")

    chatbot()
