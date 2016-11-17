import sys

class Musician (object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end= " ")
        print()
    
class Bassist(Musician):
    def __init__(self, name):
        super().__init__(sounds = ["Twang", "Thrumb", "Bling"])
        self.name = name
        self.instrument = "Bass"
  
        
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(sounds = ["Boink", "Bow", "Boom"])
        self.name = name
        self.instrument = "Guitar"

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(sounds = ["Thump", "Snare", "Crash"])
        self.name = name
        self.instrument = "Drums"
    
    def HitIt(self):
        for i in range(1,5):
            print(str(i)+"!", end=" ")
        print()
    
    def SpontaneousCombustion(self):
        print("Your drummer has died of spontaneous combustion.")

class Band(object):
    def __init__(self):
        self.BandMembers = {}
        self.LeadDrums = None
        
    def HireMember(self, musician):
        if musician in self.BandMembers.keys():
            print("They're already part of the band!")
            return
        elif musician.instrument == "Drums":
            if "Drums" not in self.BandMembers.values():
                self.LeadDrums = musician
    
        self.BandMembers[musician] = musician.instrument
        print("Welcome to the band, " + str(musician.name) + "!")
    
    def FireMember(self, musician):
        if musician in BandMembers:
            BandMembers.remove(musician)
            print(str(musician.name) + " has been fired from the band.")
        else:
            print("Uh, you can't fire someone that isn't part of the band.")
            
    def JamSession(self):
        if self.LeadDrums == None:
            print("You need to find a drummer to kick off this jam session!")
        else:
            print(str(self.LeadDrums.name) +": ", end=" ")
            self.LeadDrums.HitIt()
            for member in self.BandMembers:
                print(member.name +": ", end=" ")
                member.solo(6)

            

nigel = Bassist("Nigel")
moon = Drummer("Keith")
flea = Bassist("Flea")

TheShins = Band()

TheShins.HireMember(flea)
TheShins.HireMember(nigel)
TheShins.HireMember(moon)

TheShins.JamSession()        