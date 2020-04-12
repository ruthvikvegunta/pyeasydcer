import sys
import shutil
import os

def checkForPython():
    if sys.version_info.major == 3:
        return True
    else:
        return False

def checkForLando():
    lando_location = shutil.which('lando')
    if lando_location is not None:
        return True
    else:
        return False

def checkForDrush():
    drush_location = shutil.which('drush')
    if drush_location is not None:
        return True
    else:
        return False

def basicChecks():
    print ('\nDoing Initial checks\n')
    python_check = checkForPython()
    print ('OS Type : ' + sys.platform)
    print ('Python3 Check : ' + str(python_check))
    if 'lando' in sys.argv:
        drush_check = checkForLando()
        print ('Lando Check : ' + str(drush_check))
    else:
        drush_check = checkForDrush()
        print ('Drush Check : ' + str(drush_check))
    
    if python_check and drush_check:
        return True
    else:
        return False
    
def rootCheck(path, subscription):
    destinationPath = path + subscription + '/app/profiles/' + subscription + '_profile/content'
    if os.path.isdir(path + subscription):
        if os.path.isdir(destinationPath):
            pass
        else:
            os.mkdir(destinationPath)
        return True
    else:
        return False
