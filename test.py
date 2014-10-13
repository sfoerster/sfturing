from sfturing import sfturing

#Test Run will test your machine on this input.
#test_tape = ['0','1','#','1','0','1','0']
test_tape = ['1','1','0','1','#','0','0','0','1','0','0','0','0','0','0','0','1','1','1','1','0','1','1','0']

#Specify the Multitape machine here
q_0 = 0
q_a = 10
q_r = 11

delta = {}
# Copy the first substring to the second tape

# write a blank at the beginning of the second tape
delta[(0,'0','b')] = (1,'0','b','S','R')
delta[(0,'1','b')] = (1,'1','b','S','R')
delta[(0,'b','b')] = (11,'#','b','R','R') # no hash --> reject

# Copy the 1st onto the 2nd tape
delta[(1,'0','b')] = (1,'0','0','R','R')
delta[(1,'1','b')] = (1,'1','1','R','R')
delta[(1,'#','b')] = (2,'#','b','S','L') # first tape head stays over #, begin rewinding 2nd
delta[(1,'b','b')] = (11,'#','b','S','L') # no hash --> reject

# Rewind 2nd tape
delta[(2,'#','0')] = (2,'#','0','S','L')
delta[(2,'#','1')] = (2,'#','1','S','L')
delta[(2,'#','b')] = (3,'#','b','R','R') # move first head over first number of compare string, second head over first of copied first string

# begin looking for match between heads
delta[(3,'0','0')] = (3,'0','0','R','R') # match!
delta[(3,'1','1')] = (3,'1','1','R','R') # match!

delta[(3,'1','0')] = (5,'1','0','L','L') # mismatch - rewind 2nd tape (we don't know what's under 1st head)!
delta[(3,'0','1')] = (5,'0','1','L','L') # mismatch - rewind 2nd tape!

delta[(3,'b','0')] = (11,'b','0','S','S') # blank under first, still characters to match... reject
delta[(3,'b','1')] = (11,'b','1','S','S')

delta[(3,'1','b')] = (10,'1','b','S','S') # ACCEPT conditions: run out of 2nd string, still matches
delta[(3,'0','b')] = (10,'0','b','S','S') 
delta[(3,'b','b')] = (10,'b','b','S','S') # or both end at same time, still matching

# rewind 2nd tape, don't know what's under first head
delta[(5,'0','0')] = (5,'0','0','L','L')
delta[(5,'0','1')] = (5,'0','1','L','L')
delta[(5,'1','0')] = (5,'1','0','L','L')
delta[(5,'1','1')] = (5,'1','1','L','L')
delta[(5,'#','0')] = (5,'#','0','L','L')
delta[(5,'#','1')] = (5,'#','1','L','L')
delta[(5,'0','b')] = (6,'0','b','R','R')
delta[(5,'1','b')] = (6,'1','b','R','R')
delta[(5,'#','b')] = (6,'#','b','R','R')

# if heads match, send to state 3
# if mismatch, increment first head, send to state 3
delta[(6,'0','0')] = (3,'0','0','R','S')
delta[(6,'1','1')] = (3,'1','1','R','S')
delta[(6,'0','1')] = (3,'0','1','R','S')
delta[(6,'1','0')] = (3,'1','0','R','S')

test = sfturing(q_0,q_a,q_r,delta,test_tape,single_tape=True)
test.run()

test_tape = ['0','0','1', '0', '1', '1']

#Specify your turing machine here
q_0 = 0
q_a = 2
q_r = 1

delta = {}
delta[(0,'0')] = (10,'b','R') # found 0, look for 1
delta[(0,'1')] = (11,'b','R') # found 1, look for 0
delta[(0,'x')] = (0,'x','R') # keep moving
delta[(0,'b')] = (2,'b','R') # ACCEPT!

delta[(10,'0')] = (10,'0','R')
delta[(10,'x')] = (10,'x','R')
delta[(10,'b')] = (1,'b','R') # reject
delta[(10,'1')] = (20,'x','L') # found matching 1, x it out, rewind back to blank

delta[(11,'1')] = (11,'1','R')
delta[(11,'x')] = (11,'x','R')
delta[(11,'b')] = (1,'b','R') # reject
delta[(11,'0')] = (20,'x','L') # found matching 0, x it out, rewind back to blank

delta[(20,'0')] = (20,'0','L')
delta[(20,'1')] = (20,'1','L')
delta[(20,'x')] = (20,'x','L')
delta[(20,'b')] = (0,'x','R')

test2 = sfturing(q_0,q_a,q_r,delta,test_tape)
test2.run()




