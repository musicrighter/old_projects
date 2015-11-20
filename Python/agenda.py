"""An Agenda is a list-like container of Appt (appointment).

   Authors: David Gustafson for CIS 210, U. Oregon, Winter 2014
   Consulted with: Xintien Meng
   
   Each Appt occurs on a single day, with a start time, an end time, and
   a textual description.   They can be converted to and
   from strings, using the from_string class method and the __str__
   method.  An Agenda is essentially a list of appointments,
   with some special methods.  An Agenda can be read from a file using the
   from_file class method.  Intersecting Agendas produces
   a new Agenda whose Appts are periods that are in the overlap
   of Appts in the first and second Agenda.
   
"""

import datetime

class Appt:

    """
    A single appointment, starting on a particular
    date and time, and ending at a later time the same day.
    """
    
    def __init__(self, day, begin, end, desc):
        """Create an appointment on date
        from begin time to end time.
        
        Arguments:
            day:   A datetime.date object.  The appointment occurs this day.
            begin: A datetime.time object.  When the appointment starts. 
            end:  A datetime.time object, 
                after begin.                When the appointments ends.
            desc: A string describing the appointment
            
        Raises: 
        	ValueError if appointment ends before it begins
        	
        Example:
            Appt( datetime.date(2012,12,1),
                datetime.time(16,30),
                datetime.time(17,45))
            (December 1 from 4:30pm to 5:45pm)
        """
        self.begin = datetime.datetime.combine(day, begin)
        self.end = datetime.datetime.combine(day, end)
        if self.end < self.begin:   # Rasises error for impossible appt time
            raise ValueError('Appointment ends before it begins')
        self.desc = desc
        return

    @classmethod
    def from_string(cls, txt):
        """Factory parses a string to create an Appt.
           Args:
               txt: String specifying appointment date, time, and description
                    Format is "2014.2.14 15:10 15:35 | Umbrella lessons"
        """
        fields = txt.split("|")
        if len(fields) != 2:
            raise ValueError("Appt literal requires exactly one '|' before description")
        timespec = fields[0].strip()
        desc = fields[1].strip()
        fields = timespec.split()
        if len(fields) != 3:
            raise ValueError("Appt literal must start with date, time, time, separated by blanks")
        appt_date_text = fields[0]
        appt_begin_text = fields[1]
        appt_end_text = fields[2]
        fields = appt_date_text.split(".")
        try:
            year = int(fields[0].strip())
            month = int(fields[1].strip())
            day = int(fields[2].strip())
        except:
            raise ValueError("Date in Appt literal should be 9999.99.99 (Year.Month.Day)")

        ### 
        date = datetime.date(year,month,day)
        begin = datetime.datetime.strptime(appt_begin_text, "%H:%M").time()
        end =   datetime.datetime.strptime(appt_end_text, "%H:%M").time()

        result = Appt(date, begin, end, desc)
        return result   
        
    def __lt__(self, other):
        """Does this appointment finish before other begins?
        
        Arguments:
        	other: another Appt
        Returns: 
        	True iff this Appt is done by the time other begins.
        """
        return other.begin >= self.end 
        
    def __gt__(self, other):
        """Does other appointment finish before this begins?      
        Arguments:
        	other: another Appt
        Returns: 
        	True iff other is done by the time this Appt begins
        """
        return other < self

    def overlaps(self, other):
        """Is there a non-zero overlap between this appointment
           and the other appointment?
        Arguments:
            other: another Appt
        Returns:
            True iff there is not a non-zero overlap between appointments    
        """
        if self > other or self < other:
            return False
        else:
            return True
        
    def intersect(self, other, desc=""):
        """Return an appointment representing the period in
        common between this appointment and another.
        Requires self.overlaps(other).
        
		Arguments: 
			other:  Another Appt
			desc:  (optional) description text for this appointment. 
		Returns: 
			An appointment representing the time period in common
			between self and other.   Description of returned Appt 
			is copied from this (self), unless a non-null string is 
			provided as desc. 
        """
        if desc=="":
            desc = self.desc
        if self.overlaps(other):  # No need to continue if this is False
            start = self.begin   
            if self.begin < other.begin:   # Earliest time of overlap
                start = other.begin
            end = self.end
            if self.end > other.end:   # Latest time of overlap
                end = other.end
            return Appt(self.begin.date(), start.time(), end.time(), desc) ##FIXME

    def __str__(self):
        """String representation of appointment.
        Example:
            2012.10.31 13:00 13:50 | CIS 210 lecture
            
        This format is designed to be easily divided
        into parts:  Split on '|', then split on whitespace,
        then split date on '.' and times on ':'.
        """
        daystr = self.begin.date().strftime("%Y.%m.%d ")
        begstr = self.begin.strftime("%H:%M ")
        endstr = self.end.strftime("%H:%M ")
        return daystr + begstr + endstr + "| " + self.desc

