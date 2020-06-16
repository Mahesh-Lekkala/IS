# problem using dfs backtrack forward checking and singleton heuristic
from datetime import datetime

print("Please Enter the Country\nAmerica / Australia")
start = datetime.now()
country = input()
counterForBacktrack=0

class dfs_forward_Checking_Singleton_heuristic(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 

    ## heuristic functions
    def m_r_v(self, domain_dictionary, colours):
        least_val_states = {0:[],1:[],2:[],3:[],4:[]}

        for key, value in domain_dictionary.items():
            if len(value)==0 and colours[key-1] == 0:
                least_val_states[0].append(key-1)

            elif(len(value)==1 and colours[key-1]==0):
                least_val_states[1].append(key-1)

            elif(len(value)==2 and colours[key-1]==0):
                least_val_states[2].append(key-1)

            elif(len(value)==3 and colours[key-1]==0):
                least_val_states[3].append(key-1)

            elif(len(value)==4 and colours[key-1]==0):
                least_val_states[4].append(key-1)

        if len(least_val_states[0])>0:
            return least_val_states[0]

        elif len(least_val_states[1])>0:
            return least_val_states[1]

        elif len(least_val_states[2])>0:
            return least_val_states[2]

        elif len(least_val_states[3])>0:
            return least_val_states[3]
        else:
            return least_val_states[4]


    def DegreeConstraint(self, domain_dictionary, colours):
        Max_DC = 0 #Degree constraint
        Max_DC_state = -1

        for v in range(self.V): 
            if colours[v]!=0:
                continue
            counter = 0
            for i in range(self.V):
                if self.graph[v][i] == 1:
                    counter = counter + 1
            if counter > Max_DC:
                Max_DC = counter
                Max_DC_state = v
        return Max_DC_state


    def L_C_V(self, domain_dictionary, colours):
        Min_DegreeConstraint = 0
        min_DegreeConstraint_state = -1

        for v in range(self.V): 
            if colours[v]!=0:
                continue
            counter = 0
            for i in range(self.V):
                if self.graph[v][i] == 0:
                    counter = counter + 1
            if counter > Min_DegreeConstraint:
                Min_DegreeConstraint = counter
                min_DegreeConstraint_state = v

        return min_DegreeConstraint_state

    def get_next_state(self, domain_dictionary, colours):
        NextState = 0

        next_MRV_states = self.m_r_v(domain_dictionary, colours)
        next_DC_states = self.DegreeConstraint(domain_dictionary, colours)
        next_LeastConstraintValue_states= self.L_C_V(domain_dictionary, colours)

        if (len(next_MRV_states)==1):
            NextState = next_MRV_states[0]
        elif(next_DC_states!=-1):
            NextState = next_DC_states
        else:
            NextState = next_LeastConstraintValue_states

        return NextState




    def if_safe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True

    def retrieve_neighbors(self, state):
        neighbours = []
        for i in range(self.V):
            if self.graph[state][i] == 1:
                neighbours.append(i)
        return neighbours


    #singleton methods
    def if_coloured(self, colors):
        totalvertex = 0

        for color in colors:
            if color != 0:
                totalvertex = totalvertex + 1

        if totalvertex == 50:
            return True
        elif totalvertex == 7:
            return True
        else:
            return False

    def check_singleton_constraints(self, v):
        if self.if_coloured(colour):  
                return True
        if v == self.V: 
                v = random.choice([a for a in range(len(colour)) if colour[a] == 0])

    def singleton_domain_variables_removing(self, v):
        if c in domain_dictionary[v+1]:
            domain_dictionary[v+1].remove(c)

        if c not in domain_dictionary[v+1]:
            domain_dictionary[v+1].append(c)
            domain_dictionary[v+1].sort()


    def singleton_logic(self, st_states):
        if len(st_states)==0:
            return
        state_tocolor = -1
        for key,value in domain_dictionary.items():
            if len(value) == 1 and colour[key-1] == 0:
                state_tocolor = key
                break

        if state_tocolor == -1:
            current = random.choice([a for a in range(len(colour)) if colour[a] == 0])
            if self.graph_colour(m, colour, current) == True:
                return True
        else:
            if self.graph_colour(m, colour, state_tocolor-1) == True:
                return True

    def graph_colour(self, m, colour, v):
        global counterForBacktrack
        try:
            if v == self.V: 
                return True
            if country == 'Australia':
                list_st_states = list(range(self.V%7))
            if country == 'America':
                list_st_states = list(range(self.V%50))
            self.singleton_logic(list_st_states)

            if not domain_dictionary[v+1]:
                return False

            for c in domain_dictionary[v+1]:
                if self.if_safe(v, colour, c) == True:
                    colour[v] = c 
                    neighbors = self.retrieve_neighbors(v) 

                    for neighbor in neighbors:
                        if c in domain_dictionary[neighbor+1]:
                            domain_dictionary[neighbor+1].remove(c)

                    NextState = self.get_next_state(domain_dictionary, colour)
                    if NextState != -1:
                        if self.graph_colour(m, colour, NextState) == True:
                            return True
                    else:
                        if self.graph_colour(m, colour, v+1) == True:
                            return True

                    for neighbor in neighbors:
                        a = neighbor+1
                        if c not in domain_dictionary[a]:
                            domain_dictionary[a].append(c)
                            domain_dictionary[a].sort()
                    colour[v] = 0
                else:
                    counterForBacktrack +=1
        except Exception as e:
            print("something wrong", e)

    def GraphColuringUtil(self, m): 
        colour = [0] * self.V 
        if self.graph_colour(m, colour, 0) == False: 
            return False

        # Print the solution 
        print("Solution exist and Following are the colours that have been assingned:")
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

    state_dictionary = {}
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
    color_dictionary = {"1":"red", "2":"green", "3":"yellow", "4":"blue"}






    dictionary_of_domain(5)


    # Driver Code 
    g = dfs_forward_Checking_Singleton_heuristic(50)

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
    g = dfs_forward_Checking_Singleton_heuristic(7) #number of states 

    g.graph =  positions

    m=3 ## chromataic number


g.GraphColuringUtil(m) 

end = datetime.now()

elapsed = end - start
print("THE TOTAL TIME TOOK FOR EXECUTION ----------------",str(elapsed.total_seconds()))
print("total number of backtracks taken:"+str(counterForBacktrack))
for key, value in result_dictionary.items():
	print("{} => {}".format(key,value))
