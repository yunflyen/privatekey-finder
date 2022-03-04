


from ecdsa import SigningKey, SECP256k1
import sha3, random, binascii

#private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
def generate_address_from_privatekey(private_key):
        private_key = bytes(private_key, 'utf-8')
        private_key = binascii.unhexlify(private_key)
        priv = SigningKey.from_string(private_key, curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak = sha3.keccak_256()
        keccak.update(pub)
        address = keccak.hexdigest()[24:]
        return address;

private_key = '0000000000000000000000000000000000000000000000000000000000000001'
address=generate_address_from_privatekey(private_key)
print(address, private_key)

