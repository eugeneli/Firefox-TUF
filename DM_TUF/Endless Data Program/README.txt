The endless data program sends endless data to Firefox when it requests the update.xml file.
Make sure the ip address in firefox for app.update.url.override is set to:
http://127.0.0.1:8080/update/3/%PRODUCT%/%VERSION%/%BUILD_ID%/%BUILD_TARGET%/%LOCALE%/%CHANNEL%/%OS_VERSION%/%DISTRIBUTION%/%DISTRIBUTION_VERSION%/update.xml

and start the program by entering:
python svr-endless.py

Then go to update Firefox in the usual way with the help / about Firefox menu.
Using program manager, you will see that Firefox is continually eating up memory.

