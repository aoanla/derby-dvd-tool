#
# This is the Tkinter based interface code, which hopefully provides a front-end to dvd-chapter
#

import Tkinter as tk
import dvd-chapter as dc
import tkSimpleDialog as SD

class TeamNDialog(SD.Dialog): #we use the data constructor option to pass an existing Team structure if one is available for the Team 
	def body(self,master):
		#where we stick our custom body (master is the frame we're given)
		topframe = Tk.Frame(master)
		topframe.pack()
		Tk.Label(topframe,text="League").pack(side=Tk.LEFT)
		self.LeagueEntry = Tk.Entry(topframe)
		self.LeagueEntry.pack(side=Tk.LEFT)


		#and unpack data if we were given it
		if self.data is not None:
			self.LeagueEntry.delete(0,Tk.END)
			self.LeagueEntry(0,data.LeagueName)
 
	#def validate(self):
	#	#optional method for validating input when apply is called	
	def apply(self):
		#where we apply the results on "Okay" being clicked

		#if we don't have an existing Team, make one		
		if data is not None:
			self.data = dc.Team()
		
		#we probably want to do text field length validation on these
		self.data.LeagueName = self.LeagueEntry.get()		
		self.data.TeamName = self.TeamEntry.get()
		for skate_entry in self.SkaterEntries:
			if skate_entry[0] == "" then exit loop #detect blank line, which means end of list
			s = dc.Skater()
			s.Skatename = skate_entry[0].get()
			s.Number = skate_entry[1].get()
			s.Role = #however we read radio buttons
			self.data.Skaters.append(s)				
		return self.data

class DerbyTK(object):
	#constructs for currying the callbacks for buttons appropriately
	def TeamNWindow(self,teamnum):
		return lambda : _TeamNWindow(self,teamnum)

	def _TeamNWindow(self,teamnum):
		"""Get the information for Team N with a dialog box"""
		#This is a grid-layout dialog, with
		#    [League Name] [Team Name]
		# and then 24 of
		#    [Skate name] [number] Role:Capt[x] Vice-capt[x] Bench[x] Coach[x]
		# any of the fields can be blank (but the first field with a blank skate name signals end of list)
		#done with SD.Dialog class, need to subclass		
		
			
	def OfficialsWindow(self,boutnum):
		return lambda: self._OfficialsWindow(self,boutnum)
	
	def _OfficialsWindow(self,boutnum):
		"""Get the information for the Skating Officials with a dialog box"""
		#This is a grid-layout dialog, with 14 (just to be safe!) of 
		#     [Skating official] [number] Role:Head[x] Jam[x] IPR[x] OPR[x]
		# any of the fields can be blank (but the first field with a blank official name signals end of list)
		# this also needs to handle being called more than once for multiple bouts. Possibly need an internal "Bout number" field
	def JamsWindow(self,boutnum):
		return lambda: self._JamsWindow(self,boutnum)

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

	def boutbuttonarray(self):
		"""Make an array of buttons for adding a new bout's info (Teams,Officials,Jams)"""
		boutnum = self._b
		self.buttonframe.append(Tk.Frame(self.buttonmasterframe)) #the default button frame
		self.buttonframe[boutnum].pack()
		self.buttonarray.append([Tk.Button(self.buttonframe[0]) for i in range(4)])
		self.buttonarray[boutnum][0].configure(text="Add Team "+str(boutnum*2+1))
		self.buttonarray[boutnum][0].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][0].bind("<Button-1">,self.TeamNWindow(boutnum*2)) #numbering teams from 0 internally as is pythonic
		self.buttonarray[boutnum][1].configure(text="Add Team "+str(boutnum*2+2))
		self.buttonarray[boutnum][1].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][1].bind("<Button-1>",self.TeamNWindow(boutnum*2+1))
		self.buttonarray[boutnum][2].configure(text="Add Officials bout "+str(boutnum+1))
		self.buttonarray[boutnum][2].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][2].bind("<Button-1>",self.OfficialsWindow(boutnum))
		self.buttonarray[boutnum][3].configure(text="Enter Jam info bout "+str(boutnum+1))
		self.buttonarray[boutnum][3].pack(side=Tk.LEFT)
		self.buttonarray[boutnum][3].bind("<Button-1">,self.JamsWindow(boutnum))
		self._b += 1

	def RenderDVD(self):
		"""Render the DVD, using the functions in dvd-chapter, imported as dc"""

	def mainWindow(self):
		"""The Main Tkinter window interface"""
		# This is a packed dialog with:
		#   [Movie source] [Main menus source] [Chapter menus source] [Credits music source] 
		#   {Enter Team 1} {Enter Team 2} {Enter Officials} {Enter Jam info}
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
