import os
import time

print('This is a simple tool to rename multiple files of a folder.')

while (True):
    files = []

    print('Please enter a folder path:')
    folder_path = input('')
    time.sleep(1.5)
    print('Obtaining files...')
    time.sleep(1.5)

    counter = 0
    try:
        for file in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file)):
                print('Obtained file...', file, 'succesfully!')
                time.sleep(0.1)
                files.append(file)



        print('All files obtained!')

        time.sleep(1.5)
        exchange_value = input('Enter re-name value:\n')


        for file_name in files:
            words = file_name.split('_')
            if (len(words) == 4):
                print(words)
                counter =+ 1
                new_name = exchange_value + '_' + words[2] + '.pdf'
                new_path = os.path.join(folder_path, new_name)
                old_path = os.path.join(folder_path, file_name)
                os.rename(old_path, new_path)
                print('Renamed file', file_name, 'into', new_name + '!')


        if (counter >= 1):
            print('All', counter, 'files have been renamed succesfully!')

        else:
            print('No files to rename detected!')

        time.sleep(1.5)
        print('Programm is restarting...')
        time.sleep(1.5)
        os.system('cls')


    except:
        print('Invalid folder path!')
