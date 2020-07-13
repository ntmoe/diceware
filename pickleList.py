import pickle

#f = open('eff_large_wordlist.txt', 'r')
f = open('original_wordlist.txt', 'r')

rolldict = {}

for line in f:
    linelist = line.replace('\n','').split('\t')
    rollnum = linelist[0]
    word = linelist[1]
    rolldict[rollnum] = word

f.close

g = open('dicewarePickle.txt', 'wb')

pickle.dump(rolldict, g)

g.close
