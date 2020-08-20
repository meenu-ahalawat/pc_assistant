'''this is meenu's python code'''
'''imported os library for running applications installed in our system'''
'''imported webbrowser library for making online searches'''

import os
import webbrowser

print("Chat with me with your requirements:")
p = input()

if ("search" in p) and (("google" in p) or ("chrome" in p)):
    webbrowser.open("https://google.com/?#q=" + p)

elif (("search" in p) or ("play" in p)) and ("youtube" in p):
    webbrowser.open("https://www.youtube.com/results?search_query=" + p)

elif (("search" in p) or ("play" in p)) and ("on youtube" in p):
    webbrowser.open("https://www.youtube.com/watch?v=" + p)

elif (("run" in p) or ("open" in p) or ("start" in p)) and (("notepad" in p) or ("editor" in p)):
    os.system("notepad")

elif (("run" in p) or ("open" in p) or ("start" in p)) and ("chrome" in p):
    os.system("chrome")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (("explorer" in p) or ("internet explorer" in p)):
    os.system("explorer")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (("mpc" in p) or ("media player" in p)):
    os.system("mpc-hc64")

elif (("run" in p) or ("open" in p) or ("start" in p)) and ("vlc" in p):
    os.system("vlc")


elif (("run" in p) or ("open" in p) or ("start" in p)) and ("skype" in p):
    os.system("skype")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (("calculator" in p) or ("calc" in p)):
    os.system("calc")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (
        ("excel" in p) or ("microsoft excel" in p) or ("ms excel" in p)):
    os.system("excel")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (("winword" in p) or ("word" in p)):
    os.system("winword")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (("ms access" in p) or ("microsoft access" in p)):
    os.system("msaccess")

elif (("run" in p) or ("open" in p) or ("start" in p)) and (
        ("powerpoint" in p) or ("microsoft powerpoint" in p) or ("ms powerpoint" in p) or ("ms power point" in p)):
    os.system("powerpnt")

else:
    print("don't support")
