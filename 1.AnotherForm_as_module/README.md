#--------------------
PART One AnotherForm
#--------------------

This is yet another Flask tutorial in the world, but...I don't jump from hello world to deployment. My aim was to explain the hidden brain of flask a bit more pedantically for newbies and none software developers. 

This code belongs to the the tutorial katya_flask_tutorial https://github.com/kathrynthegreat/katya_flask_tutorial
Part One creates yet another Form using: https://github.com/kathrynthegreat/AnotherForm

In this section we will start with an application that is self contained in one app.py file and runs on our local host. In Part two we will break it up from a single module to a pakcage. 


#Here's what our starting file structure looks like:

```
AnotherFormcopy.
├──  Form/           		# Everything our app includes is inside this folder
│   ├──  app.py        		# App-wide setup. Called by `run.py`
│   ├──  templates/         # HTML files go here
│   ├──  requirements.txt   # These are the dependencies that you need to install for the app to run
│   ├──  README.md           # This will be how to test/run the app & have basic info
│   │   ├──  index.html     # JavaScript & HTML
```

Credits: The original code for this application can be found here: http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python" Note that there were bugs in the original code, which I fixed.  

