#

###
#
# DVD Chapter & Subtitle Script
#
###
import string, Image, ImageDraw, ImagePalette, ImageFont
import os, sys, codecs, subprocess



#these parts and other bits of code for writing nice subtitle images stolen from aug.ment.org/dvd/makespumux.py
width = 720;
height = 576;
fontsize = 32;
#font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf", fontsize)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", fontsize)
def makeSubImage( filename, t):
	"""make a 3color png for DVD subtitles"""
	#taken from aug.ment.org/dvd/makespumux.py
	im = Image.new('P',(width, height), 2 )
	palette = []
	palette.extend( ( 255,255,255 )  )
	palette.extend( ( 0,0,0 )  )
	im.putpalette(palette)
	draw = ImageDraw.Draw(im);
	
	c = 0;
	splitpnt  = 0;
	max = -1
	lines = [];
	
	while( max < 0 or max > (width - 70) ):
		## we need to find out how many lines to make
		max = -1;
		c = c + 1;
		splitpnt = 0;
		lines = [];
		for i in range(1,c+1):
			lo = splitpnt;
			end = i * ( len(t)/c);
			#print "end = " + str(end);
			splitpnt = t.rfind(' ', 0,  end )
			if (i == c):
				splitpnt = len(t);
			#print str(lo) + ":" + str(splitpnt);
			line = t[lo:splitpnt]
			line = line.lstrip();
			line = line.rstrip();
			lines.append(line) ;
			tmp = draw.textsize( line, font=font);
			if (tmp[0] > max ):
				max = tmp[0];
				#print str(i) + ' = ' + line
				#print "max = " + str(max)
		if (c > 5):
			quit();
		c =0
   for i in lines:
		print i
		tsize = draw.textsize( i, font=font);
		x = (width - tsize[0] ) / 2;
		y = height - (( tsize[1] * (len(lines) - c ) ) + 34);
		c = c +1;
		draw.text( (x +2 ,y +2), i, font=font, fill=1 )
		draw.text( (x,y), i, font=font, fill=0 )
		
	im.save( filename, "PNG", transparency=2)




def AddChapter(ChapterList,Time,Name):
	return ChapterList.append({"T":Time,"N":Name})


def Serialise(ChapterList, baseimg):
	for block of 8 chapters:
		make 3 subpictures (4x2 arrangement) - normal, highlight, select
		make xml for spumux (Button actions are "go to chapter X")
		"<subpictures><stream>\n"
		'<spu force="yes" start="00:00:00:00" image="' + normal + '" select="' + select + '" highlight="' + highlight + '" >' + "\n"
		'<button ...
		"</spu></stream></subpictures>\n"
		and mux
		spumux menuspumux.xml < menubackdrop.mpg > thismenuname.mpg

	output list of chapter times for dvdauthor
	

class JamSubs(object):
	def __init__(self):
		self.


	def AddChange(JamDelta):
		#make change to "core list", and update only the subtitle streams we need to (can we store changes as diffs internally??)
		#Deltas must know, at least, their start and endtime (endtime=nextDelta's starttime). We can also make tests easier by marking them as Scoreline
		and or Jammerline
		#The problem here is that the endtime of a Delta depends on context (Jammer- vs Score- vs JammerScore-lines)		
		
		#we could split the structure into "JammerDelta" and "ScoreDelta" parts (of a single struct) then each can have an endtime (and we pick the soonest
		#for the JammerScore endtime, of course - or we defer outputting a JammerScore until the *next* Delta, since its starttime must be our endtime!


	def AddSpumuxxml(spumuxxml, starttime, endtime, outname, NeutralColour, Team1Colour, Team2Colour):
		#Add a subpicture's xml to the provided spumuxxml stream, with a "colour change" in the vertical middle of the subpicture
		spumuxxmls += '<spu start="' + starttime + '" end="' + endtime + '" image="' + outname + '"  >' + "\n"
		spumuxxmls += '<row startline="0" endline="' + str(height - 1) + '" >' + "\n" #height or height-1?
		spumuxxmls += '<column start="0" b="rgba(0,0,0,0)" p="rgba(0,0,0,255)" e1="' + Status.NeutralColour + '" e2="' + Status.Team1.Colour + '" />' + "\n"
		spumuxxmls += '<column start="' + str(width/2) + '" b="rgba(0,0,0,0)" p="rgba(0,0,0,255)" e1="' + Status.NeutralColour + '" e2="' + Status.Team2.Col
