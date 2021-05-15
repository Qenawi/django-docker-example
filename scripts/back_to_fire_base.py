#   Qenawi created back_to_fire_base.py at 5/15/21, 10:34 AM
#   back_to_fire_base.py @Docs
#

import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

latest_backup = ""


# send backup file to firebase storage
def init_admin():
    buckerUrl = "databasebackup-461c3.appspot.com"
    cred = credentials.Certificate("scripts/accountKey.json")
    firebase_admin.initialize_app(cred, {'storageBucket': buckerUrl})


def get_latest_database_dumb():
    global latest_backup
    path = "my/backup/dir"
    filepath = [os.path.join(path, file) for file in os.listdir(path)]
    ls = sorted(filepath)
    latest_backup = ls[-1]


def upload_to_fire_base():
    global latest_backup
    file = latest_backup
    bucket = storage.bucket()
    blob = bucket.blob(blob_name="backup.dumb")
    fi = open(file, "rb")
    rep = blob.upload_from_file(file_obj=fi)
    print(rep)


# download backup file from database
def restore_backup():
    bucket = storage.bucket()
    blob = bucket.blob(blob_name="data.dumb")
    blob.download_to_filename("my/backup/dir/backup.dumb")
    print("--------- backup restored ----------")


if __name__ == '__main__':
    print("--------- connecting to backup server ----------")
    init_admin()
    get_latest_database_dumb()
    restore_backup()
