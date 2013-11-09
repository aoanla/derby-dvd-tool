
import string,subprocess
#Fade in and out of images in filenames in lst
# We expect: awards720.png = an Awards title page 720x576
#			 black720.png = a black page 720x576
#			 x.png files for people
#			 x-names.png files for people+names
suffs = ["BJ.png","BB.png","MVP.png"]
prefs = ["Jakey","Barrow"]
lst = [ ''.join([ps,ss]) for ss in suffs for ps in prefs]
#lst=["DRGBJ.png","NRGBJ.png","DRGBB.png","NRGBB.png","DRGMVP.png","NRGMVP.png"]
ii = 0
def strc(i):
	return '{0:03}'.format(i)

for i in range(0,25):
	ii += 1
	v1 = int((i/24.0)*100)
	command = "convert black720.png awards.png -compose blend -define compose:args="+str(v1)+"% -composite -type TrueColorMatte -define png:color-type=2 output"+strc(ii)+".png"
	subprocess.call(command,shell=True)
#hold for 2 secs
for i in range(0,48):
	command = "cp output"+strc(ii)+".png output"+strc(ii+1)+".png"
	subprocess.call(command,shell=True)
	ii += 1
for i in range(24,-1,-1):
	ii += 1
	v1 = int((i/24.0)*100)
	command = "convert black720.png awards.png -compose blend -define compose:args="+str(v1)+"% -composite -type TrueColorMatte -define png:color-type=2 output"+strc(ii)+".png"
	subprocess.call(command,shell=True)	
for s in lst:
	ss = s.split('.')
	sn = ss[0]+'-name.'+ss[1]
	#fade in image
	for i in range(24,-1,-1):
		ii += 1
		v1 = int((i/24.0)*100)
		command = "convert "+s+" black720.png -compose blend -define compose:args="+str(v1)+"% -composite -type TrueColorMatte -define png:color-type=2 output"+strc(ii)+".png"
		subprocess.call(command,shell=True)
	#fade in name
	for i in range(0,25):
		ii += 1
		v1 = int((i/24.0)*100) 
		command = "convert "+s+" "+sn+" -compose blend -define compose:args="+str(v1)+"% -composite -type TrueColorMatte -define png:color-type=2 output"+strc(ii)+".png"
		subprocess.call(command,shell=True)
	#hold for 2 secs
	for i in range(0,48):
		command = "cp output"+str(ii)+".png output"+strc(ii+1)+".png"
		subprocess.call(command,shell=True)
		ii += 1
	#fade out name
	for i in range(24,-1,-1):
		ii += 1
		v1 = int((i/24.0)*100) 
		command = "convert "+s+" "+sn+" -compose blend -define compose:args="+str(v1)+"% -composite -type TrueColorMatte -define png:color-type=2 output"+strc(ii)+".png"
		subprocess.call(command,shell=True)
	#fade out image
	for i in range(1,25):
		ii += 1
		v1 = int((i/24.0)*100)
		command = "convert "+s+" black720.png -compose blend -define compose:args="+str(v1)+"% -composite -type TrueColorMatte -define png:color-type=2 output"+strc(ii)+".png"
		subprocess.call(command,shell=True)

#and ffmpeg (or avconv in newer releases) it into a dvd-suitable movie file (supply silence.mp3)
subprocess.call("ffmpeg -shortest -i silence.mp3 -i output%03d.png -target pal-dvd -aspect 4:3 awards.mpg", shell=True)

#btw, the way to get high quality output from cinelerra is to output to high quality Quicktime for Linux, MPEG4 Video, then ffmpeg it to dvd
		
