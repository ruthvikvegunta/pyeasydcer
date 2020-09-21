# pyeasydcer
Python Script which makes exporting Drupal default content in Drupal a lot easier than manually doing it

##### Work Done
+ Complete support for DCER - Script can export any number of entities in just a matter of minutes
+ Works perfectly on unix systems
+ Supports Lando (lando users need to add lando parameter when running the script so as to enable lando mode)

##### Work to be done
+ Windows support
+ Multithreading support to make the execution time more faster

##### Perks
+ User can export any number of entities in one go
+ User need not enter subscription name and path where local setup is located every time they export defult content
+ Script asks the user to enter config when they run it for the first time
    + For the next 6 hours script will not ask user to input subscription or path making user's work a bit more easy
+ And the best part is there is no need for the user to enter arguments in a particular order, user can enter arguments in any order the script will take care of the problem of handling all that stuff.

#### Requirements
+ Python v3.7+
+ pip3

#### Usage:
  + `pyeasydcer <entity_type> <id's of entities separated by a comma(,)`
  + `pyeasydcer <entity_type> <id's of entities separated by a comma(,) lando` (if using lando enviroment)
  + Refer to `pyeasydcer -help` to see the help section whenever you are confused


#### HOW TO USE THIS SCRIPT

+ You can directly install this script from pip as given below

  + `pip3 install pyeasydcer`

+ If you are cloning the repository, then you need to run it as given below.

  + > cd pyeasydcer/easydcer
  + > python3 __main__.py --help

###### Python is the FUTURE
###### Enjoy Scripting 🙂
