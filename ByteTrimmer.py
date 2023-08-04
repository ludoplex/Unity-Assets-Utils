import os

currentPath = str(input('Path to Assets: '))

for FILE in os.listdir(currentPath):
    if '.py' in FILE or not os.path.isfile(os.path.join(currentPath, FILE)):
        continue

    with open(os.path.join(currentPath, FILE), 'rb+') as BYTES:
        secondPass = False

        DATA = BYTES.read()

        l = min(len(DATA), 42069)
        pos = 0

        for i in range(l):
            BYTES.seek(i)
            byte = BYTES.read(7)

            if byte == b'UnityFS':
                pos = BYTES.tell() - 7
                if not secondPass:
                    secondPass = True
                else:
                    break

        if pos != 0:
            BYTES.seek(0)
            BYTES.write(DATA[pos:])
            BYTES.truncate()