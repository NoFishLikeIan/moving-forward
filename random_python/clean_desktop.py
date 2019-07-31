import os, glob

for n,filename in enumerate(glob.glob("Desktop/Screen*")):
    print(f'Cleaning {filename} ({n+1} out of {len(filename)})')
    os.remove(filename)

print(glob.glob('Desktop/Screen*'))