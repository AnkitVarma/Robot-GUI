import logging
import sys
logging.basicConfig(filename='test.txt',level = logging.DEBUG,format='%(message)s')
q = sys.argv[1]
if q == 'f':
    movement = 'forward'
    objectdetection = 'objectnotdetected'
    name = [movement,objectdetection]
    logging.debug(name)
elif q == 'r':
    movement = 'right'
    objectdetection = 'objectnotdetected'
    name = [movement,objectdetection]
    logging.debug(name)
elif q == 'b':
    movement = 'backward'
    objectdetection = 'objectnotdetected'
    name = [movement,objectdetection]
    logging.debug(name)
elif q == 'l':
    movement = 'left'
    objectdetection = 'objectnotdetected'
    name = [movement,objectdetection]
    logging.debug(name)

