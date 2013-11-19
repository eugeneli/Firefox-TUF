from tuf.libtuf import *

generate_and_write_rsa_keypair("keystore/root_key", bits=4096, 
				password="cloverfield")

generate_and_write_rsa_keypair("keystore/root_key2")
