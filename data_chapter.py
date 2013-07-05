#

###
#
# Data Chapter & Subtitle Script
# Cutdown data entry version (only includes Bout class + dependants)
# 
###
import string
import os, sys



#these parts and other bits of code for writing nice subtitle images stolen from aug.ment.org/dvd/makespumux.py
width = 720;
height = 576;
fontsize = 20;
#font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf", fontsize)
#font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize)
#rubyfont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf",fontsize-4)
#menufont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize+4)
#creditsfont = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf", fontsize*2)

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


#in order to handlge "pass-by-pass scores", events need to be extended to also cover scoreline changes
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
SCORE = 4 #and higher - actual score is Type - Score

#In order to handle "pass-by-pass scores", events need to be extended to also cover changes to the scoreline
class Status(object):
	#An integral of Event objects within a jam
	def __init__(self, eventseq, initscores=(0,0)):
		# LEAD gives LEAD
		# POWER gives POWER (and later removes POWER from other team)
		# POWEREND removes POWER
		# STAR gives STAR and removes LEAD (starred pivots can't have lead status)
		tr_dict = {LEAD:lambda x: x | LEAD_STATUS,POWERSTART: lambda x: x | POWER_STATUS,POWEREND:lambda x : x & POWER_CANCEL,STAR: lambda x :  (x | STAR_STATUS) & LEAD_CANCEL} 
		self.Time=eventseq[-1].Time #our time is always that of last event in passed sequence
		self.Teams = [{'Status':0,'Score':initscores[0]},{'Status':0,'Score':initscores[1]}]
		for e in eventseq:
			#handle dummy rows for jam start events (which use POWEREND with no POWERSTART)
			#don't need to do anything now, since the bitwise op will just unset an unset bit!
			#need to subtract one from e.Team cause of annoying interface issues with things starting at 0
			if e.Type > SCORE: #then we have a scoring status, not a jammer status
				self.Teams[e.Team-1]['Score'] += e.Type - SCORE
			else:
				self.Teams[e.Team-1]['Status'] = tr_dict[e.Type](self.Teams[e.Team-1]['Status'])
				if e.Type == POWERSTART: #if the team just got a power jam, remove the power jam from the other team
					self.Teams[2-e.Team]['Status'] = tr_dict[POWEREND](self.Teams[2-e.Team]['Status'])
					self.Teams[2-e.Team ]['Status'] = self.Teams[2-e.Team]['Status'] & LEAD_CANCEL #and remove the other team's lead, as majors remove your lead status 						
#masks for Status
LEAD_STATUS=1
POWER_STATUS=2
STAR_STATUS=4
LEAD_CANCEL = 7 - LEAD_STATUS
POWER_CANCEL = 7 - POWER_STATUS #use with AND to unset the POWER_STATUS bit

