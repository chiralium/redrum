import os

HOST = "45.156.26.185"
DIR = os.path.dirname( os.path.abspath( __file__ ) )

def setup():
    global HOST

    # checking the environment is prod. or local machine
    is_localhost = True
    try: open( DIR + '/app.py' );
    except IOError: is_localhost = False

    print (is_localhost)
    if is_localhost: HOST = "localhost"


setup()