from tuf.libtuf import *

repository = load_repository("repository/")
list_of_targets = repository.get_filepaths_in_directory("repository/targets/",recursive_walk=True, followlinks=True)
repository.targets.add_targets(list_of_targets)

private_targets_key = import_rsa_privatekey_from_file("keystore/targets/targets_key")
repository.targets.load_signing_key(private_targets_key)

private_root_key =  import_rsa_privatekey_from_file("keystore/root_key")
private_root_key2 =  import_rsa_privatekey_from_file("keystore/root_key2")
private_release_key =  import_rsa_privatekey_from_file("keystore/release/release_key")
private_timestamp_key =  import_rsa_privatekey_from_file("keystore/timestamp/timestamp_key")

repository.root.load_signing_key(private_root_key)
repository.root.load_signing_key(private_root_key2)
repository.release.load_signing_key(private_release_key)
repository.timestamp.load_signing_key(private_timestamp_key)

# Generate new versions of all the top-level metadata and increment version numbers.
repository.write()