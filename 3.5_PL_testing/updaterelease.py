from tuf.libtuf import *
import distutils.core

repository = load_repository("repository/")

targetsPassword = raw_input("Enter TARGETS password: ")
private_targets_key = import_rsa_privatekey_from_file("keystore/targets/targets_key", password=targetsPassword)
repository.targets.load_signing_key(private_targets_key)

#clear current targets
for target in repository.targets.target_files:
	repository.targets.remove_target("repository/targets/"+target)

#Add targets
release_targets = repository.get_filepaths_in_directory("repository/targets/update/",recursive_walk=True, followlinks=True)
repository.targets.add_targets(release_targets)
beta_targets = repository.get_filepaths_in_directory("repository/targets/pub/mozilla.org/firefox/releases/",recursive_walk=True, followlinks=True)
repository.targets.add_targets(beta_targets)

#repository.targets.version = repository.targets.version + 1

repository.write_partial()

# copy subdirectory example
stagedMetadata = "repository/metadata.staged"
metadata = "repository/metadata"
distutils.dir_util.copy_tree(stagedMetadata, metadata)