import os.path
HOST = "45.156.26.185"

def setup():
    # checking the environment is prod. or local machine
    is_localhost = os.path.isfile( '.localhost' )
    if is_localhost: HOST = "localhost"


if __name__ == '__main__':
    setup()