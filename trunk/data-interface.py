#
# This is the Tkinter based interface code, which hopefully provides a front-end to dvd-chapter
#    This is the cut-down data entry only version

import Tkinter as Tk
import tkColorChooser as Tkc
import data_chapter as dc
import tkSimpleDialog as SD
import pickle

#consider a save function (can simply pickle the Bouts[] list, and a few other items for filenames etc)

#dialogs derived from tkSimpleDialog class that makes those non-interruptable dialogs that disable the main window when they're active
#hacked a bit to add a "data" field that you use to pass data to and from the dialogs

#NOTE : need to change all those neat vars that RadioButtons reference into Tk.StringVar s (and add get() methods to their readers, set() methods to writers). Stupid Tk.

#a shim to turn on "labels" on the top row of a row/column arrangement, using the .pack geometry manager
#use like:
# root = Tk.Frame(someplace)
#for i in range(rows):
#	(s,pack) = labelshim(root,"Column Label",i,Tk.LEFT)
#	widget = Tk.Entry(s, options)
#	widget.pack(side=pack)
def labelshim(root,l,count,pack):
	if count == 0:
		s = Tk.Frame(root)
		s.pack(side=pack)
		Tk.Label(s,text=l).pack(side=Tk.TOP)
		return (s,Tk.TOP)
	else:
		return (root,pack)

class TimingDialog(SD.Dialog):
	def body(self,master):
		topframe = Tk.Frame(master)
		topframe.pack()
		#do the ancillary info (Skateout, Halftime, Fulltime, Awards timing)
		f=Tk.Frame(topframe)
		f.pack()
		Tk.Label(f,text="Start Time HH:MM:SS.HU").pack(side=Tk.LEFT)
		self.StartEntry = Tk.Entry(f)
		self.StartEntry.pack(side=Tk.LEFT)
		f=Tk.Frame(topframe)
		f.pack()
		Tk.Label(f,text="Skateout Time").pack(side=Tk.LEFT)
		self.SkateoutEntry = Tk.Entry(f)
		self.SkateoutEntry.pack(side=Tk.LEFT)
		f=Tk.Frame(topframe)
		f.pack()
		Tk.Label(f,text="Half Time").pack(side=Tk.LEFT)
		self.HalftimeEntry = Tk.Entry(f)
		self.HalftimeEntry.pack(side=Tk.LEFT)
		f=Tk.Frame(topframe)
		f.pack()
		Tk.Label(f,text="Full Time").pack(side=Tk.LEFT)		
		self.FulltimeEntry = Tk.Entry(f)
		self.FulltimeEntry.pack(side=Tk.LEFT)
		f=Tk.Frame(topframe)
		f.pack()
		Tk.Label(f,text="Awards Time").pack(side=Tk.LEFT)		
		self.AwardsEntry = Tk.Entry(f)
		self.AwardsEntry.pack(side=Tk.LEFT)
		
		#and now get the existing info from the passed data:
		# in this case, this is the Timing  object for the bout
		if self.data is not None:	
			self.StartEntry.delete(0,Tk.END)
			self.StartEntry.insert(0,self.data.Start)
			self.SkateoutEntry.delete(0,Tk.END)
			self.SkateoutEntry.insert(0,self.data.Skateout)
			self.HalftimeEntry.delete(0,Tk.END)
			self.HalftimeEntry.insert(0,self.data.Halftime)
			self.FulltimeEntry.delete(0,Tk.END)
			self.FulltimeEntry.insert(0,self.data.Fulltime)
			self.AwardsEntry.delete(0,Tk.END)
			self.AwardsEntry.insert(0,self.data.Awards)
	
	def apply(self):
		self.data = dc.Timing()
		self.data.Start = self.StartEntry.get()
		self.data.Skateout = self.SkateoutEntry.get()
		self.data.Halftime = self.HalftimeEntry.get()
		self.data.Fulltime = self.FulltimeEntry.get()
		self.data.Awards = self.AwardsEntry.get()