class Agenda:
    """An Agenda is essentially a list of appointments,
    with some agenda-specific methods.
    """

    def __init__(self):
        """An empty agenda."""
        self.appts = [ ]
        
    @classmethod
    def from_file(cls, f):
        """Factory: Read an agenda from a file.
        
        Arguments: 
            f:  A file object (as returned by io.open) or
               an object that emulates a file (like stringio). 
        returns: 
            An Agenda object
        """
        agenda = cls()
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                # Skip blank lines and comments
                pass
            else: 
                try: 
                    agenda.append(Appt.from_string(line))
                except ValueError as err: 
                    print("Failed on line: ", line)
                    print(err)
        return agenda

    def append(self,appt):
        """Add an Appt to the agenda."""
        self.appts.append(appt)

    def intersect(self,other,desc=""): 
        """Return a new agenda containing appointments
        that are overlaps between appointments in this agenda
        and appointments in the other agenda.

        Titles of appointments in the resulting agenda are
        taken from this agenda, unless they are overridden with
        the "desc" argument.

        Arguments:
           other: Another Agenda, to be intersected with this one
           desc:  If provided, this string becomes the title of
                all the appointments in the result.
        """
        use_default_desc = (desc == "")
        result = Agenda()   # Empty list
        for appt_self in self.appts:
            for appt_other in other.appts:
                if appt_other.overlaps(appt_self):
                    result.append(appt_self.intersect(appt_other))   # Add times to list
        return result

    def sort(self):
         '''Order appointments by begin time'''
         ordering = lambda ap: ap.begin
         self.appts.sort(key=ordering)

    def normalize(self):
        '''Merge overlapping times so that each overlapping section is put
           together in a new list.
        Arguments:
            self: Agenda that might contain appointments with overlapping times
        Returns:
            new_list: Agenda of merged appointments
        '''
        self.sort()
        new_list = Agenda()   # empty Agenda
        if self.appts == []:
            return self.appts
        appt = self.appts
        prev_date = appt[0].begin.date()   # Seperate out the
        prev_begin = appt[0].begin         # first appointment
        prev_end = appt[0].end             
        prev_desc = appt[0].desc           
        for i in appt[1:]:                 # Seperate the rest
            date = i.begin.date()          # of the appointments
            begin = i.begin
            end = i.end
            desc = i.desc
            if prev_end < begin:   # Create new appointment
                new_list.append(Appt(prev_date, prev_begin.time(), prev_end.time(), prev_desc))
                prev_date = date
                prev_begin = begin
                prev_end = end
                prev_desc = desc
            else:
                prev_end = end
                prev_desc += ';' + desc
        new_list.append(Appt(prev_date, prev_begin.time(), prev_end.time(), prev_desc))   # Acoounts for last appointments
        return new_list

    def complement(self, freeblock):
        '''Produce the complement of an agenda within the 
           span of a timeblock represented by an appointment.
        Arguments:
            self: Agenda that contains appointments with unavailable times.
            freeblock: Start to end time being looked for free times
        Returns:
            complement: Agenda full of available times
        '''
        self.normalize()
        current = freeblock.begin.time()   # Initialize current
        free_end = freeblock.end.time()
        complement = Agenda()
        free_day = freeblock.begin.date()
        for appt in self:   # Cycle through each appointment
            day = appt.begin.date()
            begin = appt.begin.time()
            end = appt.end.time()
            desc = freeblock.desc
            if appt.begin.date() == freeblock.begin.date():   # Check for same day
                if end <= current:
                    continue
                if begin >= free_end:   # Outside of freeblock
                    break
                if begin < freeblock.begin.time():
                    current = end
                if current < begin:   # Doesn't overlap
                    complement.append(Appt(free_day, current, begin, desc))
                current = end
        if free_end > current:   # Section after end of appt but before freeblock ends
            complement.append(Appt(free_day, current, free_end, desc))
        return complement

    def __len__(self):
        """Number of appointments, callable as built-in len() function"""
        return len(self.appts)

    def __iter__(self):
        """An iterator through the appointments in this agenda."""
        return self.appts.__iter__()

    def __str__(self):
        """String representation of a whole agenda"""
        rep = ""
        for appt in self.appts:
            rep += str(appt) + "\n"
        return rep[:-1]

    def __eq__(self,other):
        """Equality, ignoring descriptions --- just equal blocks of time"""
        if len(self.appts) != len(other.appts):
            return False
        for i in range(len(self.appts)):
            mine = self.appts[i]
            theirs = other.appts[i]
            return (mine.begin == theirs.begin and
                    mine.end == theirs.end)


