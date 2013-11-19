from tuf.libtuf import *

public_root_key = import_rsa_publickey_from_file("keystore/root_key.pub")
private_root_key = import_rsa_privatekey_from_file("keystore/root_key")

repository = create_new_repository("repository/")
repository.root.add_key(public_root_key)

public_root_key2 = import_rsa_publickey_from_file("keystore/root_key2.pub")
repository.root.add_key(public_root_key2)

repository.root.threshold = 2
private_root_key2 = import_rsa_privatekey_from_file("keystore/root_key2", password="cloverfield")

repository.root.load_signing_key(private_root_key)
repository.root.load_signing_key(private_root_key2)

repository.status()

try:
  repository.write()
except tuf.Error, e:
  print e 

generate_and_write_rsa_keypair("keystore/targets/targets_key", password="cloverfield")
generate_and_write_rsa_keypair("keystore/release/release_key", password="cloverfield")
generate_and_write_rsa_keypair("keystore/timestamp/timestamp_key", password="cloverfield")

repository.targets.add_key(import_rsa_publickey_from_file("keystore/targets/targets_key.pub"))
repository.release.add_key(import_rsa_publickey_from_file("keystore/release/release_key.pub"))
repository.timestamp.add_key(import_rsa_publickey_from_file("keystore/timestamp/timestamp_key.pub"))

private_targets_key = import_rsa_privatekey_from_file("keystore/targets/targets_key")
private_release_key = import_rsa_privatekey_from_file("keystore/release/release_key")
private_timestamp_key = import_rsa_privatekey_from_file("keystore/timestamp/timestamp_key")

repository.targets.load_signing_key(private_targets_key)
repository.release.load_signing_key(private_release_key)
repository.timestamp.load_signing_key(private_timestamp_key)

repository.timestamp.expiration = "2014-10-28 12:08:00"

repository.targets.compressions = ["gz"]
repository.release.compressions = ["gz"]

repository.write()
