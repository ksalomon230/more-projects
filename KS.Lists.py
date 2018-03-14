import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=qZLs7BHhduA"]

music = ["https://www.youtube.com/watch?v=miTPOX3kQZk"]


answer = pg.prompt(
"""
what do you want to do?
a) videos
b) music

"""

    )
if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
