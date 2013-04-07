#

###
#
# DVD Chapter & Subtitle Script
#
###
import string, Image, ImageDraw, ImagePalette, ImageFont
import os, sys, codecs, subprocess, textwrap



#these parts and other bits of code for writing nice subtitle images stolen from aug.ment.org/dvd/makespumux.py
width = 720;
height = 576;
fontsize = 20;
#font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf", fontsize)
font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize)
rubyfont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf",fontsize-4)
menufont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize+4)
def drawoutlinedtext(drawhandle,x,y,text, font, outlinecol, textcol):
	"""Draws to drawhandle at location(x,y) the text in text, outlined in outlinecol, rendered in textcol"""
	
	draw.text((x-1, y), text, font=font, fill=outlinecol)
	draw.text((x+1, y), text, font=font, fill=outlinecol)
	draw.text((x, y-1), text, font=font, fill=outlinecol)
	draw.text((x, y+1), text, font=font, fill=outlinecol)
	draw.text((x, y), text, font=font, fill=textcol)

def getrightalignedloc(draw, x,text, font):
	"""Correct width location so text looks right-aligned (PIL only does left)"""
	w, h = draw.textsize(text,font=font)
	return x-w #shift "rightaligned location" back by length of text

def getcentredloc(draw,text,font):
	"""Correct width location so text is centred (PIL only does left)"""
	w, h = draw.textsize(text,font=font)
	return (width-w)/2 #shift "centred location" back by 1/2 length of text

def initSubImage():
	"""Initalise the PIL canvas for a new SubImage"""
	im = Image.new('P',(width, height), 1 )
        palette = []
        palette.extend( ( 255,255,255 )  ) #maps to transparent = 1
        palette.extend( ( 0,0,0 )  ) #maps to black outline colour = 2 
	palette.extend( ( 255,0,0) ) #maps to team colours (changed dynamically by chg_colcon in finished subtitles) = 3
	palette.extend( ( 200,200,200) ) #maps to "neutral" colour (for Period, Jam, other indicators) = 4
        im.putpalette(palette)
        draw = ImageDraw.Draw(im);
	return draw, im

def makeScoreSubImage (filename, Status):
	"""make a 3colour png for the Scoreline, at top of display"""
	#needs to make
	#
	#  T1 S1  PPJJJ  S2 T2  59 char width (out of 60 allowed)
	d,i = initSubImage()
	string1 = '{:<20}'.format(Teams[Status.Team1.ID]["Name"]) 
	string1 += '  ' + '{0:<3}'.format(Status.Team1.Score)
	string2 += 'P' + Status.Period + 'J' + '{:<2}'.format(Status.Jam)
	string3 += '{0:<3}'.format(Status.Team2.Score)
	string3 += '  ' + '{:>20}'.format(Teams[Status.Team2.ID]["Name"])
	 
	#regularise team name + score lines to standard length
	drawoutlinedtext(d,6,22,string1,font,2,3)
	drawoutlinedtext(d,getcentredloc(d,string2,font),22,string2,font,2,4)
	drawoutlinedtext(d,getrightalignedloc(d,714,string2,font),22,string3,font,2,3)
	i.save( filename, "PNG", transparency=1)

