import sys
import os

if len(sys.argv) < 2:
    sys.exit('Please specify the Mode')

mode = sys.argv[1]
delete = True if len(sys.argv) < 3 else sys.argv[2]
bufsize = 420 if len(sys.argv) < 4 else sys.argv[3]
cap = 0 if len(sys.argv) < 5 else sys.argv[4]

currentPath = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(currentPath):
    if '.py' in file or not os.path.isfile(os.path.join(currentPath, file)):
        continue

    with open(os.path.join(currentPath, file), 'rb') as in_file:
        
        if mode == 'single':

            for i in range(bufsize):
                in_file.seek(i)
                byte = in_file.read(5)

                if byte == b'Unity':
                    pos = in_file.tell() - 5
                    break

        elif mode == 'double':

            secondPass = False
            for i in range(bufsize):
                in_file.seek(i)
                byte = in_file.read(5)

                if byte == b'Unity':
                    if not secondPass:
                        secondPass = True
                    else:
                        pos = in_file.tell() - 5
                        break

        else:
            sys.exit('Mode = single | double')

        if not cap == 0:
            output = os.path.join(currentPath, file[:cap])
        else:
            output = os.path.join(currentPath, file) + '_edited'

        with open(output, 'wb+') as out_file:
            in_file.seek(0)
            out_file.write(in_file.read()[pos:])
        out_file.close()
        
    in_file.close()
    if delete:
        os.remove(file)