import os

HOST = "45.156.26.185"
DIR = os.path.dirname( os.path.abspath( __file__ ) )

def setup():
    global HOST

    # checking the environment is prod. or local machine
    is_localhost = True
    try: open( DIR + '/.localhost' );
    except IOError: is_localhost = False

    if is_localhost: HOST = "localhost"


setup()