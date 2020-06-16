# problem using dfs backtracking and forward Checking


from datetime import datetime

print("Please Enter the Country\nAmerica / Australia")

starting_time = datetime.now()
country = input()
counterForBacktrack = 0



class dfs_forwardchecking(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 


    def check_is_safe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True

    def get_the_neighbors(self, state):
        neighbors = []
        for i in range(self.V):
            if self.graph[state][i] == 1:
                neighbors.append(i)
        return neighbors


    # A recursive utility function to solve m  
    def garph_colour(self, m, colour, v):
        global counterForBacktrack
        try:
            if v == self.V: 
                return True

            if not domain_dictionary[v+1]:
                return False

            for c in domain_dictionary[v+1]:
                if self.check_is_safe(v, colour, c) == True:
                    colour[v] = c 
                    neighbors = self.get_the_neighbors(v) 

                    for neighbor in neighbors:
                        if c in domain_dictionary[neighbor+1]:
                            domain_dictionary[neighbor+1].remove(c) 

                    if self.garph_colour(m, colour, v+1) == True:
                        return True


                    for neighbor in neighbors:
                        a = neighbor+1
                        if c not in domain_dictionary[a]:
                            domain_dictionary[a].append(c)
                            domain_dictionary[a].sort()
                    colour[v] = 0
                else:
                    counterForBacktrack+=1
        except Exception as e:
            print("something wrong", e)

    def graph_colouring(self, m): 
        colour = [0] * self.V 
        if self.garph_colour(m, colour, 0) == False: 
            return False

        # Print the solution 
        print("Solution exist and Following are the colours that we have assinged:")
        for idx, val in enumerate(colour): 
             result_dictionary[state_dictionary[str(idx+1)]] = color_dictionary[str(val)]
        return True






def dictionary_of_domain(n):
	for key, value in enumerate(state_dictionary):
		integers = list(range(1,n))
		domain_dictionary[key+1] = integers
        

if country == 'America':        
    change_position=[[9,10,24,42],[],[5,6,28,31,44],[18,24,25,36,42,43],[3,28,37],[3,16,27,31,34,36,50],[21,32,39],[20,30,38],[1,10],[1,9,33,40,42],[],[26,28,37,44,47,50],[14,15,17,22,25,49],[13,17,22,35],[13,23,25,27,41,49],[6,25,27,36],[13,14,25,35,42,46,48],[4,24,43],[29],[8,38,46,48],[7,29,32,39,45],[13,14,23,35,49],[15,22,34,41,49],[1,18,42,43],[4,13,15,16,17,27,36,42],[12,34,41,50],[6,15,16,25,41,50],[3,5,12,37,44],[19,21,45],[8,32,38],[3,6,36,43,44],[7,21,30,38,39,45],[10,23,26,40,41,42,46],[23,26,41],[14,17,22,38,48],[4,6,16,25,31,43],[5,12,28,47],[8,20,30,32,35,48],[7,21,32],[10,33],[15,23,26,27,34,50],[1,4,10,17,24,25,33],[4,18,31,36],[3,6,12,28,31,50],[21,29,32],[17,20,33,42,48],[12,37],[17,20,35,38,46],[13,15,20,22,23],[6,12,26,27,41,44]]

    positions = []
    for i in range(0,50) :
        individual=[]
        for j in range(0,50) : 
            individual.append(0)
        for j in change_position[i] : 
            individual[j-1] =1 
        positions.append(individual)

    state_dictionary={}
    color_dictionary = {"1":"red", "2":"green", "3":"yellow", "4":"blue"}
    result_dictionary = {}
    domain_dictionary = {}
    state_dictionary["1"] = "AL"
    state_dictionary["2"] = "AK"
    state_dictionary["3"] = "AZ"
    state_dictionary["4"] = "AR"
    state_dictionary["6"] = "CO"
    state_dictionary["5"] = "CA"
    state_dictionary["7"] = "CT"
    state_dictionary["8"] = "DE"
    state_dictionary["9"] = "FL"
    state_dictionary["10"] = "GA"
    state_dictionary["11"] = "HI"
    state_dictionary["12"] = "ID"
    state_dictionary["13"] = "IL"
    state_dictionary["14"] = "IN"
    state_dictionary["15"] = "IA"
    state_dictionary["16"] = "KS"
    state_dictionary["17"] = "KY"
    state_dictionary["18"] = "LA"
    state_dictionary["19"] = "ME"
    state_dictionary["20"] = "MD"
    state_dictionary["21"] = "MA"
    state_dictionary["22"] = "MI"
    state_dictionary["23"] = "MN"
    state_dictionary["24"] = "MS"
    state_dictionary["25"] = "MO"
    state_dictionary["26"] = "MT"
    state_dictionary["27"] = "NE"
    state_dictionary["28"] = "NV"
    state_dictionary["29"] = "NH"
    state_dictionary["30"] = "NJ"
    state_dictionary["31"] = "NM"
    state_dictionary["32"] = "NY"
    state_dictionary["33"] = "NC"
    state_dictionary["34"] = "ND"
    state_dictionary["35"] = "OH"
    state_dictionary["36"] = "OK"
    state_dictionary["37"] = "OR"
    state_dictionary["38"] = "PA"
    state_dictionary["39"] = "RI"
    state_dictionary["40"] = "SC"
    state_dictionary["41"] = "SD"
    state_dictionary["42"] = "TN"
    state_dictionary["43"] = "TX"
    state_dictionary["44"] = "UT"
    state_dictionary["45"] = "VT"
    state_dictionary["46"] = "VA"
    state_dictionary["47"] = "WA"
    state_dictionary["48"] = "WV"
    state_dictionary["49"] = "WI"
    state_dictionary["50"] = "WY"
    color_dictionary = {"1":"red", "2":"green", "3":"yellow", "4":"blue"}
    result_dictionary = {}
    domain_dictionary = {}





    dictionary_of_domain(5)


    # Driver Code 
    g = dfs_forwardchecking(50)

    g.graph =  positions


    m=4 ## chromataic number
 
    
    
if country == 'Australia':
    change_position = [[3,4,6],[3,4,7],[1,2,4],[1,2,3,4,6,7],[],[1,4],[2,4]]
    positions = []
    for i in range(0,7) :
        individual=[]
        for j in range(0,7) : 
            individual.append(0)
        for j in change_position[i] : 
            individual[j-1] =1 
        positions.append(individual)

    state_dictionary = {}
    state_dictionary["1"] = "New South Wales"
    state_dictionary["2"] = "Northern Territory"
    state_dictionary["3"] = "Queensland"
    state_dictionary["4"] = "South Australia"
    state_dictionary["5"] = "Tasmania"
    state_dictionary["6"] = "Victoria"
    state_dictionary["7"] = "Western Australia"
    color_dictionary = {"1": "red", "2": "green", "3": "blue"}
    result_dictionary = {}
    domain_dictionary = {}
    dictionary_of_domain(4)
    
     # Driver Code 
    g = dfs_forwardchecking(7) 

    g.graph =  positions

    m=3 ## chromataic number


    

    

g.graph_colouring(m) 
ending_time = datetime.now()

difference = ending_time - starting_time
print("THE TOTAL TIME TOOK FOR EXEC ----------------",str(difference.total_seconds()))
print("The number of backtracking steps happened:"+str(counterForBacktrack))

for key, value in result_dictionary.items():
	print("{} => {}".format(key,value))