from tuf.libtuf import *

generate_and_write_rsa_keypair("keystore/root_key", bits=2048, password="asd123")
generate_and_write_rsa_keypair("keystore/root_key2", bits=2048, password="asd123")
