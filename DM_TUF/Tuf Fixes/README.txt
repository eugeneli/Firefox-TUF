The problem we were having is that the tuf tools were updated and the updates were conflicting with what we
need to have in the updater.py files in the tuf client directory and interposition directory.

We all first need to update tuf tools on our machines.  To do this, use:

pip install --upgrade https://github.com/theupdateframework/tuf/archive/repository-tools.zip

Then we need to replace the updater.py files in the tuf/client and tuf/interposition directories.  Delete both
the updater.py and updater.pyc files in each of these directories.  Then copy the attached files into the
appropriate directory.  The directory names of the files that I have provided indicate where the files should go.

Use the client directory provided herein for your metatdata.  It was generated using the new scripts.

I have also included svr.py for you.  It works fine.  just start it by entering python svr.py