def makeJammerSubImage (filename, Status):
	"""make a 3colour png for the Jammerline, at bottom of display"""
	#needs to make
	#
	# J1 Status      Status J2 (allowed width 60 = 720)
	d,i = initSubImage()
	#it is possible (cf "The Very Hungry Splatterkiller" = 30 chars) for jammer names to be too long for fields
	#consider wrapping names in that case, using the textwrap.wrap(text,width) method
	jammers = (Teams[Status.Team1.ID]["Skaters"][Status.Team1.Jammer],(Teams[Status.Team1.ID]["Skaters"][Status.Team2.Jammer])
	string1 = '{:<25}'.format(jammers[0])
	string2 = '{:>25}'.format(jammers[1])
	drawoutlinedtext(d,6,550,string1,font,2,3)
	drawoutlinedtext(d,getrightalignedloc(d,714,string2,font),550,string2,font,2,3)
	#strings1a, 2a are the status strings for jammer status, and appear above the names
	statusstrs = ["",""]
	if Status.LeadJammer is not None:
		statusstrs[Status.LeadJammer] += "Lead "
		statusstrs[1 - Status.LeadJammer] += "     "
	else:
		statusstrs = [s + "     " for s in statusstrs]
	if Status.PowerJam is not None:
		statusstrs[Status.PowerJam] += "Power "
		statusstrs[1 - Status.PowerJam] += "     "
	else:
		statusstrs = [s + "     " for s in statusstrs] 
	if Status.Team1.StarPass is not None:
		statusstrs[0]

def makeMenuSubImage(filename,Chapters,last=False):
	"""make a set of gridded 3colour pngs for selecting the given Chapters"""
	#needs to make 
	#
	#  C C C C
	#  C C C C
	#  B     N
	# and needs to know if needs N (if last Chapter is in the list then we don't need it)
	d,i = initSubImage()
	
	#render blocks of 4, width=10 chars + 2 char padding
	#normal image is called filename+"n.png"
	#select image is called filename+"s.png"
	#highlight image is called filename+"h.png"

def makeCreditsCrawl(Teams,Officials,Extracredits)
	"""Make a long png for the credits crawl to be rendered from"""
	#first we need to collect metrics, as we need to make our image the right length
	#this requires a "sacrificial" image to let us use the draw.textsize metric
	im = Image.new('RGB',(width,height))
	d = ImageDraw.Draw(im)
	w, h = d.textsize("A",font=creditsfont)
	#get metrics and workout how much space we need
	numlines = 5 #intro and outro padding
	#these need modified to account for line wrapping (length is sum(len( sum of textwrap.wrap(s, txt_width) for s in t["Skaters"] )) etc)
	numlines += sum([len(s["Skaters"])+4 for s in Teams]) #num of skaters + 2 for League,Team + 2 for spacing
	numlines += len(Officials["Skaters"])+3 #num of skaters + 1 for title + 2 for spacing
	numlines += len(Extracredits)
	
	crawl_height = numlines * h
	#and make our working image
	im = Image.new('RGB',(width,crawl_height))
	d = ImageDraw.Draw(im)	

	rendertoppiece
	for t in Teams:
		renderleaguename
		renderteamname
		for s in Teams["Skaters"]:
			renderskater, captains first, benchstaff last
		render2blanks
	for o in Officials:
		renderofficial, headref first, titles!
	render2blanks
	for line in Extracredits:
		renderline



def AddChapter(ChapterList,Time,Name):
	return ChapterList.append({"T":Time,"N":Name})


def Serialise(ChapterList, baseimg):
	#this will write out the entire movie now, so execute last of all Serialisers
	#it needs the credits done, as well as the movie subtitles muxed
	
	#start by writing out the header for dvdauthor
	'<?xml version="1.0" encoding="UTF-8"?>' + "\n"
	'<dvdauthor dest="' + pathtodvdtmpdir + '">' + "\n"
	"<vmgm>\n"
	"<fpc>\n"
	"jump menu 1\n" #I think this goes to the first menu in the vmgm...
	"</fpc>\n"
	#define the main menu here in the vmgm
	"<menus>\n"
	"<pgc>\n"
	#TODO - jump to titleset 1 title 1 (the movie) or titleset 1 menu 1 (first chapter menu)
	# or jump to menu 2 (in the vmgm), the subtitles menu
	"<\pgc>\n"
	'<pgc entry="subtitle">' + "\n"
	#TODO - the subtitles menu (set subtitles to none,0,1,2)
	"</pgc>\n"
	"</menus>\n"
	"</vmgm>\n"
	"<titleset>\n"
	"<menus>"
	for block of 8 chapters:
		#make 3 subpictures (4x2 arrangement) - normal, highlight, select
		if last block, last = True #removes "Next" button
		if first block, first = True #changes "Prev" button target to the main menu
		fname="chaptermenu"+str(blocknum)
		makemenuSubImage(fname,block,last)
		#make xml for spumux (this stuff is output to menuspumux.xml not the auth.xml)
		#remember to add autobutton detection, in row then column mode
		"<subpictures><stream>\n"
		'<spu force="yes" start="00:00:00:00" image="' + fname + 'n.png" select="' + fname + 's.png" highlight="' + fname + 'h.png" >' + "\n"
		"</spu></stream></subpictures>\n"
		#and mux
		spumux menuspumux.xml < menubackdrop.mpg > fname+".mpg"

		#outputthe xml for this menu for dvdauthor (this is where the actions come in

		"<pgc>\n"
		for chapter in block:
			"<button>jump chapter" + chapter.index + ";</button>\n"
		"<button>jump menu" prev chaptermenu or main menu if first + ";</button>\n"
		if not last "<button> jump menu" next chaptermenu + ";</button>\n"
		'<vob file="'+fname+'.mpg" />' + "\n"

		"</pgc>\n"

	"</menus>\n"
	#now we've done the menus, setup the movie bit, with the list of chapters
	"<titles>"
	'<video format="pal" aspect="16:9" widescreen="nopanscan" />' + "\n"
	"<pgc>\n"
	'<vob file="' + name of movie itself + '" chapters="' + ",".join([c.Time for c in ChapterList]) + '" />' + "\n"
	"<post>jump title 2;</post>\n" #the credits are title 2
	"</pgc>\n"
	#and add the credits as title 2
	"<pgc>\n"
	'<vob file="' + name of credits + '" />' + "\n"
	"<post>jump vmgm menu 1;</post>\n" #jump back to the main menu, in the vmgm
	"<\pgc>\n"
	"</titles>\n"
	"</titleset>\n"
	"</dvdauthor>\n"

class JamSubs(object):
	def __init__(self):
		self.


	def AddChange(JamDelta):
		#make change to "core list", and update only the subtitle streams we need to (can we store changes as diffs internally??)
		# Deltas are always Jammerlines (and thus always ScoreJammerlines), as we only change the Scoreline on new jams. Just store Deltas and detect *Scorelines* as being also *Chapters* (since Chapters are also on new Jams)

	def AddSpumuxxml(spumuxxml, starttime, endtime, outname, NeutralColour, Team1Colour, Team2Colour):
		#Add a subpicture's xml to the provided spumuxxml stream, with a "colour change" in the vertical middle of the subpicture
		spumuxxmls += '<spu start="' + starttime + '" end="' + endtime + '" image="' + outname + '"  >' + "\n"
		spumuxxmls += '<row startline="0" endline="' + str(height - 1) + '" >' + "\n" #height or height-1?
		spumuxxmls += '<column start="0" b="rgba(0,0,0,0)" p="rgba(0,0,0,255)" e1="' + Team1Colour + '" e2="' + NeutralColour + '" />' + "\n"
		spumuxxmls += '<column start="' + str(width/2) + '" b="rgba(0,0,0,0)" p="rgba(0,0,0,255)" e1="' + Team2Colour + '" e2="' + NeutralColour + '" />' + "\n"
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
