#!/usr/bin/python3
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, simpledialog

import backend
import main

algorithm = None
initialState = None
statepointer = cost = counter = depth = 0
path = []


class InterfaceApp:

    def __init__(self, master=None):

        self._job = None
        self.appFrame = ttk.Frame(master)
        self.appFrame.configure(height=550, width=800)
        self.appFrame.pack(side="top")

        self.mainlabel = ttk.Label(self.appFrame)
        self.mainlabel.configure(anchor="center", font="{Forte} 36 {bold}", foreground="#003e3e", justify="center",
                                 text='8-Puzzle Solver')
        self.mainlabel.place(anchor="center", x=300, y=50)

        self.backbutton = ttk.Button(self.appFrame)
        self.img_backicon = tk.PhotoImage(file="back-icon.png")
        self.backbutton.configure(cursor="hand2", image=self.img_backicon)
        self.backbutton.place(anchor="center", height=80, width=80, x=250, y=500)
        self.backbutton.bind("<ButtonPress>", self.prevSequence)

        self.nextbutton = ttk.Button(self.appFrame)
        self.img_nexticon = tk.PhotoImage(file="next-icon.png")
        self.nextbutton.configure(cursor="hand2", image=self.img_nexticon)
        self.nextbutton.place(anchor="center", height=80, width=80, x=350, y=500)
        self.nextbutton.bind("<ButtonPress>", self.nextSequence)

        self.fastforwardbutton = ttk.Button(self.appFrame)
        self.img_fastforwardicon = tk.PhotoImage(file="fast-forward-icon.png")
        self.fastforwardbutton.configure(cursor="hand2", image=self.img_fastforwardicon)
        self.fastforwardbutton.place(anchor="center", height=80, width=80, x=450, y=500)
        self.fastforwardbutton.bind("<ButtonPress>", self.fastForward)

        self.fastbackwardbutton = ttk.Button(self.appFrame)
        self.img_fastbackwardicon = tk.PhotoImage(file="fast-backward-icon.png")
        self.fastbackwardbutton.configure(cursor="hand2", image=self.img_fastbackwardicon)
        self.fastbackwardbutton.place(anchor="center", height=80, width=80, x=150, y=500)
        self.fastbackwardbutton.bind("<ButtonPress>", self.fastBackward)

        self.stopbutton = ttk.Button(self.appFrame)
        self.img_stopicon = tk.PhotoImage(file="stop.png")
        self.stopbutton.configure(cursor="hand2", image=self.img_stopicon, state='disabled')
        self.stopbutton.place(anchor="center", height=80, width=80, x=550, y=500)
        self.stopbutton.bind("<ButtonPress>", self.stopFastForward)

        self.resetbutton = ttk.Button(self.appFrame)
        self.img_reseticon = tk.PhotoImage(file="reset-icon.png")
        self.resetbutton.configure(cursor="hand2", image=self.img_reseticon, state='disabled')
        self.resetbutton.place(anchor="center", height=80, width=80, x=50, y=500)
        self.resetbutton.bind("<ButtonPress>", self.resetStepCounter)

        self.stepCount = ttk.Label(self.appFrame)
        self.stepCount.configure(anchor="center", background="#d6d6d6",
                                 font="{@Malgun Gothic Semilight} 12 {}", justify="center", text='0 / 0')
        self.stepCount.place(anchor="center", width=200, x=300, y=440)

        self.contributorsbutton = ttk.Button(self.appFrame)
        self.contributorsbutton.configure(cursor="hand2", text='Contributors')
        self.contributorsbutton.place(anchor="n", width=150, x=700, y=500)
        self.contributorsbutton.bind("<ButtonPress>", self.showContributors)

        self.solvebutton = ttk.Button(self.appFrame)
        self.solvebutton.configure(cursor="hand2", text='Solve')
        self.solvebutton.place(anchor="s", height=150, width=150, x=700, y=230)
        self.solvebutton.bind("<ButtonPress>", self.solve)

        self.algorithmbox = ttk.Combobox(self.appFrame)
        self.algorithmbox.configure(cursor="hand2", values=('BFS', 'DFS', 'A* Manhattan', 'A* Euclidean'))
        self.algorithmbox.place(anchor="center", height=30, width=150, x=700, y=260)
        self.algorithmbox.bind("<<ComboboxSelected>>", self.selectAlgorithm)

        self.cell0 = ttk.Label(self.appFrame)
        self.cell0.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text=' ')
        self.cell0.place(anchor="center", height=100, width=100, x=200, y=150)

        self.cell1 = ttk.Label(self.appFrame)
        self.cell1.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='1')
        self.cell1.place(anchor="center", height=100, width=100, x=300, y=150)

        self.cell2 = ttk.Label(self.appFrame)
        self.cell2.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='2')
        self.cell2.place(anchor="center", height=100, width=100, x=400, y=150)

        self.cell3 = ttk.Label(self.appFrame)
        self.cell3.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='3')
        self.cell3.place(anchor="center", height=100, width=100, x=200, y=250)

        self.cell4 = ttk.Label(self.appFrame)
        self.cell4.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='4')
        self.cell4.place(anchor="center", height=100, width=100, x=300, y=250)

        self.cell5 = ttk.Label(self.appFrame)
        self.cell5.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='5')
        self.cell5.place(anchor="center", height=100, width=100, x=400, y=250)

        self.cell6 = ttk.Label(self.appFrame)
        self.cell6.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='6')
        self.cell6.place(anchor="center", height=100, width=100, x=200, y=350)

        self.cell7 = ttk.Label(self.appFrame)
        self.cell7.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='7')
        self.cell7.place(anchor="center", height=100, width=100, x=300, y=350)

        self.cell8 = ttk.Label(self.appFrame)
        self.cell8.configure(anchor="center", background="#5aadad", borderwidth=3,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="sunken", text='8')
        self.cell8.place(anchor="center", height=100, width=100, x=400, y=350)

        self.enterstatebutton = ttk.Button(self.appFrame)
        self.enterstatebutton.configure(cursor="hand2", text='Enter initial state')
        self.enterstatebutton.place(anchor="n", width=150, x=700, y=290)
        self.enterstatebutton.bind("<ButtonPress>", self.enterInitialState)

        self.analysisbutton = ttk.Button(self.appFrame)
        self.analysisbutton.configure(cursor="hand2", text='Show search analysis')
        self.analysisbutton.place(anchor="n", width=150, x=700, y=330)
        self.analysisbutton.bind("<ButtonPress>", self.printSearchAnalysis)

        self.mainwindow = self.appFrame

    def run(self):
        app.displayStateOnGrid('000000000')
        self.updateGrid(self)
        self.mainwindow.mainloop()

    def prevSequence(self, event=None):
        global statepointer
        if statepointer > 0:
            self.stopFastForward()
            statepointer -= 1
            self.updateGrid(self)

    def nextSequence(self, event=None):
        global statepointer
        if statepointer < len(path) - 1:
            self.stopFastForward()
            statepointer += 1
            self.updateGrid(self)

    def solve(self, event=None):
        global algorithm, initialState
        if self.readyToSolve():
            self.resetGrid()
            print('Running ' + str(algorithm))
            self.solveState()
            if len(path) == 0:
                print('<!> Unsolvable State')
                messagebox.showinfo('Unsolvable!', 'The state you entered is unsolvable')
                initialState = None
                self.reset()
            else:
                print('<!> Solved!')
                self.updateGrid(self)
        else:
            print('Cannot solve.\n'
                  'Algorithm in use: ' + str(algorithm) + '\n'
                                                          'Initial State   : ' + str(initialState) + '\n-')

    def enterInitialState(self, event=None):
        global initialState, statepointer
        inputState = simpledialog.askstring('Initial State Entry', 'Please enter your initial state')
        if inputState is not None:
            if backend.validateState(inputState):
                initialState = inputState
                app.displayStateOnGrid(initialState)
                statepointer = 0
            else:
                print('Invalid initial state')
                messagebox.showerror('Input Error', 'Invalid initial state')

    def selectAlgorithm(self, event=None):
        global algorithm
        try:
            choice = self.algorithmbox.selection_get()
            self.reset()
            algorithm = choice
        except:
            print('Invalid algorithm selection')

    def showContributors(self, event=None):
        messagebox.showinfo('Contributors', "6744   -   Adham Mohamed Aly\n"
                                            "6905   -   Mohamed Farid Abdelaziz\n"
                                            "7140   -   Yousef Ashraf Kotp\n")

    def printSearchAnalysis(self, event=None):
        if self.solved():
            analytics = 'Analysis of ' + str(algorithm) + ' search\n'\
                  'initial state = ' + str(initialState) + '\n'\
                  '-------------------------------\n'\
                  'Nodes expanded: ' + str(counter) + '\n' + 'Search depth: ' + str(depth)
            print(analytics + '\n-')
            messagebox.showinfo('Analysis', analytics)

    def fastForward(self, event=None):
        global statepointer
        self.stopFastForward()
        if statepointer < cost:
            app.stopbutton.configure(state='enabled')
            statepointer += 1
            self.updateGrid(self)
            ms = 50
            if cost > 1000:
                ms = 1
            app._job = app.stepCount.after(ms, self.fastForward)
        else:
            self.stopFastForward()

    def fastBackward(self, event=None):
        global statepointer
        self.stopFastForward()
        if statepointer > 0:
            app.stopbutton.configure(state='enabled')
            statepointer -= 1
            ms = 50
            if cost > 1000:
                ms = 1
            app._job = app.stepCount.after(ms, self.fastBackward)
        else:
            self.stopFastForward()
        self.updateGrid(self)

    def stopFastForward(self, event=None):
        if app._job is not None:
            app.stopbutton.configure(state='disabled')
            app.stepCount.after_cancel(app._job)
            app._job = None



    def resetStepCounter(self, event=None):
        global statepointer
        if statepointer > 0:
            self.stopFastForward()
            statepointer = 0
            self.updateGrid(self)


    def displayStateOnGrid(self, state):
        if not backend.validateState(state):
            state = '000000000'
        self.cell0.configure(text=backend.adjustDigit(state[0]))
        self.cell1.configure(text=backend.adjustDigit(state[1]))
        self.cell2.configure(text=backend.adjustDigit(state[2]))
        self.cell3.configure(text=backend.adjustDigit(state[3]))
        self.cell4.configure(text=backend.adjustDigit(state[4]))
        self.cell5.configure(text=backend.adjustDigit(state[5]))
        self.cell6.configure(text=backend.adjustDigit(state[6]))
        self.cell7.configure(text=backend.adjustDigit(state[7]))
        self.cell8.configure(text=backend.adjustDigit(state[8]))

    @staticmethod
    def readyToSolve():
        return initialState is not None and algorithm is not None

    @staticmethod
    def solved():
        return len(path) > 0

    @staticmethod
    def solveState():
        global path, cost, counter, depth
        if str(algorithm) == 'BFS':
            main.BFS(initialState)
            path, cost, counter, depth = main.bfs_path, main.bfs_cost, main.bfs_counter, main.bfs_depth
        elif str(algorithm) == 'DFS':
            main.DFS(initialState)
            path, cost, counter, depth = main.dfs_path, main.dfs_cost, main.dfs_counter, main.dfs_depth
        elif str(algorithm) == 'A* Manhattan':
            main.AStarSearch_manhattan(initialState)
            path, cost, counter, depth = main.manhattan_path, main.manhattan_cost, main.manhattan_counter, main.manhattan_depth
        elif str(algorithm) == 'A* Euclidean':
            main.AStarSearch_euclid(initialState)
            path, cost, counter, depth = main.euclid_path, main.euclid_cost, main.euclid_counter, main.euclid_depth
        else:
            print('Error occurred')

    def resetGrid(self):
        global statepointer
        statepointer = 0
        self.updateGrid(self)
        app.stepCount.configure(text=self.getStepCount())

    def reset(self):
        global statepointer, path, cost, counter
        statepointer = cost = counter = 0
        path = []
        self.resetGrid()

    @staticmethod
    def getStepCount():
        return str(statepointer) + ' / ' + str(cost)

    @staticmethod
    def updateGrid(self):
        if cost > 0:
            state = main.getStringRepresentation(path[statepointer])
            app.displayStateOnGrid(state)
            app.stepCount.configure(text=self.getStepCount())
        if statepointer == 0:
            app.resetbutton.configure(state='disabled')
            app.backbutton.configure(state='disabled')
            app.fastbackwardbutton.configure(state='disabled')
        elif statepointer == cost:
            app.backbutton.configure(state='disabled')
        else:
            app.resetbutton.configure(state='enabled')
            app.backbutton.configure(state='enabled')
            app.fastbackwardbutton.configure(state='enabled')

        if cost == 0 or statepointer == cost:
            app.fastforwardbutton.configure(state='disabled')
            app.nextbutton.configure(state='disabled')
        else:
            app.fastforwardbutton.configure(state='enabled')
            app.nextbutton.configure(state='enabled')



if __name__ == "__main__":
    global app
    root = tk.Tk()
    root.title('8-Puzzle Solver')
    app = InterfaceApp(root)
    app.run()