#########################
#  Self-test invoked when module is run
#  as main program. 
#########################
    
from test_harness import *
import io
def selftest_appt():
    """Simple smoke test for Appt class."""
    sample = Appt(datetime.date(2012, 10, 31),
                  datetime.time(14, 30), datetime.time(15, 45),
                  "Sample appointment")
    testEQ("Create and format",str(sample),
           "2012.10.31 14:30 15:45 | Sample appointment") 
    
    earlier = Appt(datetime.date(2012, 10, 31),
                    datetime.time(13, 30), datetime.time(14,30), 
                    "Before my appt")
    later = Appt(datetime.date(2012, 10, 31),
                  datetime.time(16,00), datetime.time(21,00), "Long dinner")
    
    testEQ("Strictly before is '<'", earlier < later, True)
    testEQ("Strictly after is '>'", later > earlier, True)
    testEQ("Not earlier than itself", earlier < earlier, False)
    testEQ("Not later than itself", earlier > later, False)
    
    testEQ("Earlier doesn't overlap later", earlier.overlaps(later), False) 
    testEQ("Later doesn't overlap earlier", later.overlaps(earlier), False)
    
    conflict = Appt(datetime.date(2012, 10, 31), 
                    datetime.time(13, 45), datetime.time(16,00),
        "Conflicting appt")

    testEQ("Should overlap", sample.overlaps(conflict), True)
    testEQ("Opposite overlap", conflict.overlaps(sample), True)
    overlap = sample.intersect(conflict)
    testEQ("Expected intersection", str(overlap), 
           "2012.10.31 14:30 15:45 | Sample appointment")
    overlap = conflict.intersect(sample)
    testEQ("Expected intersection", str(overlap), 
           "2012.10.31 14:30 15:45 | Conflicting appt")
    overlap = conflict.intersect(sample,"New desc")
    testEQ("Expected intersection", str(overlap), 
           "2012.10.31 14:30 15:45 | New desc")

    text = "2012.10.31 14:30 15:45 | from text"
    from_text = Appt.from_string(text)
    testEQ("String <-> Appt",text, str(from_text))
    def die():
       Appt.from_string("2012.10.31 15:45 14:30 | time traveler")
    testRaise("Time order error", ValueError, die)       
       

