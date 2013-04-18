#

###
#
# DVD Chapter & Subtitle Script
#
###
import string, Image, ImageDraw, ImagePalette, ImageFont
import os, sys, codecs, subprocess, textwrap, itertools

#might need to make this do
#from data_chapter import * 
# to get the data_chapter version of Bout, depending on how picky pickle is about reconstructing classes
#(it might not like the data_chapter and dvd_chapter versions of Bout being from different modules, despite being identical).
#really confused by what pickle needs to be in scope to reconstruct a class. 
#even without the necessary module loaded, pickle can apparently "load" a class
#probably fine with "data only classes", like Bout...

#these parts and other bits of code for writing nice subtitle images stolen from aug.ment.org/dvd/makespumux.py
width = 720;
height = 576;
fontsize = 20; # fontsize may not be big enough for subs. Might have to use "menufont" for subs too
#font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf", fontsize)
font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize)
rubyfont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf",fontsize-4)
menufont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize+4)
creditsfont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize*2)

#Structure

class Bout(object):
	def __init__(self):
		self.Name = None
		self.Teams = [] #team 1,2
		self.Officials = []
		self.Jams = []
		#self.Timeouts = []
		self.Timing = Timing()
		self.NeutralCol = (200,200,200)

class Timing(object):
	def __init__(self):
		self.Start = ""
		self.Skateout = ""
		self.Halftime = ""
		self.Fulltime = ""
		self.Awards = ""

class Team(object):
	def __init__(self):
		self.LeagueName = ""
		self.TeamName = ""
		self.TeamCol = (255,255,255) #R,G,B tuple
		self.Skaters = []

class Skater(object):
	def __init__(self):
		self.Skatename = ""
		self.Number = ""
		self.Role = SKATER #see enum below

#enum for Skater (designed so order by Role gives credits order):

CAPTAIN = 0
VICECAPTAIN = 1
SKATER = 2
BENCH = 3
LINEUP = 4


class Official(object):
	def __init__(self):
		self.Name = ""
		self.Number = ""
		self.Role = None #see enum below

#enum for Official (designed so order by Role gives credits order):
HEAD=0
JAM=1
IPR=2
OPR=3

class Jam(object):
	def __init__(self):
		self.StartTime = ""
		self.Period = '0'
		self.Jam = '0'
		self.Jammers = [] #refs to Skaters, Team1,Team2
		self.Pivots = [] #refs to Pivots, Team1, Team2
		self.Score = [] #numerical scores to Team1,Team2
		self.Events = [] #contains the moments of Lead Jammer, Power Jam start/end, Star Pass
		#self.EndTime = ""

class Event(object):
	def __init__(self):
		self.Time = ""
		self.Team = None #0 or 1 for Team 1 or 2  - this turns out to be 1,2 from interface, so we fix in Status function
		self.Type = None #LJ, PJStart, PJEnd, Star Pass

#enum for Events
LEAD=0
POWERSTART = 1
POWEREND = 2
STAR = 3


class Status(object):
	#An integral of Event objects within a jam
	def __init__(self, eventseq):
		tr_dict = {LEAD:lambda x: x | LEAD_STATUS,POWERSTART: lambda x: x | POWER_STATUS,POWEREND:lambda x : x & POWER_CANCEL,STAR: lambda x : x | STAR_STATUS}
		self.Time=eventseq[-1].Time #our time is always that of last event in passed sequence
		self.Teams = [0,0]
		for e in eventseq:
			#handle dummy rows for jam start events (which use POWEREND with no POWERSTART)
			#don't need to do anything now, since the bitwise op will just unset an unset bit!
			#need to subtract one from e.Team cause of annoying interface issues with things starting at 0
			self.Teams[e.Team-1] = tr_dict[e.Type](self.Teams[e.Team-1])
			
#masks for Status
LEAD_STATUS=1
POWER_STATUS=2
STAR_STATUS=4
POWER_CANCEL = 7 - POWER_STATUS #use with AND to unset the POWER_STATUS bit
#Functions of the Bout Render class render a contained Bouts object

#to make a dvd:
# init BoutRender object with Bouts you care about, options for extra credits, input images etc
# b = BoutRender(Bouts,Extracredits)
# mux subtitles
# b.RenderSubtitles()
# render credits
# b.RenderCredits()
# and render menus + DVD
# b.RenderDVD()

def drawoutlinedtext(draw,x,y,text, font, outlinecol, textcol):
	"""Draws to drawhandle at location(x,y) the text in text, outlined in outlinecol, rendered in textcol"""
	
	draw.text((x-1, y), text, font=font, fill=outlinecol)
	draw.text((x+1, y), text, font=font, fill=outlinecol)
	draw.text((x, y-1), text, font=font, fill=outlinecol)
	draw.text((x, y+1), text, font=font, fill=outlinecol)
	draw.text((x, y), text, font=font, fill=textcol)

