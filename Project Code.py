import os.path, readline, gzip, csv, re

def get_constraint(file): #this function will find the constraint block
    constraints=[]
    line = file.readline()
    Start = "constraints"
     
    while line:
        line = line.strip()
        if line.startswith(Start):
            constart = line.index("(")
            line = line[constart:]
            constraints.append(line)
        line = file.readline()
    #print (constraints)
    return constraints

def work_constraint(constraints): # this function will alter the constraint and return the new constraint
    digits = ["1", "2", "3","4","5","6","7","8","9","0"]
    constrain_block = []
    for unit in constraints:
        tntconstrain = ""
        temp = ""
        for letter in unit:
            if letter in digits:
                temp = temp + letter
            else:
                if temp !="":
                    temp = int(temp) -1
                    tntconstrain = tntconstrain + str(temp)
                    temp = ""
                if letter == "(" or letter == ")":
                    tntconstrain = tntconstrain + letter
                if letter == ",":
                    tntconstrain = tntconstrain + " "
        tntconstrain = tntconstrain + ";"
        constrain_block.append(tntconstrain)
    return constrain_block
        

def get_matrix(file): #this function will find the block of text we need reading line by line
    line = file.readline()
    StringTaxon = ""
    Taxon = []
    RecordLines = False
    Start = "MATRIX"
    End = "END;"
    while line:
        strip = line.strip()
        if strip == End and RecordLines == True:
            break
        if RecordLines == True and strip !="" and strip !=";":
            StringTaxon = StringTaxon + strip + "\n" 
            Taxon.append(strip)
        if strip == Start:
            RecordLines = True
        line = file.readline()
    return Taxon, StringTaxon
    
       

def Machars(matrix): # this will allow us to parse the character matrix
    #char = ''
    #stringchar = ''
    taxa = {}
    #print("matrix is",matrix)
    for taxonline in matrix:
        WholeMatrix = re.split('\s+',taxonline) 
        taxa[WholeMatrix[0]]=WholeMatrix[1]
    #print(taxa)    
    return taxa

def percentincom(taxa): #this function will collect the character matrix and compute percentage complete
    totallen= 0 #this variable will be the total number of characters coded for the taxa
    questionnum = 0 #this variable will be the number of ? or - for the file
    #taxanum = 0
    print("Taxa \t Percentage Incomplete")
    for species,chars in taxa.items(): 
        taxanum = len(taxa.keys())
        totallen = 0
        questionnum = 0
        
        for char in chars:
            totallen = totallen + 1
            if char == "?":
                questionnum = questionnum + 1
        
        print (species + "\t" +"\t"+ str(round((questionnum/totallen)*100,2 ))+ "%")
    #print (totallen)
    #print (taxanum)
    return totallen, taxanum

def compare (string1, string2):
    #string1 = "1000101010"
    #string2 = "100000100?"
    dist = 0
    
    for x, y in zip (string1, string2): 
            if x !="?" and y !="?" and x !="-" and y !="-" and x==y:
                dist = dist + 1
                #print (dist)
    return (dist)

def comparedic (taxa):
    f2 = open("DistanceData.txt", "w+")
    for species,chars in taxa.items():
        for specie, char in taxa.items():
            if species != specie:
                distmat = compare(chars,char)
                #print (str(species) + "\t" + str(specie))
                #print (distmat)
                f2.write (str(species) + "\t" +str(specie) +"\n")
                f2.write (str(distmat)+ "\n")
    f2.close()
location = 1 # (add back later) input("Where is the file you need? 1 Local 2 Online: ") #would you like to use a local file or download one from online?
try:
    location = int(location) #tells it to expect an integer input
    if location == 1:  #runs script for a local file
        print ("Using Local File")
        local= "tester matrix.nex" #(add back later) input ("What is the file name?: ") #file name must be input here correctly and in the current directory; file should be in nexus format

        try:
            fileloc = str(local)
            #print (fileloc)
            f = open(fileloc, "r")
            f1 = open("TNTOutput.txt", "w+")
            Taxon, StringTaxon = get_matrix(f)
            Matrix = Machars(Taxon)
            totallen, taxanum = percentincom(Matrix)
            TNT1 = str(totallen)
            TNT2 = str(taxanum)
            #print(Taxon)
            #print(StringTaxon)
            #Matrix = Machars(Taxon)
            
            f1.write("nstates 32;" + "\n")
            f1.write("xread" + "\n")
            f1.write(TNT1 + " " + TNT2 + "\n")
            f1.write(StringTaxon)
            f1.write(";" + "\n\n")
            #print(Matrix)
#            print ("File Found!")
            #string1 = "1000101010"
            #string2 = "100000100?"
            #distmat = compare(string1, string2)
            #print (str(distmat) +" this is the distance")
            comparedic(Matrix)
            #print (str(distmatrix) +" this is the distance")
            constraints = get_constraint(f)
            tntcon = work_constraint(constraints)
            #print(tntcon)
            f1.write("force / " + tntcon[0] + "\n")
            f1.write("constrain =;" + "\n")
            f1.write("proc/;" + "\n")
            f.close()
            f1.close()
        except FileNotFoundError:
            print("File Not Found")
 
    elif location == 2:  #runs script for a URL file
        print ("Using URL File")
        url= input ("What is the full url?: ") #asks for url input for download 
        if not os.path.exists(url):
            os.system("curl -0 %s"%(url)) #makes a call to download the file using the Bash curl command
    else:
        print ("Not a valid input. Please enter 1 for local or 2 for online")
except ValueError:
    print("This is not a valid input. Please enter 1 for local or 2 for online.")
