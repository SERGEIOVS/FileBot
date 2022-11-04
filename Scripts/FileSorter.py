import os,shutil,sys

mydir = os.listdir('My1/')

mydir0 =os.path.basename(mydir[0])

run = True

while run:
    
            menupointslist = [

' - Создать  папку / несколько папок' ,

' - Выбрать нужную папку' ,

' - Удалить нужную папку / несколько папок' ,

' - Переименовать нужную папку / несколько папок' ,

' - Создать файл / несколько файлов' ,

' - Показать содержимое  нужной папки' ,

' - Показать содержимое нужного файла'
            
            ]

            print()
            print('----')
            print()
            print( 'МЕНЮ' )
            print()
            print('----')

            for i in range( len( menupointslist ) ) :
                
                print( i + 1 , menupointslist[i]  )
            
                print()

            print('----')

            print()

            directory = input('directory : ')

            print()

            print('Elements : ' , len(directory))

            print()

            print('mydir  =  '  , mydir)

            print()

            print()

            print('----------------------------------------------------------------------------------------------------------')

            """            name = input('name : ')

                        obj = open(str(directory) + name)

                        new_name = input('new  name : ')

                        directory = input('new  directory : ')

                        obj.save(str(directory) + new_name )"""


















