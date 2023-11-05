#!/usr/bin/python3

import ProxySetter.ProxySetter as ProxySetter
import sys

def main():
    ps = ProxySetter("localhost", "8888")
    while 1:
        date = input("Enter a date: ") 
        
        try:
            ps.changeDate(date)
        except: 
            print('failed to change the date')

if __name__ == '__main__': 
    main()