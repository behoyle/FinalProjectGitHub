class scheduler:
    allCourses = []
    preferenceCourses = []
    coursesTaken = []
    class course:
        def __init__(self, term, subject, catalog, section, component, descr, instructor, timeSlot, prereqs, division, wi, qfr, edi):
            self.term = term
            self.classNumber = str(subject) + " " + str(catalog)
            self.subject = subject
            self.catalog = catalog
            self.section = section
            self.component = component
            self.descr = descr
            self.instructor = instructor
            self.timeSlot = timeSlot
            self.prereqs = prereqs
            self.division = division
            self.wi = wi
            self.qfr = qfr
            self.edi = edi
        def printer(self):
            print(str(self.term) + str(self.subject) + str(self.catalog) + str(self.section) + str(self.component) + str(self.descr) + str(self.instructor) + str(self.timeSlot) + str(self.prereqs) + str(self.division) + str(self.wi) + str(self.qfr) + str(self.edi))
    #%%Could add a classes taken array afterwards if we want
    def __init__(self, preferenceStack=None):
        self.importCourses()
        self.importPreferences()
        self.schedulerBuilder()

    def importCourses(self):
        #preferenceStack is a list which we can treat as a stack, containting the contraints given by the user, which we will order based on restriction level
        #parse the csv file
        r = 0
        
        with open('CatalogDataNew3.csv', 'r') as csvfile:
            for line in csvfile.readlines():
                #remove the newline character 
                line = line.replace('\n','')
                data = line.split(',')
                
                if(r>0):
                    self.allCourses.append(scheduler.course(data[0],data[1], data[2], data[3], data[4], data[5], data[6], self.timeGenerator(data[7], data[8], data[9], data[10], data[11], data[12]), self.prereqParser(data[13]), data[14], data[15], data[16], data[17]))
                r+=1                

    def timeGenerator(self, mtg1Start, mtg1End, mtg1Days, mtg2Start, mtg2End, mtg2Days):
        #Organized first by the main meeting days and then further sorts by the meeting hours to find if it's A,B,C, etc
        #Letters as posted in web.williams.edu/admin/registrar//catalog/classhou.pdf
        #Monday, Wednesday, Friday classes
        if mtg1Days == "MWF": 
            if mtg1Start == "08:00 AM":
                return "A"
            elif mtg1Start == "09:00 AM":
                return "B"
            elif mtg1Start == "10:00 AM":
                return "C"
            elif mtg1Start == "11:00 AM" and mtg1End == "11:50 AM":
                return "D"
            elif mtg1Start == "12:00 PM":
                return "E"
            elif mtg1Start == "08:30 AM":
                return "O"
            elif mtg1Start == "11:00 AM" and mtg1End == "12:15 PM":
                return "P"
        #Tuesday, Thursday classes
        if mtg1Days == "TR":
            if mtg1Start == "08:55 AM":
                return "F"
            elif mtg1Start == "08:30 AM":
                return "L"
            elif mtg1Start == "09:55 AM":
                return "M"
            elif mtg1Start == "11:20 AM":
                return "N"
        #Monday only classes
        if mtg1Days == "M":
            #%% Check that these exist
            if mtg1Start == "07:00 PM":
                return "K"
        #Monday, Wednesday classes
        if mtg1Days == "MW":
            if mtg1Start == "11:00 AM":
                return "Q"
        #Monday, Thursday classes
        if mtg1Days == "MR":
            if mtg1Start == "01:10 PM":
                return "R"
            elif mtg1Start == "02:35 PM":
                return "S"
        #Tuesday, Friday classes
        if mtg1Days == "TF":
            if mtg1Start == "01:10 PM":
                return "T"
            elif mtg1Start == "02:35 PM":
                return "U"
        #Wednesday only classes
        if mtg1Days == "W":
            if mtg1Start == "01:10 PM" and mtg1End == "03:50 PM":
                return "W"
            elif mtg1Start == "01:10 PM" and mtg1End == "02:00 PM":
                return "X"
            elif mtg1Start == "02:10 PM":
                return "Y"
            elif mtg1Start == "03:10 PM":
                return "Z"
        else:
            #Does not fit into our block system
            pass

    def prereqParser(self, allPrereqs):
        if allPrereqs.contains("none"):
            return ""
        else:
            #%%make into an array of classes: [ARTH 101, ARTH 102, MATH 101]
            data = allPrereqs.split(" or ")
            data = data.split(" and ")
            data = data.replace()
            return data

    def schedulerBuilder(self):
        fallOutput = []
        springOutput = []
        for i in len(preferenceCourses):
            if 
            if len(self.preferenceCourses[i]) > numSchedules:
                #look further into prefs and compare
                #if still more than 5, prompt user for additional information
                refineFromPrefs(self.preferenceCourses[i])

    def refineFromPrefs(self):
        pass
        
        #we have currentOutput which can be for the fallOutput or springOutput. If it is springOutput, then pass fallOutput as previousSemester
    def fitsPrereqs(self, currentOutput, previousSemseter = None, course):
        #tells us if given course fits in the given semester of the output schedule
        if course.prereqs != "" or !course.prereqs.contains("none") :
            if previousSemseter != None:
                for i in len(previousSemseter): 
                    if course.prereqs == previousSemseter[i].classNumber:
                        return True
            for i in len(coursesTaken)
                if course.prereqs == coursesTaken[i].classNumber:
                    return True
            return False
        else:
            return True
            

            #currentOutput just means the semester we're checking the course against (i.e. the one we're building)
    def fitsScheduleTimes(self, currentOutput, course):
        for i in len(currentOutput):
            if course.timeSlot == currentOutput[i].timeSlot:
                return False
            else:
                return True


    def importPreferences(self):
        file = open('userInput.txt', 'r')
        preferences = file.readlines()
        for x in preferences:
            #%%unsure if this is doing anything
            x.replace("\n", "")
            #%%make sure the stripping of spaces works
            x.strip(" ")
        #make other sortedPreferences which arranges into stack by  most restrictive
        for pref in preferences:
            #will make an array of the filtered course arrays
            self.preferenceCourses.append(self.filteredCourseArray(pref))
        self.preferenceCourses.sort(key = len)

    #Method to create an array of all courses that fit within the given parameter. E.g. professor = bob
    def filteredCourseArray(self, pref):
        sign = pref.find("=")
        category = pref[:sign]
        #Value goes from sign+1 to -1 to skip the \n at the end
        value = pref[sign+1:-1]
        filteredCourseArray = []
        for course in self.allCourses:
            print("category:", getattr(course, category))
            print("value:", value)
            if(getattr(course, category) == value):
                filteredCourseArray.append(course)
                print("appended")
        return filteredCourseArray


if __name__ == '__main__' :
    newSchedule = scheduler()
    print(newSchedule.preferenceCourses)
    #this is how we'll have
    
    
#%%fix catalog number
