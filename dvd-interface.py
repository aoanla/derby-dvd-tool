#
# This is the Tkinter based interface code, which hopefully provides a front-end to dvd-chapter
#

import Tkinter as tk
import dvd-chapter as dc
import tkSimpleDialog as SD

#consider a save function (can simply pickle the Bouts[] list, and a few other items for filenames etc)

#dialogs derived from tkSimpleDialog class that makes those non-interruptable dialogs that disable the main window when they're active
#hacked a bit to add a "data" field that you use to pass data to and from the dialogs

#NOTE : need to change all those neat vars that RadioButtons reference into Tk.StringVar s (and add get() methods to their readers, set() methods to writers). Stupid Tk.

class TimingDialog(SD.Dialog):
	def body(self,master):
		topframe = Tk.Frame(master)
		topframe.pack()
		#do the ancillary info (Skateout, Halftime, Fulltime, Awards timing)
		self.StartEntry = tk.Entry(topframe)
		self.StartEntry.pack()
		self.SkateoutEntry = tk.Entry(topframe)
		self.SkateoutEntry.pack()
		self.HalftimeEntry = tk.Entry(topframe)
		self.HalftimeEntry.pack()
		self.FulltimeEntry = tk.Entry(topframe)
		self.FulltimeEntry.pack()
		self.AwardsEntry = tk.Entry(topframe)
		self.AwardsEntry.pack()
		
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
		jamframes = []		
		self.JamEntries = []
		for i in range(25): #initial set of rows for jams
			#So initial row is [Time HH:MM:SS.HH] [Period] [Jam] [Jammer 1] [Pivot 1] [Score 1] [Jammer 2] [Pivot 2] [Score 2] [Add Event]
			# and the [Add Event] adds an Event row under the current row
			self.JamEntries.append([])
			jamframes.append(Tk.Frame(topframe)) #this is the containing frame for the initial row + event rows we dynamically add
			jamframes[i].pack()
			#add initial entry boxes:
			for j in range(7):
				#make the Period, Jam, Jammer,Pivot boxes into dropdowns to reduce error - Tk.OptionMenu types
				self.JamEntries[i].append(Tk.Entry(jamframes[i]))
				self.JamEntries[i][j].pack(side=Tk.LEFT)
				#option menu messing
				self.JamEntries[i]=Tk.IntVar( #really? need to know if I can return *numbers* and display *names* for options
				Tk.OptionMenu(jamframes[i],self.data[1].Team1.Skaters[0],*(self.data[1].Team1.Skaters) ) #data[1] is the Bout struct for this bout
			
			#and add the button for events (see below for callback)
			eventbut = Tk.Button(self.JamFrames[i],text="Add Event Row",command=self.add_eventrow(jamframes[i],self.JamEntries[i])
			eventbut.pack(Tk.RIGHT)

		#now fill in info from data[0] (data[1] is the Bout structure and should be rigourously used READONLY for lookup)
		for (jam,jentry,jframe) in zip(self.data[0],self.JamEntries,jamframes):
			jentry[0] = jam.Time
			jentry[1] = jam.Jammer1 #etc
			
			for event in jam:
				#identify type, unpack
				self._add_eventrow(jframe,jentry)
				#this row is always the last one, so
				jentry[-1][0].insert(0,event.Time) #the first entry box is the Time
				jentry[-1][1].intsert(0,event.Team) #the second entry box is the Team ID
				jentry[-1][2].set(event.Type) #this is the internal value of the radio button selector 

	def add_eventrow(self,frame,entry):
		return lambda: self._add_eventrow(frame,entry)
		
	def _add_eventrow(self,frame,entry):
		row = []
		f = Tk.Frame(frame)
		f.pack()
		row.append(Tk.Entry(f)) #TIME
		row.pack(side=Tk.LEFT)
		row.append(Tk.Entry(f)) #Team number (validate this as a number on submit, or even on entry...)
		row.pack(side=Tk.LEFT)		
		row.append(Tk.IntVar(dc.LEAD))  #Radio Buttons for Event type, default value Lead Jammer call
		decode = ("Lead Jammer","Power Jam Starts", "Power Jam Ends", "Star Pass")
		for i in range(dc.STAR+1):
			t = Tk.Radiobutton(f,text=decode[i],variable=row[2],value=i).pack(side=Tk.RIGHT)
		entry.append(row)

	def apply(self):
		#self.data[1] is the Bout structure, don't clobber it!
		self.data[0] = []
		for jam_entry in self.JamEntries:
			j = dc.Jam()
			j.Time = jam_entry[0].get()
 			#and so on
			j.
			#then do events!
			for event_entry in jam_entry[7:]:
				e = dc.Event()
				e.Time = event_entry[0].get()
				e.Team = event_entry[1].get()
				e.Type = event_entry[2].get()
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
			for j in range(2):  #name and number fields
				ss = Tk.Entry(s)
				ss.pack(side=Tk.LEFT)
				self.OfficialEntries[i].append(ss)
			#and radio buttons for roles
			self.OfficialEntries.append(Tk.IntVar(dc.JAM))
			self.OfficialEntries.append([])
			decode = ("Head Ref","Jam Ref","IPR","OPR")
			for j in range(dc.OPR+1):
				r = Tk.Radiobutton(s,text=decode[j],variable=self.SkaterEntries[i][2],value=j)
				r.pack(side=Tk.RIGHT)
		
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
			if official_entry[0].get() = "" then break #end of list signalled by blank name
			s = dc.Official()
			s.Name = official_entry[0].get()
			s.Number = official_entry[1].get()
			s.Role = official_entry[2].get()
			self.data.append(s)

class TeamNDialog(SD.Dialog): #we use the data constructor option to pass an existing Team structure if one is available for the Team 
	def body(self,master):
		#where we stick our custom body (master is the frame we're given)
		topframe = Tk.Frame(master)
		topframe.pack()
		Tk.Label(topframe,text="League").pack(side=Tk.LEFT)
		self.LeagueEntry = Tk.Entry(topframe)
		self.LeagueEntry.pack(side=Tk.LEFT)
		self.SkaterEntries = []
		for i in range(24):
			s = Tk.Frame(master)
			s.pack()
			self.SkaterEntries.append([])
			for j in range(2): #the Skatename and Skate number fields
				ss = Tk.Entry(s)
				ss.pack(side=Tk.LEFT)
				self.SkaterEntries[i].append(ss)
			#and make radio button array (fairly sure that the "set" is based on the common parent (s) )
			self.SkaterEntries[i].append(Tk.IntVar(dc.SKATER))
			decode = ("Captain","Vice-Captain","Skater","Bench","Line-up")			
			for j in range(dc.LINEUP+1):
				t=(Tk.Radiobutton(s, text=decode[j],variable=self.SkaterEntries[i][2],value=j)
				t.pack(side=Tk.RIGHT)

		#and unpack data if we were given it
		if self.data is not None:
			self.LeagueEntry.delete(0,Tk.END)
			self.LeagueEntry.insert(0,data.LeagueName)
			
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
		if data is None:
			self.data = dc.Team()
		
		#we probably want to do text field length validation on these
		self.data.LeagueName = self.LeagueEntry.get()		
		self.data.TeamName = self.TeamEntry.get()
		self.data.Skaters = []
		for skate_entry in self.SkaterEntries:
			if skate_entry[0] == "" then break #detect blank line, which means end of list
			s = dc.Skater()
			s.Skatename = skate_entry[0].get()
			s.Number = skate_entry[1].get()
			s.Role = skate_entry[2].get() #reading the linked button state variable
			self.data.Skaters.append(s)				

class DerbyTK(object):
	#constructs for currying the callbacks for buttons appropriately
	def TeamNWindow(self,teamnum):
		return lambda : _TeamNWindow(teamnum)

	def _TeamNWindow(self,teamnum):
		"""Get the information for Team N with a dialog box"""
		#This is a grid-layout dialog, with
		#    [League Name] [Team Name]
		# and then 24 of
		#    [Skate name] [number] Role:Capt[x] Vice-capt[x] Bench[x] Coach[x]
		# any of the fields can be blank (but the first field with a blank skate name signals end of list)
		boutnum = teamnum/2 
		#done with SD.Dialog class, need to subclass		
		if len(self.Bouts < (boutnum+1): #then we've not made this Bout or its fields yet  
			self.Bouts.append(dc.Bout())
			self.Bouts[boutnum].Teams = (dc.Team(),dc.Team())
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
		d = TimingDialog(self.root, title="Misc. Timing: Bout " + str(boutnum+1), data=self.Bouts.Timing)
		self.Bouts[boutnum].Timing = d.data #shallow copies might make this irrelevant

	def boutbuttonarray(self):
		"""Make an array of buttons for adding a new bout's info (Teams,Officials,Jams)"""
		boutnum = self._b
		self.buttonframe.append(Tk.Frame(self.buttonmasterframe)) #the default button frame
		self.buttonframe[boutnum].pack()
		self.buttonarray.append([Tk.Button(self.buttonframe[0]) for i in range(4)])
		self.buttonarray[boutnum][0].configure(text="Add Team "+str(boutnum*2+1), command=self.TeamNWindow(boutnum*2))
		self.buttonarray[boutnum][0].pack(side=Tk.LEFT)
		#todo: replace binds with command= (as optimised for button press events)
		self.buttonarray[boutnum][1].configure(text="Add Team "+str(boutnum*2+2), command=self.TeamNWindow(boutnum*2+1))
		self.buttonarray[boutnum][1].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][2].configure(text="Add Officials bout "+str(boutnum+1)), command=self.OfficialsWindow(boutnum))
		self.buttonarray[boutnum][2].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][3].configure(text="Enter Jam info bout "+str(boutnum+1), command=self.JamsWindow(boutnum))
		self.buttonarray[boutnum][3].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][4].configure(text="Enter ancillary timing for bout " +str(boutnum+1), command=self.TimingWindow(boutnum))
		self.buttonarray[boutnum][4].pack(side=Tk.RIGHT)
		self._b += 1

	def RenderDVD(self):
		"""Render the DVD, using the functions in dvd-chapter, imported as dc"""

	def mainWindow(self):
		"""The Main Tkinter window interface"""
		#need to get Skateout, (Timeouts?), Halftime, Fulltime, Awards times for the bouts too
		# This is a packed dialog with:
		#   [Movie source] [Main menus source] [Chapter menus source] [Credits music source] 
		#   {Enter Team 1} {Enter Team 2} {Enter Officials} {Enter Jam info} {Enter ancillary timing}
		#   {Add another bout} 
		# (which adds a row of {Enter Team 2N-1} {Enter Team 2N} {Enter Officials}? {Enter Jam info}? buttons
		#   {Render DVD} 
		# which muxes the subtitle stream, generates chapter menus and credits crawls, then authors the DVD structure + makes an ISO
		#
	 	# (In a future version, we will have an "Import from Rinxter" button to use the API to pull all the info except Chapter times from Rinxter instance)
	
		#create root TK instance
		self.root = Tk.TK()
		self.inputframe = Tk.Frame(self.root) #frame that contains the text input fields
		self.inputframe.pack()
		
		self.buttonmasterframe = Tk.Frame(self.root) #master frame for the team input frames to faciliate adding rows
		self.buttonmasterframe.pack()
		self.buttonframes=[]
		self.buttonarray=[] #arrays of buttons for frames
		self._b = 0
		self.boutbuttonarray() #make the default button array (for "Bout 0", counting pythonically)
		
		self.lastframe = Tk.Frame(self.root)
		self.lastframe.pack()
		self.nextboutbutton = Tk.Button(self.lastframe)
		self.nextboutbutton.pack(side=Tk.LEFT)
		self.nextboutbutton.bind("<Button-1>",self.boutbuttonarray)
		self.renderdvdbutton = Tk.Button(self.lastframe)
		self.renderdvdbutton.pack(side=Tk.RIGHT)
		self.renderdvdbutton.binf("<Button-1>",self.RenderDVD)

		self.root.mainloop()
