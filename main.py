import time
import os
from splinter import Browser
from tkinter import *

def deletefile():
    os.remove("results.csv")

def writetoresults(towrite):
    with open("results.csv", "a") as results:
        results.write(towrite)

def testrunner(methods):
    fails = 0
    methodno = 0
    for method in methods:
        methodno = methodno + 1
        try:
            method
        except:
            fails += 1
    return fails

def firefoxtest():
    with Browser() as browser:
        runs = int(runentry.get())
        writetoresults("Firefox run on " + str(time.strftime("%d/%m/%Y")) + " at " + str(time.strftime("%H:%M:%S") + "\n"))
        i = 0
        f = 0
        timer = time.clock()
        while i < runs:
            runstart = time.clock()
            f = f + testrunner([
                browser.visit("https://m.quote.comparethemarket.com/car/newquote/?AFFCLIE=CM01"),
                browser.find_by_id("registration-number").fill("A1"),
                browser.find_by_id("find-vehicle-by-reg").click(),
                browser.is_text_present("What type of alarm and/or immobiliser does your car have?"),
                browser.find_by_id("vehicle-lookup-next").click(),
                browser.is_text_present("When did you buy the car?")])
            runend = time.clock()
            writetoresults("Test run " + str(i) + " total time," + str(runend - runstart) + "\n")
            i = i + 1
        endtimer = time.clock()
        totaltime = endtimer - timer
        writetoresults("Total time," + str(endtimer - timer) + ",Average," + str(totaltime/runs) + "\n\n")
        FFtimelabel.config(text = "This test ran " + str(runs) + " times Firefox completed at: " + str(totaltime) + " and failed " + str(f) + " times. Average time of " + str(totaltime/runs))

def chrometest():
    with Browser("chrome") as browser:
        runs = int(runentry.get())
        writetoresults("Chrome run on " + str(time.strftime("%d/%m/%Y")) + " at " + str(time.strftime("%H:%M:%S") + "\n"))
        i = 0
        f = 0
        timer = time.clock()
        while i < runs:
            runstart = time.clock()
            f = f + testrunner([
                browser.visit("https://m.quote.comparethemarket.com/car/newquote/?AFFCLIE=CM01"),
                browser.find_by_id("registration-number").fill("A1"),
                browser.find_by_id("find-vehicle-by-reg").click(),
                browser.is_text_present("What type of alarm and/or immobiliser does your car have?"),
                browser.find_by_id("vehicle-lookup-next").click(),
                browser.is_text_present("When did you buy the car?")])
            runend = time.clock()
            writetoresults("Test run " + str(i) + " total time," + str(runend - runstart) + "\n")
            i = i + 1
        endtimer = time.clock()
        totaltime = endtimer - timer
        writetoresults("Total time," + str(endtimer - timer) + ",Average," + str(totaltime/runs) + "\n\n")
        CHtimelabel.config(text = "This test ran " + str(runs) + " times, Chrome completed at " + str(totaltime) + " and failed " + str(f) + " times. Average time of " + str(totaltime/runs))

def clearText():
    CHtimelabel.config(text = "")
    FFtimelabel.config(text = "")


root = Tk()
root.minsize(800,100)
root.resizable(width=FALSE, height=FALSE)
toolbar = Frame(root)
clear = Button(toolbar, text="Delete results file", command=deletefile)
clear.pack({"side": "left"})
clear = Button(toolbar, text="Clear", command=clearText)
clear.pack({"side": "left"})
fftest = Button(toolbar, text="Run in FireFox", command=firefoxtest)
fftest.pack({"side": "left"})
chtest = Button(toolbar, text="Run in Chrome", command=chrometest)
chtest.pack({"side": "left"})
Label(toolbar, text="Runs: ").pack({"side": "left"})
runentry = Entry(toolbar, width=3)
runentry.insert(0, "3")
runentry.pack({"side": "left"})
toolbar.pack()

FFtimelabel = Label(root)
FFtimelabel.pack()
CHtimelabel = Label(root)
CHtimelabel.pack()
mainloop()