test_tape = ['0','1','#','1','0','1','0']
#test_tape = ['1','1','0','1','#','0','0','0','1','0','0','0','0','0','0','0','1','1','1','0','1','1','1','0']

#Specify the Multitape machine here
q_0 = 0
q_a = 10
q_r = 11

delta = {}
# Copy the first substring to the second tape

# write a blank at the beginning of the second tape
delta[(0,'0','b')] = (1,'0','b','S','R')
delta[(0,'1','b')] = (1,'1','b','S','R')
delta[(0,'b','b')] = (11,'#','b','R','R') # no hash --> reject

# Copy the 1st onto the 2nd tape
delta[(1,'0','b')] = (1,'0','0','R','R')
delta[(1,'1','b')] = (1,'1','1','R','R')
delta[(1,'#','b')] = (2,'#','b','S','L') # first tape head stays over #, begin rewinding 2nd
delta[(1,'b','b')] = (11,'#','b','S','L') # no hash --> reject

# Rewind 2nd tape
delta[(2,'#','0')] = (2,'#','0','S','L')
delta[(2,'#','1')] = (2,'#','1','S','L')
delta[(2,'#','b')] = (3,'#','b','R','R') # move first head over first number of compare string, second head over first of copied first string

# begin looking for match between heads
delta[(3,'0','0')] = (3,'0','0','R','R') # match!
delta[(3,'1','1')] = (3,'1','1','R','R') # match!

delta[(3,'1','0')] = (5,'1','0','L','L') # mismatch - rewind 2nd tape (we don't know what's under 1st head)!
delta[(3,'0','1')] = (5,'0','1','L','L') # mismatch - rewind 2nd tape!

delta[(3,'b','0')] = (11,'b','0','S','S') # blank under first, still characters to match... reject
delta[(3,'b','1')] = (11,'b','1','S','S')

delta[(3,'1','b')] = (10,'1','b','S','S') # ACCEPT conditions: run out of 2nd string, still matches
delta[(3,'0','b')] = (10,'0','b','S','S') 
delta[(3,'b','b')] = (10,'b','b','S','S') # or both end at same time, still matching

# rewind 2nd tape, don't know what's under first head
delta[(5,'0','0')] = (5,'0','0','L','L')
delta[(5,'0','1')] = (5,'0','1','L','L')
delta[(5,'1','0')] = (5,'1','0','L','L')
delta[(5,'1','1')] = (5,'1','1','L','L')
delta[(5,'#','0')] = (5,'#','0','L','L')
delta[(5,'#','1')] = (5,'#','1','L','L')
delta[(5,'0','b')] = (6,'0','b','R','R')
delta[(5,'1','b')] = (6,'1','b','R','R')
delta[(5,'#','b')] = (6,'#','b','R','R')

# if heads match, send to state 3
# if mismatch, increment first head, send to state 3
delta[(6,'0','0')] = (3,'0','0','R','S')
delta[(6,'1','1')] = (3,'1','1','R','S')
delta[(6,'0','1')] = (3,'0','1','R','S')
delta[(6,'1','0')] = (3,'1','0','R','S')

test3 = sfturing(q_0,q_a,q_r,delta,test_tape)
test3.run()

# test_tape = ['0','1','1','1','&','1','0','1','0','0','0','1','0','c','w','0','1','1']

# #Specify your turing machine here
# from sfturingDeltas import sfturingDeltas

# # q_0 = 0
# # q_a = 10
# # q_r = 20

# # delta = {}
# # #delta[(0,'0')] = (0,'0','R')
# # #delta[(0,'1')] = (1,'1','R')
# # #delta[(1,'0')] = (0,'0','R')
# # #delta[(1,'1')] = (1,'1','R')
# # delta[(0,'0')] = (0,'0','R')
# # delta[(0,'1')] = (0,'1','R')
# # delta[(0,'&')] = (0,'&','R')
# # delta[(0,'c')] = (0,'c','R')
# # delta[(0,'w')] = (0,'w','R')

# # delta[(0,'b')] = (1,'b','L')

# # delta[(1,'0')] = (2,'b','R') # write a 0
# # delta[(1,'1')] = (3,'b','R') # write a 1

# # delta[(2,'b')] = (4,'0','L') # set to state 1 after going left one more
# # delta[(3,'b')] = (4,'1','L') # set to state 1 after going left one more

# # delta[(4,'0')] = (1,'0','L')
# # delta[(4,'1')] = (1,'1','L')
# # delta[(4,'b')] = (1,'b','L')

# # delta[(1,'&')] = (10,'&','S')

# q_0,q_a,q_r,delta = sfturingDeltas.rightShiftParams('&',test_tape)

# test3 = sfturing(q_0,q_a,q_r,delta,test_tape)
# test3.run()