class JamsDialog(SD.Dialog):
	def body(self,master):
		topframe = Tk.Frame(master)
		topframe.pack()
		#do some titles
		
		
		#and now do the Jams
		# this is all in a Canvas so we can have a nice vertical scrollbar
		c = Tk.Canvas(master)
		f = Tk.Frame(c,width=800)
		v = Tk.Scrollbar(master, orient="vertical",command=c.yview)
		#h = Tk.Scrollbar(master, orient="horizontal",command=c.xview) #workaround
		c.configure(yscrollcommand=v.set)
		#c.configure(xscrollcommand=h.set)
		v.pack(side=Tk.RIGHT,fill="y")
		#h.pack(side=Tk.BOTTOM,fill="x") #workaround for Tk Canvas not letting me set 
		c.pack(side=Tk.LEFT,fill="both",expand=True)
		c.create_window((4,4),window=f,anchor="nw",tags="f") 
 		def OFC(event):
			c.configure(scrollregion=c.bbox("all")) #set scrollregion (= internal size of canvas) to size of frame
			c.configure(width=c.bbox("all")[2]) #set width of canvas displayed to width of frame
		f.bind("<Configure>",OFC) #and call the above every time the frame reconfigures itself
		#adding the "width" setting there works on OSX to make the canvas change width appropriately with the frame

		jamframes = []
		interstitial = []		
		self.JamEntries = []
		
		jammernames = ([s.Skatename for s in self.data[1].Teams[0].Skaters],[s.Skatename for s in self.data[1].Teams[1].Skaters])
		for i in range(25): #initial set of rows for jams
			#So initial row is [Time HH:MM:SS.HH] [Period] [Jam] [Jammer 1] [Pivot 1] [Score 1] [Jammer 2] [Pivot 2] [Score 2] [Add Event]
			# and the [Add Event] adds an Event row under the current row
			self.JamEntries.append([])
			interstitial.append(Tk.Frame(f)) #needed to make Jam rows appear above their Event rows
			interstitial[-1].pack()
			jamframes.append(Tk.Frame(interstitial[-1])) #this is the containing frame for the initial row + event rows we dynamically add
			jamframes[i].pack()
			#add initial entry boxes:
			#make the Period, Jam, Jammer,Pivot boxes into dropdowns to reduce error - Tk.OptionMenu types
			#Period, Jam must be strings
			#Time
			(fr,pack) = labelshim(jamframes[i],"Time",0,Tk.LEFT) 
			self.JamEntries[i].append(Tk.Entry(fr))
			self.JamEntries[i][-1].pack(side=pack)
			#Period, Jam
			self.JamEntries[i].append(Tk.StringVar())
			(fr,pack) = labelshim(jamframes[i],"Per",0,Tk.LEFT)
			Tk.OptionMenu(fr,self.JamEntries[i][-1],"1","2").pack(side=pack)
			self.JamEntries[i].append(Tk.StringVar())
			(fr,pack) = labelshim(jamframes[i],"Jam",0,Tk.LEFT)
			Tk.OptionMenu(fr,self.JamEntries[i][-1],*[str(j) for j in range(1,30)]).pack(side=pack)			
			#Jammer1
			self.JamEntries[i].append(Tk.StringVar()) #Jammer is a string!!!
			(fr,pack) = labelshim(jamframes[i],"J1",0,Tk.LEFT)			
			Tk.OptionMenu(fr,self.JamEntries[i][-1],*(jammernames[0]) ).pack(side=pack) #jammernames[0] contains Team1's list of Skatenames
			#Pivot1
			self.JamEntries[i].append(Tk.StringVar()) #Pivot is a string!!!
			(fr,pack) = labelshim(jamframes[i],"P1",0,Tk.LEFT)			
			Tk.OptionMenu(fr,self.JamEntries[i][-1],*(jammernames[0]) ).pack(side=pack) #jammernames[0] contains Team1's list of Skatenames
			#Score 1
			(fr,pack) = labelshim(jamframes[i],"Score 1",0,Tk.LEFT)
			self.JamEntries[i].append(Tk.Entry(fr))
			self.JamEntries[i][-1].pack(side=pack)
			#Jammer2
			self.JamEntries[i].append(Tk.StringVar()) #Jammer is a string!!!
			(fr,pack) = labelshim(jamframes[i],"J2",0,Tk.LEFT)
			Tk.OptionMenu(fr,self.JamEntries[i][-1],*(jammernames[1]) ).pack(side=pack) #jammernames[1] contains Team2's list of Skatenames
			#Pivot2
			self.JamEntries[i].append(Tk.StringVar()) #Pivot is a string!!!
			(fr,pack) = labelshim(jamframes[i],"P2",0,Tk.LEFT)			
			Tk.OptionMenu(fr,self.JamEntries[i][-1],*(jammernames[1]) ).pack(side=pack) #jammernames[1] contains Team2's list of Skatenames
			#Score 2
			(fr,pack) = labelshim(jamframes[i],"Score 2",0,Tk.LEFT)			
			self.JamEntries[i].append(Tk.Entry(fr))
			self.JamEntries[i][-1].pack(side=pack)
			#There is always at least one Event row (since each jam has an initial state that may include continuing Power jams from last bout
			#ideally, this first Event row would be magically linked with the Start Time from the same Jam row, as it must use same value
			(fr,pack) = labelshim(interstitial[-1],"Event Data",0,Tk.TOP)
			self._add_eventrow(fr,self.JamEntries[i])
			#and add the button for events (see below for callback)
			eventbut = Tk.Button(jamframes[i],text="Add Event Row",command=self.add_eventrow(interstitial[-1],self.JamEntries[i]))
			eventbut.pack(side=Tk.RIGHT)
		#need to be able to add more jam rows
		Tk.Button(f,text="Add more jams",command=self.add_jams(f).pack(side=Tk.BOTTOM) #pack at bottom so always lowest thing

		#now fill in info from data[0] (data[1] is the Bout structure and should be rigourously used READONLY for lookup)
		for (jam,jentry,jframe) in zip(self.data[0],self.JamEntries,interstitial):
			jentry[0].insert(0,jam.Time)
			jentry[1].set(jam.Period)
			jentry[2].set(jam.Jam)
			jentry[3].set(jam.Jammers[0]) #etc
			jentry[4].set(jam.Pivots[0])
			jentry[5].insert(0,jam.Score[0])
			jentry[6].set(jam.Jammers[1]) #etc
			jentry[7].set(jam.Pivots[1])
			jentry[8].insert(0,jam.Score[1])
			jentry[-1][0].insert(0,jam.Events[0].Time)
			jentry[-1][1].set(jam.Events[0].Team)
			jentry[-1][2].set(jam.Events[0].Type)
			for event in jam.Events[1:]:
				#identify type, unpack
				self._add_eventrow(jframe,jentry)
				#this row is always the last one, so
				jentry[-1][0].insert(0,event.Time) #the first entry box is the Time
				jentry[-1][1].set(event.Team) #the second entry box is the Team ID
				jentry[-1][2].set(event.Type) #this is the internal value of the radio button selector 

	def add_jams(self,f):
		return lambda: self._add_jams(f)
	def _add_jams(self,f):
		#what this does is to to precisely what we did to add the first 25 jams, but for one more jam...
	
	def add_eventrow(self,frame,entry):
		return lambda: self._add_eventrow(frame,entry)
		
	def _add_eventrow(self,frame,entry):
		row = []
		f = Tk.Frame(frame)
		f.pack()
		row.append(Tk.Entry(f)) #TIME
		row[-1].pack(side=Tk.LEFT)	
		row.append(Tk.IntVar()) #Team number, using Option Menu to prevent need for validation
		row[-1].set(1) #say Team 1 is the default (we should pick one, afterall)
		Tk.OptionMenu(f,row[-1],1,2).pack(side=Tk.LEFT)				
		row.append(Tk.IntVar())  #Radio Buttons for Event type, default value "NO PJ" for starting jam event
		row[-1].set(dc.POWEREND) 
		decode = ("Lead Jammer","Power Jam Starts", "PJ Ends/No PJ", "Star Pass")
		for i in range(dc.STAR+1):
			t = Tk.Radiobutton(f,text=decode[i],variable=row[2],value=i).pack(side=Tk.LEFT)
		entry.append(row)

	def apply(self):
		#self.data[1] is the Bout structure, don't clobber it!
		self.data[0] = []
		for jam_entry in self.JamEntries:
			j = dc.Jam()
			j.Time = jam_entry[0].get()
			j.Period = jam_entry[1].get()
			j.Jam = jam_entry[2].get()
 			#and so on
 			j.Jammers.append(jam_entry[3].get())
 			j.Pivots.append(jam_entry[4].get())
 			j.Score.append(jam_entry[5].get())
 			j.Jammers.append(jam_entry[6].get())
 			j.Pivots.append(jam_entry[7].get())
 			j.Score.append(jam_entry[8].get())
			j.Events = []
			#then do events!
			for event_entry in jam_entry[9:]:
				e = dc.Event()
				e.Time = event_entry[0].get()
				e.Team = event_entry[1].get()
				e.Type = event_entry[2].get()
				j.Events.append(e)
				
			self.data[0].append(j)

class OfficialsDialog(SD.Dialog):
	def body(self,master):
		topframe = Tk.Frame(master)
		topframe.pack()
		#does some titles
		
		self.OfficialEntries = []
		for i in range(8):
			s = Tk.Frame(master)
			s.pack()
			self.OfficialEntries.append([])
			namenum = ("Official Name","Number")
			for j in range(2):  #name and number fields
				(fr,pack) = labelshim(s,namenum[j],i,Tk.LEFT)				
				ss = Tk.Entry(fr)
				ss.pack(side=pack)
				self.OfficialEntries[i].append(ss)
			#and radio buttons for roles
			(fr,pack) = labelshim(s,"Roles",i,Tk.LEFT)				
			self.OfficialEntries[i].append(Tk.IntVar())
			self.OfficialEntries[i][-1].set(dc.JAM)
			self.OfficialEntries[i].append([])
			decode = ("Head Ref","Jam Ref","IPR","OPR")
			tmp = Tk.Frame(fr) #need this to preserve arrangement of buttons using labelshim (otherwise they'd end up stacked vertically)
			tmp.pack(side=pack)
			for j in range(dc.OPR+1):
				r = Tk.Radiobutton(tmp,text=decode[j],variable=self.OfficialEntries[i][2],value=j)
				r.pack(side=Tk.LEFT)
		
		#and unpack data if given it
		if self.data is not None:
			for (s,o) in zip(self.data,self.OfficialEntries):
				for i in range(2):
					o[i].delete(0,Tk.END)
				o[0].insert(0,s.Name)
				o[1].insert(0,s.Number)
				#and set radio buttons
				o[2].set(s.Role)
				
	#def validate(self):
	
	def apply(self):
		#if data is None:
		self.data = []
		for official_entry in self.OfficialEntries:
			if official_entry[0].get() == "" : break #end of list signalled by blank name
			s = dc.Official()
			s.Name = official_entry[0].get()
			s.Number = official_entry[1].get()
			s.Role = official_entry[2].get()
			self.data.append(s)

class TeamNDialog(SD.Dialog): #we use the data constructor option to pass an existing Team structure if one is available for the Team 
	def colourcallback(self): 
		#call a colour picker dialog and then get the resultant colour (and make the button that called us change to that colour)
		(colourtuple,rgbcol) = Tkc.askcolor(self.TeamHex)
		self.TeamCol = colourtuple
		self.TeamHex = rgbcol
		#self.TeamColButton.config(bg = rgbcol) #can't get this to work and set the button colour 
		
	def body(self,master):
		#where we stick our custom body (master is the frame we're given)
		topframe = Tk.Frame(master)
		topframe.pack()
		(fr,pack) = labelshim(topframe,"League Name",0,Tk.LEFT)				
		self.LeagueEntry = Tk.Entry(fr)
		self.LeagueEntry.pack(side=pack)
		(fr,pack) = labelshim(topframe,"Team Name",0,Tk.LEFT)		
		self.TeamEntry = Tk.Entry(fr)
		self.TeamEntry.pack(side=pack)
		self.TeamCol = (255,0,0)
		self.TeamHex = "#ffffff"
		self.TeamColButton = Tk.Button(topframe,text="Team Colour",command=self.colourcallback) #colourpicker
		self.TeamColButton.pack(side=Tk.LEFT)
		self.SkaterEntries = []
		for i in range(24):
			s = Tk.Frame(master)
			s.pack()
			namenum = ("Skatename","Number")			
			self.SkaterEntries.append([])
			for j in range(2): #the Skatename and Skate number fields
				(fr,pack) = labelshim(s,namenum[j],i,Tk.LEFT)				
				ss = Tk.Entry(fr)
				ss.pack(side=pack)
				self.SkaterEntries[i].append(ss)
			#and make radio button array (fairly sure that the "set" is based on the common parent (s) )
			self.SkaterEntries[i].append(Tk.IntVar())
			self.SkaterEntries[i][-1].set(dc.SKATER)
			decode = ("Captain","Vice-Captain","Skater","Bench","Line-up")
			(fr,pack) = labelshim(s,"Roles",i,Tk.LEFT)
			tmp = Tk.Frame(fr) #make things work with labelshim (else the labelled row would have vertical buttons!)
			tmp.pack(side=pack)			
			for j in range(dc.LINEUP+1):
				t=Tk.Radiobutton(tmp, text=decode[j],variable=self.SkaterEntries[i][2],value=j)
				t.pack(side=Tk.LEFT)

		#and unpack data if we were given it
		if self.data is not None:
			self.LeagueEntry.delete(0,Tk.END)
			self.LeagueEntry.insert(0,self.data.LeagueName)
			self.TeamEntry.delete(0,Tk.END)
			self.TeamEntry.insert(0,self.data.TeamName)
			self.TeamCol = self.data.TeamCol
			self.TeamHex = '#{0:02x}{1:02x}{2:02x}'.format(*self.TeamCol)
			for (s,se) in zip(self.data.Skaters,self.SkaterEntries):
				for i in range(2):
					se[i].delete(0,Tk.END)
				se[0].insert(0,s.Skatename)
				se[1].insert(0,s.Number)
				#and set radio buttons however we do that
				se[2].set(s.Role)				


	#def validate(self):
	#	#optional method for validating input when apply is called	
	def apply(self):
		#where we apply the results on "Okay" being clicked

		#if we don't have an existing Team, make one		
		self.data = dc.Team()
		
		#we probably want to do text field length validation on these
		self.data.LeagueName = self.LeagueEntry.get()		
		self.data.TeamName = self.TeamEntry.get()
		self.data.TeamCol = self.TeamCol
		self.data.Skaters = []
		for skate_entry in self.SkaterEntries:
			if skate_entry[0] == "" : break #detect blank line, which means end of list
			s = dc.Skater()
			s.Skatename = skate_entry[0].get()
			s.Number = skate_entry[1].get()
			s.Role = skate_entry[2].get() #reading the linked button state variable
			self.data.Skaters.append(s)				

class DerbyTK(object):
	#constructs for currying the callbacks for buttons appropriately
	def TeamNWindow(self,teamnum):
		return lambda : self._TeamNWindow(teamnum)

	def _TeamNWindow(self,teamnum):
		"""Get the information for Team N with a dialog box"""
		#This is a grid-layout dialog, with
		#    [League Name] [Team Name]
		# and then 24 of
		#    [Skate name] [number] Role:Capt[x] Vice-capt[x] Bench[x] Coach[x]
		# any of the fields can be blank (but the first field with a blank skate name signals end of list)
		boutnum = teamnum/2 
		#done with SD.Dialog class, need to subclass		
		if len(self.Bouts) < (boutnum+1): #then we've not made this Bout or its fields yet  
			self.Bouts.append(dc.Bout())
			self.Bouts[boutnum].Teams = [dc.Team(),dc.Team()]
		#create dialog and fill with existing data on that team (mapping through the Bout list)
		d = TeamNDialog(self.root,title="Team "+str(teamnum),data=self.Bouts[boutnum].Teams[teamnum-2*boutnum])
		#and refresh the team data from the new Dialog data
		self.Bouts[boutnum].Teams[teamnum-2*boutnum] = d.data		

	def OfficialsWindow(self,boutnum):
		return lambda: self._OfficialsWindow(boutnum)
	
	def _OfficialsWindow(self,boutnum):
		"""Get the information for the Skating Officials with a dialog box"""
		#This is a grid-layout dialog, with 14 (just to be safe!) of 
		#     [Skating official] [number] Role:Head[x] Jam[x] IPR[x] OPR[x]
		# any of the fields can be blank (but the first field with a blank official name signals end of list)
		# this also needs to handle being called more than once for multiple bouts. Possibly need an internal "Bout number" field
		if len(self.Bouts) < (boutnum+1): #then we've not made this Bout or its fields yet , so make it 
			self.Bouts.append(dc.Bout())
			self.Bouts[boutnum].Teams = [dc.Team(),dc.Team()]
		d = OfficialsDialog(self.root,title="Officials Bout "+str(boutnum+1), data=self.Bouts[boutnum].Officials)
		self.Bouts[boutnum].Officials = d.data #do I actually need this, given shallow copy semantics?

	def JamsWindow(self,boutnum):
		return lambda: self._JamsWindow(boutnum)

	def _JamsWindow(self,boutnum):
		"""Get the Jam by Jam data (needs to be run *after* get Teams, get Officials), with a dialog box"""
		# This is a grid-layout dialog, with 30 of
		#   [Time HH:MM:SS.HH] [Bout] [Period] [Jam] [Team1] [Team1 Jammer] [Team1 Pivot] [Team1Score] [Team2] [Team2 Jammer] [Team2 Pivot] [Team2Score] {ADD EVENTS}
	 	#   where {ADD EVENTS} spawns a dialog to collect status changes during the jam (Lead Jammer, Power Jam, Star Pass)
		# followed by 
		#   {Add more lines}
		# which adds another 10 lines of entries to the dialog
		# The parser assumes that if part of an entry is empty, then the previous value should be continued
		# (but if the Time is empty, then this signals the end of the list)
		# Pivot data is mostly used to determine the Jammer after a star pass.
		#
		#put in a check for if there are actual team entries, to prevent Jam entry before Team entry
		#
		d = JamsDialog(self.root, title="Jams: Bout " + str(boutnum+1), data=[self.Bouts[boutnum].Jams, self.Bouts[boutnum]])
		self.Bouts[boutnum].Jams = d.data[0] #does shallow copy semantics make this irrelevant?

	def TimingWindow(self,boutnum):
		return lambda: self._TimingWindow(boutnum)
	
	def _TimingWindow(self,boutnum):
		"""Get the Timing data for Skateout, Halftime, Fulltime, Awards for the bout"""
		# This is a grid-layout dialog, with:
		# [Time HH:MM:SS.HH] [Skateout]
		# [Time HH:MM:SS.HH] [Halftime]
		# [Time HH:MM:SS.HH] [Fulltime]
		# [Time HH:MM:SS.HH] [Awards]
		if len(self.Bouts) < (boutnum+1): #then we've not made this Bout or its fields yet , so make it 
			self.Bouts.append(dc.Bout())
			self.Bouts[boutnum].Teams = [dc.Team(),dc.Team()]		
		d = TimingDialog(self.root, title="Misc. Timing: Bout " + str(boutnum+1), data=self.Bouts[boutnum].Timing) #
		self.Bouts[boutnum].Timing = d.data #shallow copies might make this irrelevant

	def boutbuttonarray(self):
		"""Make an array of buttons for adding a new bout's info (Teams,Officials,Jams)"""
		boutnum = self._b
		self.buttonframes.append(Tk.Frame(self.buttonmasterframe)) #the default button frame
		self.buttonframes[boutnum].pack(side=Tk.TOP)
		self.buttonarray.append([Tk.Button(self.buttonframes[-1]) for i in range(5)])
		self.buttonarray[boutnum][0].configure(text="Add Team "+str(boutnum*2+1), command=self.TeamNWindow(boutnum*2))
		self.buttonarray[boutnum][0].pack(side=Tk.LEFT)
		#todo: replace binds with command= (as optimised for button press events)
		self.buttonarray[boutnum][1].configure(text="Add Team "+str(boutnum*2+2), command=self.TeamNWindow(boutnum*2+1))
		self.buttonarray[boutnum][1].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][2].configure(text="Add Officials bout "+str(boutnum+1), command=self.OfficialsWindow(boutnum))
		self.buttonarray[boutnum][2].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][3].configure(text="Enter Jam info bout "+str(boutnum+1), command=self.JamsWindow(boutnum))
		self.buttonarray[boutnum][3].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][4].configure(text="Enter ancillary timing for bout " +str(boutnum+1), command=self.TimingWindow(boutnum))
		self.buttonarray[boutnum][4].pack(side=Tk.RIGHT)
		self._b += 1
	
	def save(self):
		pickle.dump(self.Bouts,open("bouts.save","wb"))
		#Bug here, kinda - since BR isn't built until RenderSubs, we don't save the text entry boxes on main window most of the time


	def load(self):
		self.Bouts = pickle.load(open("bouts.save","rb"))
		#should really make enough entry fields to enter all the bouts that we've loaded

	def __init__(self):
		"""The Main Tkinter window interface"""
		#need to get Skateout, (Timeouts?), Halftime, Fulltime, Awards times for the bouts too
		# This is a packed dialog with:
		#   [Movie source] [Main menus source] [Chapter menus source] [Credits music source] 
		#   {Enter Team 1} {Enter Team 2} {Enter Officials} {Enter Jam info} {Enter ancillary timing}
		#   {Add another bout} 
		# (which adds a row of {Enter Team 2N-1} {Enter Team 2N} {Enter Officials}? {Enter Jam info}? buttons
		#   {Render Subs} {Render Credits} {Render DVD} 
		# which muxes the subtitle stream, generates chapter menus and credits crawls, then authors the DVD structure + makes an ISO
		#
	 	# (In a future version, we will have an "Import from Rinxter" button to use the API to pull all the info except Chapter times from Rinxter instance)	
		self.Bouts = []
		self.Extracredits=["Movie generated by derby-dvd-tool","Released under CC:BY 3.0","Sam Skipsey"]
		#create root TK instance
		self.root = Tk.Tk()
		inputframe = Tk.Frame(self.root) #frame that contains the text input fields
		inputframe.pack()
		f=Tk.Frame(inputframe)
		f.pack(side=Tk.LEFT)
		
		self.buttonmasterframe = Tk.Frame(self.root) #master frame for the team input frames to faciliate adding rows
		self.buttonmasterframe.pack()
		self.buttonframes=[]
		self.buttonarray=[] #arrays of buttons for frames
		self._b = 0
		self.boutbuttonarray() #make the default button array (for "Bout 0", counting pythonically)
		
		frame = Tk.Frame(self.root)
		frame.pack()
		Tk.Button(frame,text="New bout row", command=self.boutbuttonarray).pack(side=Tk.LEFT)
		Tk.Button(frame,text="Save", command=self.save).pack(side=Tk.RIGHT)
		Tk.Button(frame,text="Load", command=self.load).pack(side=Tk.RIGHT)

		self.root.mainloop()

DerbyTK()
