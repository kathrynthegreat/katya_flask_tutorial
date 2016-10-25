#-------------------------
PART TWO: AnotherFormcopy
#-------------------------

This is yet another Flask tutorial in the world, but...I don't jump from hello world to deployment. My aim was to explain the hidden brain of flask a bit more pedantically for newbies and none software developers. 

This code belongs to the the tutorial katya_flask_tutorial https://github.com/kathrynthegreat/katya_flask_tutorial
Part Two uses: https://github.com/kathrynthegreat/AnotherFormcopy

In this section we will get you the minimum viable solution for a flask app that has a front end where you can upload files (csv or pictures) and have them stored in a postgres database. In the next section we will deploy this app to heroku. 


#Here's what our new file structure looks like:

```
AnotherFormcopy.
├── .gitignore              # So that we don't commit compiled files or our environment passwords
├── README.md               # This will be how to test/run the app & have basic info
├── requirements.txt        # These are the dependencies that you need to install for the app to run
├── run.py  				# Runs the app!
├── test.csv                # sample csv to load
├──  Form/           # Everything our app includes is inside this folder
│   ├──  __init__.py        # App-wide setup. Called by `run.py`
│   ├──  config.py          # Configuration Files. i.e. Login related things
│   ├──  views.py           # All the view routes
│   ├──  database_helper.py # All the view routes
│   ├──  setup.py           # Folder for any data we might want to use
│   ├──  templates/         # HTML files go here
│   │   ├──  index.html     # JavaScript & HTML
```

Read about going from module to a package: http://flask.pocoo.org/docs/0.11/patterns/packages/# AnotherFormcopy