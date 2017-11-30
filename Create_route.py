import numpy as np
import time




class router:
    current_dir = 0  #0 = up , 1 = down ||, 2 = left , 3 = right
    orientation = 0

    def horizontal_move(direction):

        if(direction == 'left'):
            current_dir = 2
            print 'moving left' + str(current_dir)

            time.sleep(2)
        elif(direction == 'right'):
            current_dir = 3
            print 'moving left' + str(current_dir)


            time.sleep(2)


    def vertical_move(direction):

        if(direction == 'up'):
            print 'moving forward'
            orientation = 0
            time.sleep(1)
        elif(direction == 'down'):
            print 'moving backward'
            time.sleep(1)
            orientation = 1
        elif(direction == 'same'):
            print 'stopping'



    try:
        r = np.load('Route.npy')


        # print r
        # ---- store initial position
        prev_x,prev_y = r[0]
        print prev_x,prev_y
        # ----
        for x,y in r:
            print x
            print y
            if (x > prev_x):
                vertical_move('up')
            elif (x == prev_x):
                vertical_move('same')
            elif(x < prev_x):
                vertical_move('down')
            prev_x = x
            prev_y = y
    except:
        pass
