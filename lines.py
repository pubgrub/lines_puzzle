import copy
# acc photo, from upper left to right, then next line
# each piece starting from top side left point, then clockwise

#pieces as seen on orig photo
pieces_orig = [ [3,5],
           [4,6],
           [0,3,5,7],
           [5,6],
           
           [0,3],
           [1,4,5,6],
           [1,2],
           [0,1,4,6],
           
           [],
           [0,1,2],
           [2,4,5,7],
           [1,4,5,7],

           [],
           [],
           [0,1,2,3],
           [0,1,6,7]
          ]

# populate rotations
pieces = []
for i, p in enumerate( pieces_orig):
  pieces.append([p])
  p_temp = p.copy()
  for r in range( 0,3):
    for j,entry in enumerate(p_temp):
      entry += 2
      if entry > 7:
        entry -= 8
      p_temp[j] = entry
    if p_temp not in pieces[i]:
      pieces[i].append(p_temp.copy())
for p in pieces:
  print( p)
#exit()
connections = [ [((1,1),(2,1))]
                #toDo
    ]

def solve( board, rot):
  piece_x = len(board) % 4
  piece_y = int(len(board) / 4) 
  
  for p_i, p in enumerate( pieces):
    if p_i in board:
      continue
    for r_i, r in enumerate( p):

      # check if possible
      if piece_x == 0:
        # leftmost
        if 6 in r or 7 in r:
          continue
      else:
        # has left neighbor
        if 6 in r and not 3 in pieces[board[-1]][rot[-1]]:
          continue
        if 7 in r and not 2 in pieces[board[-1]][rot[-1]]:
          continue
        
      if piece_x == 3:
        #rightmost
        if 2 in r or 3 in r:
          continue

      if piece_y == 0:
        # topmost
        if 0 in r or 1 in r:
          continue
      else:
        if 0 in r and not 5 in pieces[board[-4]][rot[-4]]:
          continue
        if 1 in r and not 4 in pieces[board[-4]][rot[-4]]:
          continue
      
      if piece_y == 3:
        # downmost
        if 4 in r or 5 in r:
          continue

      global cnt 
      cnt += 1
      if cnt % 10000 == 0:
        print( len(board), board, rot)
      if len(board) == 16:
        print('*****')
        print( board, rot)
        exit()     
#      solve( copy.deepcopy(board), copy.deepcopy(rot))
      
      solve( board + [p_i], rot + [r_i])

board = [] # first array: pieces laid, second:  rotation: 0 - 3
rot = []

cnt = 0
solve(board, rot)