our + '" />' + "\n"
		#Above does the below pseudocode, with a suitably patched spumux binary(!)
		#xml chg_colcon (all rows, col 0 to middle, TeamColour = Status.Team1.Colour)
		#xml chg_colcon (all rows, col middle to last, TeamColour = Status.Team2.Colour)
		spumuxxmls += "</row>\n</spu>\n"	

	def Serialise(fileroot):
		#make a set of files based on root name
		#Colours are Transparent, Black(outline), NeutralColour (for time), TeamColour (for team dependant colouring)
		#encoding is fileroot+subtitlestream+subtitlenum.png, with a fileroot+subtitlestream.xml for the spumux config
		Status = #null status
		spuframes = [0,0,0]
		outname = ["","",""]
		spumuxxmls = ["<subpictures>\n<stream>\n","<subpictures>\n<stream>\n","<subpictures>\n<stream>\n"]
		for Delta in self.JamDeltas:
			Status.Update(Delta)
			#update Score
           #Scorelines update precisely once per jam, at the start of the jam (when a new chapter happens). 
           #Jammerlines update at the same time as a Scoreline (new jammers at start of each jam), but also at LJ, PJ, SP points during a jam
           #Therefore ScoreJammerlines are precisely as frequent as Jammerlines, as each Scoreline also has a Jammerline
           #Also Therefore: We can combine Chapter detection during a Bout (outside the bout, we need more Chapters for Skateout+Credits, and we might need 
           # more than one bout in a DVD) with Scorelines
			if Delta.Score is not None:
				spuframe[0] += 1 #increment number of Scoreline frames
                        
				printline (Status.Team1.Name, location, Status.TeamColour)
				printline (Status.Team1.Score, location1, Status.TeamColour)
			
				printline (Status.Period+":"+Status.Jam, locationx, Status.NeutralColour)
			
				printline (Status.Team2.Score, location2, Status.TeamColour)
				printline (Status.Team2.Name, location3, Status.TeamColour)
				outname[0] = "Scoreline" + str(spuframe[0]) + ".png"

				self.AddSpumuxxml(spumuxxmls[0],starttime,endtime,outname[0],Status.NeutralColour,Status.Team1.Colour,Status.Team2.Colour)

			#update Jammer
			if Delta.Jammer is not None:
				spuframe[1] += 1 #increment number of Jammerline frames


				#also represent LJ,PJ,SP status somehow (icon? bold/italics?)
				printline (Status.Team1.Jammer, location, Status.Team.Colour)
				printline (Status.Team2.Jammer, location2, Status.Team.Colour)
				outname[1] = "Jammerline" + str(spuframe[1]) + ".png"

				self.AddSpumuxxml(spumuxxmls[1],starttime,endtime,outname[1],Status.NeutralColour,Status.Team1.Colour,Status.Team2.Colour)

			#update JammerScore
			# take latest Score and latest Jammer, and sum them, taking the start time of the later of the two (possibly do this as a second pass)
			spuframe[2] += 1
			outname[2] = "JammerScoreline" + str(spuframe[2]) + ".png"
			#call convert(?) to smoosh the two pngs together into the third
			try:
				retcode = subprocess.call("convert --composite " + outname[0] + " " + outname[1] + " " + outname[2], shell=True)
				if retcode < 0:
					print >>sys.stderr, "Child was terminated by signal", -retcode
			except OSError as e:
				print >>sys.stderr, "Execution failed:", e

			self.AddSpumuxxml(spumuxxmls[2],starttime,endtime,outname[2],Status.NeutralColour,Status.Team1.Colour,Status.Team2.Colour)

		#and close the xml streams
		spumuxxmls = [i+"</stream>\n</subpictures>\n" for in spumuxxmls]

		#write spumuxxmls to files

		#and mux with spumux
		moviefile = "bout"
		num = 0
		for i in spumuxfiles:
			outfile = moviefile + str(num)
			try:
				retcode = subprocess.call("spumux -s" + str(num) + " " + i + " < " + moviefile + ".mpg > " + outfile + ".mpg", shell=True)
				if retcode < 0:
					print >>sys.stderr, "Child was terminated by signal", -retcode
			except OSError as e:
				print >>sys.stderr, "Execution failed:", e
			num += 1
			moviefile = outfile
		#At this point, we have a file called "bout012.mpg", which has bout.mpg muxed with the 3 subtitle files, hopefully


def WriteDVDxml():
<dvdauthor>
<vmgm></vmgm>
<titleset>
<menus>
<video format="pal" aspect="4:3" resolution="720x576"/>
<audio format="ac3" channels="2"/>
<pgc entry="root">
<button>subtitle=64; jump title 1;</button>
<button>subtitle=65; jump title 1;</button>
<vob file="menu.mpg"/>
</pgc>
</menus>
#more menus than this

<titles>
#aspect ratio probably 16:9
<video format="pal" aspect="4:3"/>
<audio format="mp2" channels="2"/>
<subpicture lang="en"/>
<subpicture lang="it"/>
<pgc>
<vob file="bout012.mpg" pause="6"/>
<post>call menu;</post>
</pgc>
</titles>
</titleset>
</dvdauthor>
#write this to auth.xml

#and author
subprocess.call("dvdauthor -o mydvd -x auth.xml", shell=True)
#and iso
mkisofs -r -V "nameofdvd" -dvd-video -o "nameofdvd.iso" mydvd
