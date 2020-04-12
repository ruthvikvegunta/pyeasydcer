import sys
from easydcer_modules import config, basicChecks, dcer

global subscription, base_path, entity_type


if basicChecks.basicChecks():
    if '-force' in sys.argv:
        pydcerConfig = config.checkConfig('pydcer_settings.json', 'force_change')
        sys.argv.remove('-force')
    else:
        pydcerConfig = config.checkConfig('pydcer_settings.json')
        
    pydcer_saved_config = pydcerConfig.getInfo()
    subscription = pydcer_saved_config['subscription']
    base_path = pydcer_saved_config['path']

    if basicChecks.rootCheck(base_path, subscription):
        arguments_array = sys.argv
        arguments_array.remove('main.py') #remove once pip package is done
        entity_type = ''
        with open('available_entities.txt') as entity:
            available_entities = entity.read().splitlines()
            for entry in available_entities:
                if entry in arguments_array:
                    entity_type = entry
                    arguments_array.remove(entity_type)
                    break
            if not entity_type:
                print('\nWrong entity type detected\n')
                sys.exit(1)

        if 'lando' in arguments_array:
            landoEnv = True
            arguments_array.remove('lando')
        else:
            landoEnv = False
            
        if len(arguments_array) == 1:
            ids_array = arguments_array[0]
        else:
            print('\nWrong input given to the script, Please use -help section\n')
            sys.exit(1)
            
        if landoEnv:
            dcer.dcer(entity_type, ids_array.split(','), subscription, base_path, landoEnv)
        else:
            dcer.dcer(entity_type, ids_array.split(','), subscription, base_path)
    else:
        print('\nLook\'s like Drupal is not properly installed, Cannot find a project with the name: ' + subscription + ' in the mentioned path: ' + base_path)
        sys.exit(1)
else:
    print('\nCannot proceed further because one of the above checks failed\n')
    sys.exit(1)


#pyeasydcer block_content 1,2,3,4,5,6,7,8,9,10