def selftest_agenda():
    """Simple smoke test for Agenda class."""

    keiko_agtxt="""# Free times for Keiko on December 1
           2012.12.1 07:00 08:00  | Possible breakfast meeting
           2012.12.1 10:00 12:00  | Late morning meeting
           2012.12.1 14:00 18:00  | Afternoon meeting
         """

    kevin_agtxt="""2012.11.30 09:00 14:00 | I have an afternoon commitment on the 30th
          2012.12.1  09:00 15:00 | I prefer morning meetings
          # Kevin always prefers morning, but can be available till 3, except for 
          # 30th of November.
          """

    emanuela_agtxt = """
    2012.12.1 12:00 14:00 | Early afternoon
    2012.12.1 16:00 18:00 | Late afternoon into evening
    2012.12.2 8:00 17:00 | All the next day
    """
    
    keiko_ag = Agenda.from_file(io.StringIO(keiko_agtxt))
    kevin_ag = Agenda.from_file(io.StringIO(kevin_agtxt))
    emanuela_ag = Agenda.from_file(io.StringIO(emanuela_agtxt))    

    keiko_kevin = keiko_ag.intersect(kevin_ag)
    kk = ("2012.12.01 10:00 12:00 | Late morning meeting\n" +
         "2012.12.01 14:00 15:00 | Afternoon meeting")
    kkactual = str(keiko_kevin)
    testEQ("Keiko and Kevin", kkactual.strip(), kk.strip())

    kevin_emanuela = kevin_ag.intersect(emanuela_ag)
    ke = "2012.12.01 12:00 14:00 | I prefer morning meetings"
    keactual = str(kevin_emanuela)
    testEQ("Kevin and Emanuela", keactual, ke)

    everyone = keiko_kevin.intersect(emanuela_ag)
    testEQ("No overlap of all three", len(everyone), 0)

