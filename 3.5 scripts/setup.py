from tuf.libtuf import *
import datetime
import distutils.core

pwdCount = 0
#Open settings file to get paths for all passwords
f = open("settings.txt")
settings = f.readlines()
f.close()

for line in settings:
	kvPair = line.split("=", 1)
	if kvPair[0] == "RootPassword1":
		rootPassword = kvPair[1]
		pwdCount = pwdCount + 1
	elif kvPair[0] == "RootPassword2":
		rootPassword2 = kvPair[1]
		pwdCount = pwdCount + 1
	elif kvPair[0] == "TargetsPassword":
		targetsPassword = kvPair[1]
		pwdCount = pwdCount + 1
	elif kvPair[0] == "ReleasePassword":
		releasePassword = kvPair[1]
		pwdCount = pwdCount + 1
	elif kvPair[0] == "TimestampPassword":
		timestampPassword = kvPair[1]
		pwdCount = pwdCount + 1
	elif kvPair[0] == "NightlyPassword":
		nightlyPassword = kvPair[1]
		pwdCount = pwdCount + 1

if pwdCount != 6:
	raise Exception("Not enough passwords supplied")

#Generate root keys
generate_and_write_rsa_keypair("keystore/root_key", bits=2048, password=rootPassword)
generate_and_write_rsa_keypair("keystore/root_key2", bits=2048, password=rootPassword2)

public_root_key = import_rsa_publickey_from_file("keystore/root_key.pub")
public_root_key2 = import_rsa_publickey_from_file("keystore/root_key2.pub")

repository = create_new_repository("repository/")
repository.root.add_key(public_root_key)
repository.root.add_key(public_root_key2)

repository.root.threshold = 2

private_root_key = import_rsa_privatekey_from_file("keystore/root_key", password=rootPassword)
private_root_key2 = import_rsa_privatekey_from_file("keystore/root_key2", password=rootPassword2)

repository.root.load_signing_key(private_root_key)
repository.root.load_signing_key(private_root_key2)
repository.status()

generate_and_write_rsa_keypair("keystore/targets/targets_key", password=targetsPassword)
generate_and_write_rsa_keypair("keystore/release/release_key", password=releasePassword)
generate_and_write_rsa_keypair("keystore/timestamp/timestamp_key", password=timestampPassword)

repository.targets.add_key(import_rsa_publickey_from_file("keystore/targets/targets_key.pub"))
repository.release.add_key(import_rsa_publickey_from_file("keystore/release/release_key.pub"))
repository.timestamp.add_key(import_rsa_publickey_from_file("keystore/timestamp/timestamp_key.pub"))

private_targets_key = import_rsa_privatekey_from_file("keystore/targets/targets_key", password=targetsPassword)
private_release_key = import_rsa_privatekey_from_file("keystore/release/release_key", password=releasePassword)
private_timestamp_key = import_rsa_privatekey_from_file("keystore/timestamp/timestamp_key", password=timestampPassword)

repository.targets.load_signing_key(private_targets_key)
repository.release.load_signing_key(private_release_key)
repository.timestamp.load_signing_key(private_timestamp_key)

#Expiration = 6 weeks from now
#expirationDate = datetime.datetime.now() + datetime.timedelta(days=42)
#repository.timestamp.expiration = expirationDate.strftime("%Y-%m-%d %H:%M:%S")

repository.write()

#Add and delegate targets
release_targets = repository.get_filepaths_in_directory("repository/targets/update/",recursive_walk=True, followlinks=True)
repository.targets.add_targets(release_targets)
beta_targets = repository.get_filepaths_in_directory("repository/targets/pub/mozilla.org/firefox/releases/",recursive_walk=True, followlinks=True)
repository.targets.add_targets(beta_targets)

nightlyPassword = raw_input("Enter the NIGHTLY password: ")

generate_and_write_rsa_keypair("keystore/nightly/nightly_key", bits=2048, password=nightlyPassword)
public_nightly_key = import_rsa_publickey_from_file("keystore/nightly/nightly_key.pub")

repository.targets.delegate("nightly", [public_nightly_key], [], 1, ["repository/targets/pub/mozilla.org/firefox/releases/"])

private_nightly_key = import_rsa_privatekey_from_file("keystore/nightly/nightly_key", password=nightlyPassword)
repository.targets.nightly.load_signing_key(private_nightly_key)

nightly_targets = repository.get_filepaths_in_directory("repository/targets/pub/mozilla.org/firefox/nightly/",recursive_walk=True, followlinks=True) 
repository.targets.nightly.add_targets(nightly_targets)

private_targets_key = import_rsa_privatekey_from_file("keystore/targets/targets_key", password=targetsPassword)
repository.targets.load_signing_key(private_targets_key)

private_root_key =  import_rsa_privatekey_from_file("keystore/root_key", password=rootPassword)
private_root_key2 =  import_rsa_privatekey_from_file("keystore/root_key2", password=rootPassword2)
private_release_key =  import_rsa_privatekey_from_file("keystore/release/release_key", password=releasePassword)
private_timestamp_key =  import_rsa_privatekey_from_file("keystore/timestamp/timestamp_key", password=timestampPassword)

repository.root.load_signing_key(private_root_key)
repository.root.load_signing_key(private_root_key2)
repository.release.load_signing_key(private_release_key)
repository.timestamp.load_signing_key(private_timestamp_key)

# Generate new versions of all the top-level metadata and increment version numbers.
repository.write()

# copy subdirectory example
stagedMetadata = "repository/metadata.staged"
metadata = "repository/metadata"
distutils.dir_util.copy_tree(stagedMetadata, metadata)

#create client
create_tuf_client_directory("repository/", "client/")