# acc photo, from upper left to right, then next line
# each piece starting from top side left point, then clockwise

pieces = [ (0,1,1,0),
           (0,0,2,2),
           (2,1,1,1),
           (0,0,1,2),
           
           (2,1,0,0),
           (1,0,3,2),
           (1,2,0,0),
           (3,0,2,2),
           
           (0,0,0,0),
           (3,2,0,0),
           (0,2,3,1),
           (1,0,3,1),

           (0,0,0,0),
           (0,0,0,0),
           (3,3,0,0),
           (3,0,0,3)
          ]

connections = [ [((1,1),(2,1))]
                #toDo
    ]

board = [ [],[] ] # first array: pieces laid, second:  rotation: 0 - 3

