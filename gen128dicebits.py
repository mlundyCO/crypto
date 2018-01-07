import pdb
import getpass



def get5rolls():
    while True:
            try:    
                pki = getpass.getpass('5 rolls :')
                if len(pki) == 5:
                    int(pki,6)
                    break
                else:
                    print 'Incorrect number of rolls'
            except ValueError:
                print 'Dat shit aint base 6 bro'
    return pki

def get4rolls():
    while True:
        try:
            pki = getpass.getpass('ONLY 4 ROLLS THIS TIME!!! ')
            if len(pki) == 4:
                int(pki,6)
                break
            else:
                print 'Incorrect number of rolls'
        except ValueError:
            print 'Dat shit aint base 6 bro'
    return pki

def get50rolls():
    base6bits = ''
    for i in range(0,10):
        base6bits += get5rolls()
    return base6bits

def convertToHex(base6bits):
    HexBits = hex(int(base6bits,6))[2:-1]
    if len(HexBits) == 32:
        return HexBits
    else:
        print 'Not enough entropy'



if __name__ == '__main__':
    #base6bits = '12345123451234512345123451234512345123451234512345'
    base6bits = get50rolls()
    hexBits = convertToHex(base6bits)
    print hexBits
    print
    pdb.set_trace()
