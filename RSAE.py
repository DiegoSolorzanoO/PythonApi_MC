import random
import json 

class RSAE():
    def __init__(self):
        super().__init__()


    # Método para checar si el número es primo
    def isPrime(self, x):
        count = 0
        for i in range(int(x/2)):
            if x % (i+1) == 0:
                count = count+1
        return count == 1


    # Método para sacar el máximo común divisor
    def MCD(self, n1, n2):
        r = 0
        while(n2 > 0):
            r = n2
            n2 = n1 % n2
            n1 = r
        return n1


    # Method which returns the public and private keys
    def GenerateKeys(self):
        primes = [i for i in range(100,200) if self.isPrime(i)]
        p = random.choice(primes)
        q = random.choice(primes)
        n = p*q
        fi_n = (p - 1)*(q - 1) 
        '''
        print('p: '+str(p))
        print('q: '+str(q))
        print('n: '+str(n))
        print('Fi_n: '+str(fi_n))
        '''
        public_exp = []
        counter = 0
        for i in range(2,fi_n+1):
            if counter==30:
                break
            if self.MCD(i,fi_n)==1:
                public_exp.append(i)
                counter+=1
        e = random.choice(public_exp)

        # print('e: '+str(e))

        d = 0
        for i in range(1,fi_n+1):
            if ((i*e)%fi_n)==(1%fi_n):
                d = i
                break

        # print('d: '+str(d))

        public_key = [n,e]
        private_key = [n,d]

        # print('Public key: ' + str(public_key))
        # print('Private key: ' + str(private_key))

        return [public_key,private_key]


    def encrypt(self, public_key, message):
        s = message.encode('utf8')
        hexa = s.hex()
        num_message = int(hexa, 16)
        return (num_message**public_key[1])%public_key[0]

    
    def encryptM(self, message, public_key, typeOf = None):
        if typeOf == 'json':
            message = json.dumps(message)
        message_encrypted = []
        for l in message:
            message_encrypted.append(self.encrypt(public_key,l))
        return message_encrypted

    def de_encrypt(self, private_key, message):
        val = (message**private_key[1])%private_key[0]
        return bytes.fromhex(hex(val)[2:]).decode('utf-8')


    def de_encryptM(self, message_encrypted, private_key, typeOf = None):
        final_message = ''
        for data in message_encrypted:
            final_message += str(self.de_encrypt(private_key,data))
        if typeOf == 'json':
            return json.loads(final_message)
        return final_message




'''
datatosend = {
    'Torch' : 'Creates Fire',
    'Knife' : 'Pointy',
    'Rock' : 'Useless Rock',
    'Paper' : 'You can write things here'
}


message = json.dumps(datatosend) 
message_encrypted = []
for l in message:
    message_encrypted.append(encrypt(public_key,l))



print(message_encrypted)



final_message = ''
for data in message_encrypted:
    final_message += str(de_encrypt(private_key,data))

print(json.loads(final_message))
'''