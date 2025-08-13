import shutil
import datetime
import os

def backupFiles(source, destination):
    today = datetime.date.today()
    backupFileName = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backupFileName, 'gztar', source)


source = "../pythonFurtherRevisionAdvanced"
destination = "../backup"

backupFiles(source, destination)