def getrightalignedloc(draw, x,text, font):
	"""Correct width location so text looks right-aligned (PIL only does left)"""
	w, h = draw.textsize(text,font=font)
	#print w
	return x-w #shift "rightaligned location" back by length of text

def getcentredloc(draw,text,font,x=width/2):
	"""Correct width location so text is centred (PIL only does left)"""
	w, h = draw.textsize(text,font=font)
	return x-(w/2) #shift "centred location" back by 1/2 length of text

def initSubImage():
	"""Initalise the PIL canvas for a new SubImage"""
	im = Image.new('P',(width, height), 0 ) #fairly sure that colours do start from 0 now...(so this makes colour 0 background + transp)
	palette = []
	palette.extend( ( 255,255,255 )  ) #maps to transparent =  0??
	palette.extend( ( 0,0,0 )  ) #maps to black outline colour =  1??
	palette.extend( ( 255,0,0) ) #maps to team colours (changed dynamically by chg_colcon in finished subtitles) =  2 ??
	palette.extend( ( 200,200,200) ) #maps to "neutral" colour (for Period, Jam, other indicators) = 3??
	im.putpalette(palette)
	draw = ImageDraw.Draw(im);
	return draw, im

class BoutRender(object):
	def __init__(self,Bouts,Extracredits="",movie="bout.mpg",mainsrc="main.jpg",chpsrc="menu.jpg",creditmusic="creditmusic.ogg"):
		self.Bouts = Bouts
		self.Extracredits=Extracredits
		self.Movie=movie
		self.MainSrc=mainsrc
		self.ChpSrc=chpsrc
		self.CreditMusic=creditmusic
			
	def makeScoreSubImage (self,filename, boutnum,jamnum):
		"""make a 3colour png for the Scoreline, at top of display"""
		#needs to make
		#
		#  T1 S1  PPJJJ  S2 T2  59 char width (out of 60 allowed)
		d,i = initSubImage()
		string1 = '{0:<20.20}'.format(self.Bouts[boutnum].Teams[0].TeamName) 
		string1 += '  ' + '{0:0>3.3}'.format(self.Bouts[boutnum].Jams[jamnum].Score[0])
		string2 = 'P' + self.Bouts[boutnum].Jams[jamnum].Period + 'J' + '{0:0<2.2}'.format(self.Bouts[boutnum].Jams[jamnum].Jam)
		string3 = '{0:0>3.3}'.format(self.Bouts[boutnum].Jams[jamnum].Score[1])
		string3 += '  ' + '{0:>20.20}'.format(self.Bouts[boutnum].Teams[1].TeamName)
		 
		#regularise team name + score lines to standard length
		drawoutlinedtext(d,6,22,string1,font,1,2)
		drawoutlinedtext(d,getcentredloc(d,string2,font),22,string2,font,1,3)
		drawoutlinedtext(d,getrightalignedloc(d,714,string3,font),22,string3,font,1,2)
		i.save( filename, "PNG", transparency=0)
	
	def makeJammerSubImage (self,filename, boutnum,jamnum,status):
		"""make a 3colour png for the Jammerline, at bottom of display"""
		#needs to make
		#
		# J1 Status      Status J2 (allowed width 60 = 720)
		d,im = initSubImage()
		#it is possible (cf "The Very Hungry Splatterkiller" = 30 chars) for jammer names to be too long for fields
		#consider wrapping names in that case, using the textwrap.wrap(text,width) method
			
		#status is an integration of the events up to + including the current event (so Star Passes stick, etc)
		#if status.Team[n] & STAR_STATUS then use Pivot[n] instead
		jammers = []
		prepend = [["","(SP)"],["","LJ "],["","PJ "]]
		append = [["(SP)",""],[" LJ",""],[" PJ",""]]
		for i in range(2):
			if status.Teams[i] & STAR_STATUS == STAR_STATUS : 
				jammers.append(prepend[0][i]+self.Bouts[boutnum].Jams[jamnum].Pivots[i][0:21]+append[0][i])
			else:  
				jammers.append(self.Bouts[boutnum].Jams[jamnum].Jammers[i][0:25])
			if status.Teams[i] & LEAD_STATUS == LEAD_STATUS :
				jammers[i] = prepend[1][i] + jammers[i] + append[1][i]
			if status.Teams[i] & POWER_STATUS == POWER_STATUS :
				jammers[i] = prepend[2][i] + jammers[i] + append[2][i]

		string1 = '{0:<28.28}'.format(jammers[0])
		string2 = '{0:>28.28}'.format(jammers[1])
		
		drawoutlinedtext(d,6,550,string1,font,1,2)
		drawoutlinedtext(d,getrightalignedloc(d,714,string2,font),550,string2,font,1,2)
		#strings1a, 2a are the status strings for jammer status, and appear above the names
		#how do we signal Lead, Power jams?
		#statusstrs = ["",""]
		#if status.Teams[i] & LEAD_STATUS == LEAD_STATUS:
		#	statusstrs[Status.LeadJammer] += "Lead "
		#	statusstrs[1 - Status.LeadJammer] += "     "
		#else:
		#	statusstrs = [s + "     " for s in statusstrs]
		#if Status.PowerJam is not None:
		#	statusstrs[Status.PowerJam] += "Power "
		#	statusstrs[1 - Status.PowerJam] += "     "
		#else:
		#	statusstrs = [s + "     " for s in statusstrs] 
		im.save( filename, "PNG", transparency=0)

	def makeMainMenu(self):
		"""Make the main menu, from a standard backdrop"""
		#make menu backdrop
		subprocess.call("ffmpeg -loop 1 -shortest -y -i " +self.MainSrc+" -i /usr/share/devede/silence.ogg -target dvd main.mpg",shell=True)
		#make subimages
		self.makeMainMenuSubImage("main")
		#mux
		menuxml = "<subpictures><stream>\n"
		menuxml += '<spu force="yes" start="00:00:00:00" image="mainn.png" select="mains.png" highlight="mainh.png" >' + "\n"
		menuxml += "</spu></stream></subpictures>\n"
		#and write out
		f = open("mainspumux.xml",'w')
		f.write(menuxml)
		f.flush()
		f.close()
		subprocess.call("spumux mainspumux.xml < main.mpg > mainmenu.mpg", shell=True)

	def makeMainMenuSubImage(self,filename):
		"""Make the Main menu, from the standard menu subimages"""
		#this does 
		#      blank top of screen until low down row
		#     [Play] [Chapters] [Subtitles]
		ctrls = (("n.png",1,3),("s.png",1,2),("h.png",2,1))
		for ctrl in ctrls:
			d,i = initSubImage()
			fname = filename + ctrl[0]
			ol = ctrl[1]
			fg = ctrl[2]
			spacing = width / 4
			for (txt,x) in zip(("Play","Chapters","Subtitles"),range(1,4)):
				l = spacing * x
				#txt pretty low on screen
				drawoutlinedtext(d,getcentredloc(d,txt,font,l),476,txt,font,ol,fg)
			i.save( fname, "PNG", transparency=0)

	def makeSubtitlesMenu(self):
		"""Make the Subtitles selection menu, from standard backdrop + subtitle menus"""
		#make menu backdrop
		subprocess.call("ffmpeg -loop 1 -shortest -y -i "+ self.ChpSrc + " -i /usr/share/devede/silence.ogg -target dvd subtitles.mpg",shell=True)	
		#make subimages
		self.makeSubtitlesSubImage("subtitles")
		#mux
		menuxml = "<subpictures><stream>\n"
		menuxml += '<spu force="yes" start="00:00:00:00" image="subtitlesn.png" select="subtitless.png" highlight="subtitlesh.png" >' + "\n"
		menuxml += "</spu></stream></subpictures>\n"
		#and write out
		f = open("subtitlesspumux.xml",'w')
		f.write(menuxml)
		f.flush()
		f.close()
		#and mux
		subprocess.call("spumux subtitlesspumux.xml < subtitles.mpg > subtitlesmenu.mpg", shell=True)

	def makeSubtitlesSubImage(self,filename):
		"""Make the Subtitles menu, from the standard Subtitles subimages"""
		#this does (columnar?)
		# [No Overlay]
		# [Scoreline + Jam Numbers]
		# [Jammers + Statuses]
		# [Both of the Above]
		ctrls = (("n.png",1,3),("s.png",1,2),("h.png",2,1))
		for ctrl in ctrls:
			d,i = initSubImage()
			fname = filename + ctrl[0]
			ol = ctrl[1]
			fg = ctrl[2]
			spacing = height / 6
			for (txt,y) in zip(("None","Scoreline + Period/Jam","Jammers","Both Above"),range(1,5)):
				l = spacing * y + (spacing/2) #nicely vertically centre!
				drawoutlinedtext(d,getcentredloc(d,txt,font),l,txt,font,ol,fg)
			#do menu design stuff
			i.save( fname, "PNG", transparency=0)
		
	def makeMenuSubImage(self,filename,Chapters,last=False):
		"""make a set of gridded 3colour pngs for selecting the given Chapters"""
		#needs to make 
		#
		#  C C C C
		#  C C C C
		#  B     N
		# and needs to know if needs N (if last Chapter is in the list then we don't need it)
		#  								(we replace it with a link to Credits)
		#ctrl is namesuffix,outline,fgcol
		ctrls = (("n.png",1,3),("s.png",1,2),("h.png",2,1))
		for ctrl in ctrls:
			d,i = initSubImage()
			fname = filename + ctrl[0]
			ol = ctrl[1]
			fg = ctrl[2]
			spacing = width / 5
			for c,j in zip(Chapters,range(0,8)):
				string = '{0:^10.10}'.format(c[1]) #make a centred string from the chapter name, length 10
				x = (1+(j%4))*spacing #4 across
				y = 100+(j//4 * 150) #2 down, starting highish
				drawoutlinedtext(d,getcentredloc(d,string,font,x),y,string,font,ol,fg)
	
			back = '{0:^10.10}'.format("Back")
			drawoutlinedtext(d,getcentredloc(d,back,font,spacing),400,back,font,ol,fg)
			next = ""
			if last:
				next = '{0:^10.10}'.format("Credits")
			else:
				next = '{0:^10.10}'.format("Next")
			drawoutlinedtext(d,getcentredloc(d,next,font,spacing),400,next,font,ol,fg)
			i.save( fname, "PNG", transparency=0)
					
		#render blocks of 4, width=10 chars + 2 char padding
		#normal image is called filename+"n.png"
		#select image is called filename+"s.png"
		#highlight image is called filename+"h.png"
	
	def RenderCredits(self):
		"""Make a long png for the credits crawl to be rendered from"""
		#first we need to collect metrics, as we need to make our image the right length
		#this requires a "sacrificial" image to let us use the draw.textsize metric
		im = Image.new('RGB',(width*2,height*2)) #
		d = ImageDraw.Draw(im)
		w, h = d.textsize("A",font=creditsfont)
		#get metrics and workout how much space we need
	
		#get Teams, Officials from Bouts structure
	
		font=creditsfont
		filename="credits.mpg"
		#increment y as we move down the credits
		y = height*2 #just a quick alias to make it clear we're leaving a bit blank at the top
		#some nice greys for default outline, fg colours
		ol = "#202020"
		fg = "#f0f0f0"
		longzip = lambda tup : itertools.izip_longest(*tup,fillvalue=" ")
		#this is how we prerender (the height we need is y+height at the end)
		credit_txt = [] #the holder for our lines to render
		for b in self.Bouts:
			if b.Name is not None:
				txtlines = textwrap.wrap(b.Name,50) #operating with 60 chars per line, but nice centring
			else: #construct bout name from Team names
				wrappednames=[textwrap.wrap(t.TeamName,22) for t in b.Teams]
				
				txtlines = ['{0:>22.22}   {1:<22.22}'.format(*a) for a in longzip(wrappednames)]  
				txtlines[0] = txtlines[0][:23] + "v" + txtlines[0][24:]
				#
			for line in txtlines:
				credit_txt.append((line,y,ol,fg))
				y+=h
			y += 2*h 
			for t in b.Teams:
				
				#get the team colour to make fancy coloured credits
				tfg = t.TeamCol
				tol = tuple([c/8 for c in tfg])
				credit_txt.append((t.LeagueName,y,tol,tfg))
				y += h
				credit_txt.append((t.TeamName,y,tol,tfg))
				y += h
				titles = ["Captain","Vice-Captain","","Bench Coach","Line-up Manager"]
				for s in t.Skaters:
					if (s.Skatename is None) or (s.Skatename.strip() == ""):
						break 
					#render title if this is first skater in list with this title
					
					tt = titles[s.Role]
					#wrap skatername and number in 27 line space
					snspace = 27 - (len(s.Number)+3) #space for skatename after making room for number
					nt = textwrap.wrap(s.Skatename,snspace)
					sp,np=[str(snspace),str(27-snspace)]
					formatting = '{0:>27.27} {1:<'+sp+'.'+sp+'}{2:>'+np+'.'+np+'}'
					
					lines = [formatting.format(*a) for a in longzip([[tt],nt,['('+s.Number+')',]])]
					for line in lines:
						credit_txt.append((line,y,tol,tfg))
						y+=h
				y += 2*h #two blank "lines"

			credit_txt.append(("Skating Officials",y,ol,fg))
			y += h
			t = None
			titles = ["Head Referee","Jammer Ref","Inside Pack Ref", "Outside Pack Ref"]
			for o in b.Officials:
				if (o.Name is None) or (o.Name.strip() == ""):
					break
				if t != o.Role:
					tt = titles[o.Role]
					t = o.Role
				else:
					tt = ""
				nt = textwrap.wrap(o.Name,27) 
				lines = ['{0:>27.27} {1:<27.27}'.format(*a) for a in longzip([[tt],nt])]
				for line in lines:
					credit_txt.append((line,y,ol,fg))
					y+=h
			y += 2*h #two blank "lines"
		for line in self.Extracredits:
			#consider explicitly forcing wrapping here
			credit_txt.append((line,y,ol,fg))
			y += h

		#make an image and a line-writer for it
		crawl_height = y + height*2 #for scrolling off screen again
		#make an image twice as big as destination so we can resize frames later to "antialias" scrolling and make it all look pro.		
		im = Image.new('RGB',(width*2,crawl_height))
		d = ImageDraw.Draw(im)
		dct = lambda txt,y,ol,fg : drawoutlinedtext(d,getcentredloc(d,txt,font,x=width),y,txt,font,ol,fg)

		#and render to image
		[dct(*l) for l in credit_txt]

		#calculate frames needed for 30 second run length (*25? fps)
		#we should actually calculate the credits length from the music supplied
		# if it's an Ogg Vorbis container, with the ogg.vorbis module, this would be
		# file = ogg.vorbis.VorbisFile(filename)
		# file.time_total(0) in seconds
		#similarly with the "audiotools" module, which provides the .seconds_length method on files
		# presumably audiotools.open(filename).seconds_length() will work? 
		# or pydub?
		frames = 30*25
		pixels_per_frame = float(crawl_height) / frames
		#blendfrac = pixels_per_frame - int(pixels_per_frame)
		#int_p_p_f = int(pixels_per_frame)
		#render frames 
		for i in range(frames):
			disp1 = im.crop([0,int(i*pixels_per_frame),width*2,int(i*pixels_per_frame)+height*2])
			display = disp1.resize((width,height),Image.ANTIALIAS)
			#display.load()
			#print display
			#scratch = Image.new('RGB',(width,height))
			#scratch.paste(display,None)
			#scratch.save("cr_frm"+'{0:04d}'.format(i)+".png",'PNG')
			display.save("cr_frm"+'{0:04d}'.format(i)+".png",'PNG')		
		#and make movies -r 25 = 25fps, -t 30 = 30 seconds duration
		if (self.CreditMusic == None) or (self.CreditMusic.isspace() ):
			print "No Music Selected for Credits"
			sys.exit(1)
		subprocess.call("ffmpeg -f image2 -r 25 -i cr_frm%04d.png -i "+ self.CreditMusic +" -target dvd -t 30 "+ filename,shell=True)

	def Tuple2Txt(self,tup):
		return "rgba(%2d,%2d,%2d,255)" % tup
		
	def AddSpumuxxml(self,spumuxxml, starttime, endtime, outname, NeutralColour, Team1Colour, Team2Colour):
		#Add a subpicture's xml to the provided spumuxxml stream, with a "colour change" in the vertical middle of the subpicture
		spumuxxml += '<spu start="' + starttime + '" end="' + endtime + '" image="' + outname + '"  >' + "\n"
		spumuxxml += '<row startline="0" endline="' + str(height - 1) + '" >' + "\n" #height or height-1?
		spumuxxml += '<column start="0" b="rgba(0,0,0,0)" p="rgba(0,0,0,255)" e1="' + self.Tuple2Txt(Team1Colour) + '" e2="' + self.Tuple2Txt(NeutralColour) + '" />' + "\n"
		spumuxxml += '<column start="' + str(width/2) + '" b="rgba(0,0,0,0)" p="rgba(0,0,0,255)" e1="' + self.Tuple2Txt(Team2Colour) + '" e2="' + self.Tuple2Txt(NeutralColour) + '" />' + "\n"
		#Above does the below pseudocode, with a suitably patched spumux binary(!)
		#xml chg_colcon (all rows, col 0 to middle, TeamColour = Status.Team1.Colour)
		#xml chg_colcon (all rows, col middle to last, TeamColour = Status.Team2.Colour)
		spumuxxml += "</row>\n</spu>\n"	
		return spumuxxml

	def RenderSubtitles(self):
		#make a set of files based on root name
		#Colours are Transparent, Black(outline), NeutralColour (for time), TeamColour (for team dependant colouring)
		#encoding is fileroot+subtitlestream+subtitlenum.png, with a fileroot+subtitlestream.xml for the spumux config
		spuframes = [0,0,0]
		outname = ["","",""]
		spumuxxmls = ["<subpictures>\n<stream>\n","<subpictures>\n<stream>\n","<subpictures>\n<stream>\n"]

		# revise below (we're now Bout centric) 
		# for Jam in Bout.Jams:
		#	do Scoreline at start of Jam	
		#	do Jammerline at start of Jam
		#	do ScoreJammerline at start of Jam
		#	for Event in Jam:
		#		do Jammerline
		#		do ScoreJammerline
		for boutnum in range(len(self.Bouts)):
			for (Jam,i) in zip([J for J in self.Bouts[boutnum].Jams if ":" in J.StartTime],range(len(self.Bouts[boutnum].Jams))):
				#It is disturbingly possible that Jams contains "blank time" entries at this point
				#Need to strip those out.
				#apparently uninitialised Jams have Time = '', but we can strip out anything without a ':' in it?
				
				#update Score
           			#Scorelines update precisely once per jam, at the start of the jam (when a new chapter happens). 
          	 		#Jammerlines update at the same time as a Scoreline (new jammers at start of each jam), but also at LJ, PJ, SP points during a jam
           			#Therefore ScoreJammerlines are precisely as frequent as Jammerlines, as each Scoreline also has a Jammerline
           	#Also Therefore: We can combine Chapter detection during a Bout (outside the bout, we need more Chapters for Skateout+Credits, and we might need 
           			# more than one bout in a DVD) with Scorelines
			 	#then it's a scoreline
				spuframes[0] += 1 #increment number of Scoreline frames
				outname[0] = "Scoreline" + str(boutnum)+ "_" + str(spuframes[0]) + ".png"
				self.makeScoreSubImage(outname[0],boutnum,i)
				#jendtime = next jam starttime , or the start of the Halftime or Fulltime chapters
				if Jam.Period == "1":
					jendtime = self.Bouts[boutnum].Timing.Halftime #end of first period time
				elif Jam.Period == "2":  
					jendtime = self.Bouts[boutnum].Timing.Fulltime #the latest the endtime can possibly be is the Fulltime for the bout
				if (i+1) < len(self.Bouts[boutnum].Jams): #then there is at least one more jam, so we should try that jams starttime
					if self.Bouts[boutnum].Jams[i+1].Period == Jam.Period: #if not, then halftime is in the way
						jendtime = self.Bouts[boutnum].Jams[i+1].StartTime 
					
				spumuxxmls[0] = self.AddSpumuxxml(spumuxxmls[0],Jam.StartTime,jendtime,outname[0],self.Bouts[boutnum].NeutralCol,self.Bouts[boutnum].Teams[0].TeamCol,self.Bouts[boutnum].Teams[1].TeamCol)

				for j in range(len(Jam.Events)):
					status = Status(Jam.Events[0:j+1])
					print status.Teams[0]
					print status.Teams[1]
					#update Jammer (always)
					spuframes[1] += 1 #increment number of Jammerline frames
					outname[1] = "Jammerline" + str(boutnum)+ "_" + str(spuframes[1]) + ".png"
					self.makeJammerSubImage(outname[1],boutnum,i,status)
					#get Endtime - it's either the next event time in the jam, or the start time of the next jam (or the end of the sequence)
					endtime = jendtime #default to the "end of jam" from above, as this is the furthest away the end can be
					if (j+1) < len(Jam.Events): #if there are more Events in this jam, use them instead
						endtime = Jam.Events[j+1].Time
					spumuxxmls[1] = self.AddSpumuxxml(spumuxxmls[1],status.Time,endtime,outname[1],self.Bouts[boutnum].NeutralCol,self.Bouts[boutnum].Teams[0].TeamCol,self.Bouts[boutnum].Teams[1].TeamCol)

					#update JammerScore
					# take latest Score and latest Jammer, and sum them, taking the start time of the later of the two (possibly do this as a second pass)	
					spuframes[2] += 1
					outname[2] = "JammerScoreline" + str(boutnum) + str(spuframes[2]) + ".png"
					#call convert(?) to smoosh the two pngs together into the third
					try:
						print "convert --composite " + outname[0] + " " + outname[1] + " " + outname[2]
						retcode = subprocess.call("convert -composite " + outname[0] + " " + outname[1] + " " + outname[2], shell=True)
						if retcode < 0:
							print >>sys.stderr, "Child was terminated by signal", -retcode
					except OSError as e:
						print >>sys.stderr, "Execution failed:", e

					spumuxxmls[2] = self.AddSpumuxxml(spumuxxmls[2],status.Time,endtime,outname[2],self.Bouts[boutnum].NeutralCol,self.Bouts[boutnum].Teams[0].TeamCol,self.Bouts[boutnum].Teams[1].TeamCol)
	
		#and close the xml streams
		spumuxxmls = [i+"</stream>\n</subpictures>\n" for i in spumuxxmls]

		#write spumuxxmls to files
		#and mux with spumux
		
		for i in range(len(spumuxxmls)):
			#write out config
			f = open("spumux.xml",'w')
			f.write(spumuxxmls[i])
			f.flush()
			f.close()
			#setup file & mux
			
			bits = self.Movie.split('.')
			
			outfile = bits[0] + str(i) + "." + bits[1]
			try:
				retcode = subprocess.call("spumux -s" + str(i) + " spumux.xml < " + self.Movie + " > " + outfile, shell=True)
				if retcode < 0:
					print >>sys.stderr, "Child was terminated by signal", -retcode
			except OSError as e:
				print >>sys.stderr, "Execution failed:", e
			#new input is old output
			
			self.Movie = outfile
			
		#At this point, we have a file called "bout012.mpg", which has bout.mpg muxed with the 3 subtitle files, hopefully
	
	def GenChapters(self):
		#need to handle ChapterLists by parsing out all of the Jams from each Bout in sequence, prepending Start,Skateout, inserting Halftime, appending FullTime, Awards
		#Credits are *not* a Chapter, they are a separately rendered title
		self.ChapList = []
		for b in self.Bouts:
			bname = ""
			if b.Name is None:
				bname = b.Name
			else: #construct bout name from Team names
				#this will always be too long (>10 chars)
				#contract using initialisms for team names
				i = lambda s : ''.join([w[0] for w in s.split(" ")]) 
				bname = i(b.Teams[0].TeamName) + " v " + i(b.Teams[1].TeamName)
			if ":" in b.Timing.Start: #we know it's got a valid timestamp cause it has colons in it
				self.ChapList.append([b.Timing.Start,bname])
			if ":" in b.Timing.Skateout:
				self.ChapList.append([b.Timing.Skateout,"Skateout"])
			for j in [j for j in b.Jams if (j.Period == "1") and (":" in j.StartTime)]:
				self.ChapList.append([j.StartTime,"P"+j.Period+"J"+j.Jam])
			#first period jams here
			if ":" in b.Timing.Halftime:
				self.ChapList.append([b.Timing.Halftime,"Halftime"])
			#second period jams here
			for j in [j for j in b.Jams if (j.Period == "2") and (":" in j.StartTime)]:
				self.ChapList.append([j.StartTime,"P"+j.Period+"J"+j.Jam])
			if ":" in b.Timing.Fulltime:
				self.ChapList.append([b.Timing.Fulltime,"Fulltime"])
			if ":" in b.Timing.Awards:
				self.ChapList.append([b.Timing.Awards,"Awards"])

	
	
	def RenderDVD(self):
		#this will write out the entire movie now, so execute last of all Serialisers
		#it needs the credits done, as well as the movie subtitles muxed, including the main menu + subtitles menu
		#we make the chapter menu vobs here, as it's convenient to generate the menus while we generate the dvdauthor xml
		
		#start by writing out the header for dvdauthor
		
		dvdauthxml = '<?xml version="1.0" encoding="UTF-8"?>' + "\n"
		dvdauthxml += '<dvdauthor dest="./tmpdir/">' + "\n"
		dvdauthxml += "<vmgm>\n"
		dvdauthxml += "<fpc>\n"
		dvdauthxml += "jump menu 1\n" #I think this goes to the first menu in the vmgm...
		dvdauthxml += "</fpc>\n"
		#define the main menu here in the vmgm
		dvdauthxml += "<menus>\n"
		dvdauthxml += "<pgc>\n"	
		self.makeMainMenu()
		#TODO - jump to titleset 1 title 1 (the movie) or titleset 1 menu 1 (first chapter menu)
		# or jump to menu 2 (in the vmgm), the subtitles menu
		dvdauthxml += "<button>jump titleset 1 title 1;</button>\n"
		dvdauthxml += "<button>jump titleset 1 menu 1;</button>\n"
		dvdauthxml += "<button>jump menu 2;</button>\n"
		dvdauthxml += '<vob file="mainmenu.mpg" />' + "\n"
		dvdauthxml += "</pgc>\n"
		dvdauthxml += '<pgc>' + "\n"
		self.makeSubtitlesMenu()
		#TODO - the subtitles menu (set subtitles to none,0,1,2 = working from references)
		dvdauthxml += "<button> g1 = 62;</button>\n"
		dvdauthxml += "<button> g1 = 64;</button>\n"
		dvdauthxml += "<button> g1 = 65;</button>\n"
		dvdauthxml += "<button> g1 = 66;</button>\n"
		dvdauthxml += '<vob file="subtitlesmenu.mpg" />' + "\n"
		dvdauthxml += "</pgc>\n"
		dvdauthxml += "</menus>\n"
		dvdauthxml += "</vmgm>\n"
		dvdauthxml += "<titleset>\n"
		dvdauthxml += "<menus>\n"
		#start making chapter menus
		#first, render our "static" generic background with ffmpeg - get silence.ogg from somewhere, and consider if input jpg is configurable
		subprocess.call("ffmpeg -loop 1 -shortest -y -i "+ self.ChpSrc +" -i /usr/share/devede/silence.ogg -target dvd menubackdrop.mpg",shell=True)	
		#then make lots of chapter menus with it
		
		self.GenChapters() #make our chapters
		l = len(self.ChapList)
		for i in range(0,l,8):
			block = self.ChapList[i:(i+8)]
			last = False
			first = False
			#make 3 subpictures (4x2 arrangement) - normal, highlight, select
			if i > (l-8) :  last = True #removes "Next" button
			if i == 0 : first = True #changes "Prev" button target to the main menu
			fname="chaptermenu"+str(i//8)
			self.makeMenuSubImage(fname,block,last)
			#make xml for spumux (this stuff is output to menuspumux.xml not the auth.xml)
			#remember to add autobutton detection, in row then column mode
			menuxml = "<subpictures><stream>\n"
			menuxml += '<spu force="yes" start="00:00:00:00" image="' + fname + 'n.png" select="' + fname + 's.png" highlight="' + fname + 'h.png" >' + "\n"
			menuxml += "</spu></stream></subpictures>\n"
			#and write out
			f = open("menuspumux.xml",'w')
			f.write(menuxml)
			f.flush()
			f.close()
			#and mux
			subprocess.call("spumux menuspumux.xml < menubackdrop.mpg > " + fname + ".mpg", shell=True)

			#outputthe xml for this menu for dvdauthor (this is where the actions come in)
	
			dvdauthxml += "<pgc>\n"
			for (chapter,index) in zip(block,range(i,i+8)):
				dvdauthxml += "<button>jump title 1 chapter" + str(index) + ";</button>\n"
				dvdauthxml += "<button>" 
				if not first: dvdauthxml +=  "jump menu " + str(i//8) #assuming menus start at 1
				else: dvdauthxml += "jump vmgm menu 1" #the main menu is jumped to by the first back button in the set of chapter menus
				dvdauthxml += ";</button>\n"
				if not last : dvdauthxml += "<button> jump menu" + str((i//8)+1) + ";</button>\n" #assuming menus start at 1 
				else: dvdauthxml += "<button>jump title 2</button>\n" # credits as a separate title
			dvdauthxml += '<vob file="'+fname+'.mpg" />' + "\n"
	
			dvdauthxml += "</pgc>\n"

		dvdauthxml += "</menus>\n"
		#now we've done the menus, setup the movie bit, with the list of chapters
		dvdauthxml += "<titles>\n"
		dvdauthxml += '<video format="pal" aspect="16:9" widescreen="nopanscan" />' + "\n"
		dvdauthxml += '<audio format="ac3" channels="2" />' + "\n"
		dvdauthxml += "<pgc>\n"
		#hopefully this pre will load the selected subtitle into the "subtitle" system register
		dvdauthxml += "<pre> s2 = g1; </pre>\n"
		dvdauthxml += '<vob file="'+self.Movie+'" chapters="' + ",".join([c[0] for c in self.ChapList]) + '" />' + "\n"
		dvdauthxml += "<post>jump title 2;</post>\n" #the credits are title 2
		dvdauthxml += "</pgc>\n"
		#and add the credits as title 2
		dvdauthxml += "<pgc>\n"
		dvdauthxml += '<vob file="credits.mpg" />' + "\n"
		dvdauthxml += "<post>jump vmgm menu 1;</post>\n" #jump back to the main menu, in the vmgm
		dvdauthxml += "</pgc>\n"
		dvdauthxml += "</titles>\n"
		dvdauthxml += "</titleset>\n"
		dvdauthxml += "</dvdauthor>\n"
		f = open("auth.xml",'w')
		#write out to auth.xml
		f.write(dvdauthxml)
		f.flush()
		f.close()
		#and make an ISO
		subprocess.call("dvdauthor -x auth.xml", shell=True)
		nameofdvd="DERBY DVD"
		subprocess.call('mkisofs -r -V "' + nameofdvd + '" -dvd-video -o "' + nameofdvd +'.iso" ' + pathtodvdtmpdir, shell=True)

def GT_Times(one,two):
	"""Compare two times in HH:MM:SS format, return True if one > two"""
	(H1,M1,SU1) = [int(i) for i in one.split(':')]
	(H2,M2,SU2) = [int(i) for i in two.split(':')]
	if H1 > H2 : return True
	if M1 > M2 : return True
	if SU1 > SU2 :return True
	return False


