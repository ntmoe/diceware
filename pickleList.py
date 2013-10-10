import pickle

f = open('diceware.txt', 'r')

rolldict = {}

for line in f:
    linelist = line.replace('\n','').split('\t')
    rollnum = linelist[0]
    word = linelist[1]
    rolldict[rollnum] = word

f.close

g = open('dicewarePickle.txt', 'w')

pickle.dump(rolldict, g)

g.close
