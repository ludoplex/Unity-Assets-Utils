import sys
import os

delete = True if len(sys.argv) < 2 else sys.argv[1]

currentPath = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(currentPath):
    if '.py' in file or not os.path.isfile(os.path.join(currentPath, file)):
        continue

    with open(os.path.join(currentPath, file), 'rb') as in_file:
        secondPass = False

        for i in range(1024):
            in_file.seek(i)
            byte = in_file.read(7)

            if byte == b'UnityFS':
                if not secondPass:
                    pos = in_file.tell() - 7
                    secondPass = True
                else:
                    pos = in_file.tell() - 7
                    break

        output = os.path.join(currentPath, file) + '_edited'

        with open(output, 'wb+') as out_file:
            in_file.seek(0)
            out_file.write(in_file.read()[pos:])
        out_file.close()
        
    in_file.close()
    if delete:
        os.remove(file)