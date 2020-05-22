from programs.backtracking.board import Chess
from time import time
import os
import tkinter
from tkinter import *
from tkinter import ttk

# dimension = int(input("Enter board dimension: "))
# chess = Chess(dimension)

'''Single BackTracking report --------------------------------'''
def singleBackTrackingReport(chess, dimension):
    with open(os.getcwd()+'\\files\\nqueen\\'+"Single_BackTrackingResults.txt","r+") as file:
        file.truncate(0)
        file.close()
    chess.reportBackTrackingTime()
    print("dimension "+str(dimension)+" completed")

'''All solutions BackTracking report --------------------------------'''
def allSolutionsBackTrackingReport(chess, dimension):
    with open(os.getcwd()+'\\files\\nqueen\\'+"All_BackTrackingResults.txt","r+") as file:
        file.truncate(0)
        file.close()
    chess.reportAllSolutionsTime()
    print("dimension "+str(dimension)+" completed")

'''Single BackTracking -------------------------------'''

# start = time()
# chess.solveBackTracking(0, True)
# # chess.solveBackTracking(0)
# end =time()
# for solution in chess.solutions:
#     for row in solution:
#         print(row)
# print(end - start)
#
'''All solutions backtracking------------------------------'''
#
# chess.getAllSolutions(0)
# print(chess.solutionCount)
# print(chess.solutions)
''' Horse movement ----------------------------------------'''




'''/---------------------------------------/
  /-------------GRAPHICAL APP-------------/
 /---------------------------------------/
'''
def solveProblem():
    chess = Chess(int(n.get()))
    if int(n.get())>2:
        chess.solveBackTracking(0, True)
        chess.reportBackTrackingTime()
        chess.reportAllSolutionsTime()
        solution = chess.solutions[0]
        for solution in chess.solutions:
            for row in solution:
                print(row)
            print("")
    return

window = Tk()
window.wm_title("HX N queen solver")

l = Label(window,text="Dimension:")
l.grid(row=0,column=0)

n = StringVar()
e1 = Entry(window,textvariable = n)
e1.grid(row=0,column=1)

solver = ttk.Button(window,text="Solve",width=8,command=solveProblem)
solver.grid(row=1,column=2)
choice = tkinter.IntVar()
back = Label(window, text="Backtracking")
back.grid(row=1,column=1)



window.mainloop()
