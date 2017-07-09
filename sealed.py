import requests
import random

r = requests.get('http://yugiohprices.com/api/set_data/Battle%20Pack:%20Epic%20Dawn', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
blah = r.json()
allcards = blah['data']['cards']
'''
cardinfo = allcards[2]
cardname = cardinfo['name']
setstuff = cardinfo['numbers'][0]['print_tag']
setnum = int(setstuff[7:])
print cardname
print setnum
'''

cardlist = [''] * 220
count = 0

while count < 440:
    cardinfo = allcards[count]
    cardname = cardinfo['name']
    setstuff = cardinfo['numbers'][0]['print_tag']
    setnum = int(setstuff[7:])
    cardlist[setnum - 1] = cardname
    count += 2
    
packs = 0

while packs < 10:
    
    pool1 = random.randint(0,54)
    pool2 = random.randint(55,109)
    pool3 = random.randint(110,169)
    pool4 = random.randint(170,219)
    starfoil = random.randint(0,219)
    print cardlist[pool1]
    print cardlist[pool2]
    print cardlist[pool3]
    print cardlist[pool4]
    print cardlist[starfoil]
    packs += 1
