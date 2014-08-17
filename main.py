import time
from splinter import Browser
from tkinter import *

class testconfig():
    runs = 3
    timeout = 5
    totaltime = 0
    loadtime = 0
    loadstart = 0

config = testconfig()

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
        config.totaltime = 0
        writetoresults("Firefox run on " + str(time.strftime("%d/%m/%Y")) + " at " + str(time.strftime("%H:%M:%S") + "\n"))
        i = 0
        f = 0
        timer = time.clock()
        while i < config.runs:
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
        writetoresults("Total time," + str(endtimer - timer) + "\n\n")
        totaltime = endtimer - timer
        writetoresults("Total time," + str(endtimer - timer) + ",Average," + str(totaltime/config.runs) + "\n\n")
        FFtimelabel.config(text = "This test ran " + str(config.runs) + " times Firefox completed at: " + str(totaltime) + " and failed " + str(f) + " times. Average time of " + str(totaltime/config.runs))

def chrometest():
    with Browser("chrome") as browser:
        config.totaltime = 0
        writetoresults("Chrome run on " + str(time.strftime("%d/%m/%Y")) + " at " + str(time.strftime("%H:%M:%S") + "\n"))
        i = 0
        f = 0
        timer = time.clock()
        while i < config.runs:
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
        writetoresults("Total time," + str(endtimer - timer) + ",Average," + str(totaltime/config.runs) + "\n\n")
        CHtimelabel.config(text = "This test ran " + str(config.runs) + " times, Chrome completed at " + str(totaltime) + " and failed " + str(f) + " times. Average time of " + str(totaltime/config.runs))

def clearText():
    CHtimelabel.config(text = "")
    FFtimelabel.config(text = "")


root = Tk()
root.minsize(800,100)
root.resizable(width=FALSE, height=FALSE)
clear = Button(root, text="Clear", command=clearText)
clear.pack()
fftest = Button(root, text="Run in FireFox", command=firefoxtest)
fftest.pack()
chtest = Button(root, text="Run in Chrome", command=chrometest)
chtest.pack()
FFtimelabel = Label(root)
FFtimelabel.pack()
CHtimelabel = Label(root)
CHtimelabel.pack()
mainloop()