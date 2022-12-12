import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    ORANGE_AND_RED = curses.color_pair(3)


    stdscr.attron()
    rectangle(stdscr, 1,1, 5,20)
    stdscr.attroff(BLUE_AND_YELLOW)
    stdscr.refresh()



    stdscr.getch()

wrapper(main)