def selftest2_agenda():
    print("""
    **********************************
    *** Smoke test Agenda addenda   **
    *** normalization and complement**
    ********************************""")
    
    """Additional tests for agenda normalization and complement."""
    # What could go wrong in sorting? 
    keiko_agtxt="""2013.12.2 12:00 14:00 | Late lunch
                   2013.12.1 13:00 14:00 | Sunday brunch
                   2013.12.2 08:00 15:00 | Long long meeting
                   2013.12.2 15:00 16:00 | Coffee after the meeting"""
    keiko_ag = Agenda.from_file(io.StringIO(keiko_agtxt))

    # Torture test for normalization
    day_in_life_agtxt = """
    # A torture-test agenda.  I am seeing a lot of code 
    # that may not work well with sequences of three or more
    # appointments that need to be merged.  Here's an agenda
    # with such a sequence.  Also some Beatles lyrics that have
    # been running through my head.  
    # 
    2013.11.26 09:00 10:30 | got up
    2013.11.26 10:00 11:30 | got out of bed
    2013.11.26 11:00 12:30 | drug a comb across my head
    2013.11.26 12:00 13:30 | on the way down stairs I had a smoke
    2013.11.26 13:00 14:30 | and somebody spoke
    2013.11.26 14:00 15:30 | and I went into a dream
    #
    # A gap here, from 15:30 to 17:00
    # 
    2013.11.26 17:00  18:30 | he blew his mind out in a car
    2013.11.26 18:00  19:30 | hadn't noticed that the lights had changed
    2013.11.26 19:00  20:30 | a crowd of people stood and stared
    #
    # A gap here, from 20:30 to 21:00
    #
    2013.11.26 21:00 22:30 | they'd seen his face before
    2013.11.26 22:00 23:00 | nobody was really sure ..."""
    day_in_life = Agenda.from_file(io.StringIO(day_in_life_agtxt))
    day_in_life = day_in_life.normalize()
    # How are we going to test this?  I want to ignore the text descriptions.
    # Defined __eq__ method in Agenda just for this
    should_be_txt = """
    2013.11.26 09:00 15:30 | I read the news today oh, boy
    2013.11.26 17:00 20:30 | about a lucky man who made the grade
    2013.11.26 21:00 23:00 | and though the news was rather sad
    """
    should_be_ag = Agenda.from_file(io.StringIO(should_be_txt))
    testEQ("Torture test normalized",day_in_life,should_be_ag)

    # Start with the simplest cases of "complement"
    simple_agtxt = """2013.12.01 12:00 14:00 | long lunch"""
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    
    # Different day - should have no effect
    tomorrow = Appt.from_string("""2013.12.02 11:00 15:00 | tomorrow""")
    simple_ag = simple_ag.complement(tomorrow)
    testEQ("Yesterday's appts don't matter",str(simple_ag).strip(),
           """2013.12.02 11:00 15:00 | tomorrow""")
    # And the freeblock should not be altered
    testEQ("Not clobber freeblock",str(tomorrow),
           """2013.12.02 11:00 15:00 | tomorrow""")
    
    # Freeblock completely covered
    simple_agtxt = """2013.12.01 12:00 14:00 | long lunch"""
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    lunch = Appt.from_string("""2013.12.01 12:30 13:30 | lunch""")
    simple_ag = simple_ag.complement(lunch)
    testEQ("Completely blocked freeblock",str(simple_ag).strip(),"")
    # And the freeblock should not be altered
    testEQ("Not clobber freeblock 2",str(lunch),
           """2013.12.01 12:30 13:30 | lunch""")
    
    # Freeblock different times same day
    simple_agtxt = """2013.12.01 12:00 14:00 | long lunch"""
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    dinner = Appt.from_string("""2013.12.01 19:30 20:30 | dinner""")
    simple_ag = simple_ag.complement(dinner)
    testEQ("Freeblock later in day",str(simple_ag).strip(),
           """2013.12.01 19:30 20:30 | dinner""")
    #
    # More complex agendas - try with two appointments
    #
    simple_agtxt = """
    2013.12.01 9:00 11:00 | morning meeting
    2013.12.01 13:00 14:00 | afternoon meeting"""
    # Cover first part first appt
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    part_cover_first = Appt.from_string("2013.12.01 08:30 09:30 | morning coffee")
    simple_ag = simple_ag.complement(part_cover_first)
    testEQ("Freeblock partly covers first appt start only",
           str(simple_ag).strip(), "2013.12.01 08:30 09:00 | morning coffee")
    # Cover last part first appt
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    part_cover_first = Appt.from_string("2013.12.01 09:30 11:30 | morning coffee")
    simple_ag = simple_ag.complement(part_cover_first)
    testEQ("Freeblock partly covers first appt end only",
           str(simple_ag).strip(), "2013.12.01 11:00 11:30 | morning coffee")
    # Cover first part second appt
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    part_cover_first = Appt.from_string("2013.12.01 12:30 13:30 | afternoon coffee")
    simple_ag = simple_ag.complement(part_cover_first)
    testEQ("Freeblock partly covers second appt start only",
           str(simple_ag).strip(), "2013.12.01 12:30 13:00 | afternoon coffee")
    # Cover last part second appt
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    part_cover_first = Appt.from_string("2013.12.01 13:30 14:30 | afternoon coffee")
    simple_ag = simple_ag.complement(part_cover_first)
    testEQ("Freeblock partly covers second appt end only",
           str(simple_ag).strip(), "2013.12.01 14:00 14:30 | afternoon coffee")
    # Cover middle part two appts
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    part_cover_first = Appt.from_string("2013.12.01 10:30 13:30 | mid-day")
    simple_ag = simple_ag.complement(part_cover_first)
    testEQ("Freeblock partly covers two appts and gap",
           str(simple_ag).strip(), "2013.12.01 11:00 13:00 | mid-day")
    # Extend across two appts
    simple_ag = Agenda.from_file(io.StringIO(simple_agtxt))
    part_cover_first = Appt.from_string("2013.12.01 08:00 15:00 | most of day")
    simple_ag = simple_ag.complement(part_cover_first)
    testEQ("Freeblock fully covers two appts and gap",
           str(simple_ag).strip(), "2013.12.01 08:00 09:00 | most of day" +
           "\n" + "2013.12.01 11:00 13:00 | most of day" + 
           "\n" + "2013.12.01 14:00 15:00 | most of day")

if __name__ == "__main__":
    # selftest_appt()
    # selftest_agenda()
    selftest2_agenda()
    
    
    
