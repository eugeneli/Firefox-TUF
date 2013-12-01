from tuf.libtuf import *

repository = load_repository("repository/")

private_nightly_key = import_rsa_privatekey_from_file("keystore/nightly/nightly_key", password="asd123")
repository.targets.nightly.load_signing_key(private_nightly_key)

nightly_targets = repository.get_filepaths_in_directory("repository/targets/pub/mozilla.org/firefox/nightly/",recursive_walk=True, followlinks=True) 
repository.targets.nightly.add_targets(nightly_targets)

repository.write()

# copy subdirectory example
stagedMetadata = "repository/metadata.staged"
metadata = "repository/metadata"
distutils.dir_util.copy_tree(stagedMetadata, metadata)