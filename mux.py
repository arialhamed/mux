import subprocess
import os

candidates = [x for x in os.listdir() if x[len(x)-4:] in ('.mov','.mp4','.m4a','.3gp','.3g2','.mj2','.avi','.mp3','.ogg')]

print()
print('Current items in Directory')

for i in range(len(candidates)):
    print('{}: {}'.format(str(i+1).zfill(3),candidates[i]))

print()
print('Enter number index for video.')
name_vid = candidates[int(input('>>> '))-1]

print()
print('Enter number index for audio.')
name_aud = candidates[int(input('>>> '))-1]

print()
print('Enter name of output video (default ext: mp4).')
out_name = input('>>> ')
cmd = 'ffmpeg -i \"'+name_vid+'\" -i \"'+name_aud+'\" -shortest -c copy \"'+out_name+'.mp4\"'
subprocess.call(cmd, shell=True)

print('Muxing completed!')
