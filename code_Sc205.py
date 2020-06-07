# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 01:37:12 2020

@author: 91846
"""

from tkinter import *
from functools import partial

#window
root = Tk()  
root.geometry('800x480')  
root.title("Schedule Maker")


class Graph:

	# Constructor
	def __init__(self, edges, N, nn):

		self.adj = [[] for _ in range(N)]

		# add edges to the undirected graph,here i am accessing the elements
        #of the edges list in pairs so users have to type the vertices(Here subject)
        #which have same student so that it will be assinged  to different slot
        #This input should be after entering the number of pairs 
		for i in range(0, nn-1, 2):
			self.adj[edges[i]].append(edges[i+1])
			self.adj[edges[i+1]].append(edges[i])
            
	# Add more Slots for graphs with many more vertices
slots = ["", "SLOT-1", "SLOT-2", "SLOT-3", "SLOT-4", "SLOT-5", "SLOT-6",
			  "SLOT-7", "SLOT-8", "SLOT-9", "SLOT-10", "SLOT-11"]



# Function to assign slots to vertices of graph
def slotGraph(graph):

	# stores slot assigned to each vertex
	result = {}

	# assign slot to vertex one by one
	for u in range(subject.get()):

		# set to store slot of adjacent vertices of u
		# check slots of adjacent vertices of u and store in set
		assigned = set([result.get(i) for i in graph.adj[u] if i in result])

		# check for first free slot
		slot = 1
		for s in assigned:
			if slot != s:
				break
			slot = slot + 1

		# assigns vertex u the first available slot
		result[u] = slot

	for v in range(subject.get()):
		Intro = Label(root, text=("SLOT", "assigned", "to", "SUBJECT", v+1, "is", slots[result[v]])).grid(row=(12+v),column=1)



def resultfunc(subject, pairs ,pairstring):

    n=pairs
    N = subject.get()
    nn=2*(pairs.get())
    
    edges= [(int(x)-1) for x in (pairstring.get()).split()] 
    
    for i in range(0, nn): 
        print(edges[i])
        
    graph = Graph(edges, N, nn)

	
    return slotGraph(graph)
      

#introlabel

Intro = Label(root, text="Welcome To Schedule maker GUI (｡◕‿◕｡): Get Your Schedule \n NOTE:   Enter Total No. of subjects \n followed by No. of pairs(The two subjects's num in which same student enrolled \n so GUI makes that two subjects in different slots)\n followed by all the subject code in one line(followed by space)\nIf You want to make Schedule again just Press rest button,type input and Get Result ").grid(row=0, column=0,sticky=W)

#subjectlabel and entry
subjectLabel = Label(root, text="Enter The number of SUBJECT(i.e 5): ").grid(row=6, column=0)
subject = IntVar()
subjectEntry =Entry(root, textvariable=subject).grid(row=6, column=1)  

#pairslabel and entry
pairsLabel = Label(root,text="Enter number of pairs(i.e 3) :").grid(row=7, column=0)  
pairs = IntVar()
pairsEntry = Entry(root, textvariable=pairs).grid(row=7, column=1)  

#pairsinstring label and entry
pairstringLabel = Label(root,text="Enter All pairs(i.e 1 means subject1) followed by space(i.e 1 2 1 4 3 5):").grid(row=8, column=0)  
pairstring = StringVar()
pairstringEntry = Entry(root, textvariable=pairstring).grid(row=8, column=1)  


#partial func
resultfunc = partial(resultfunc, subject, pairs, pairstring)

#result button
resultButton = Button(root, text="Result", command=resultfunc).grid(row=9, column=1) 

#resetfunc
def reset():
    
    subject.set("")
    pairs.set('')
    pairstring.set('')
    return
#reset button
ButtonReset = Button(root, text="Reset", command=reset).grid(row=9, column=2)

root.mainloop()
