# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:03:11 2020

@author: Adi

Adapted from:
https://stackoverflow.com/questions/48289636/speedtest-python-script
"""

# ---------------------------------------------
# Instal speedtest: 'pip install speedtest-cli'
# ---------------------------------------------
import speedtest
from datetime import datetime

'''
set the number of tests that will be performed
on my connection, one test is 28 seconds on average
for one hour of testing, set the number to 129
'''
no_tests = 500

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    # write to csv
    with open('speed_test.csv', 'w') as f:
        f.write('time,download,upload,ping\n')
        for i in range(no_tests):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            f.write(current_time+',')
            f.write('{},{},{}\n'.format(d/1000000, u/1000000, p))
    f.close()
    # # pretty write to txt file
    # with open('file.txt', 'w') as f:
    #     for i in range(3):
    #         print('Making test #{}'.format(i+1))
    #         d, u, p = test()
    #         f.write('Test #{}\n'.format(i+1))
    #         f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
    #         f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
    #         f.write('Ping: {}\n'.format(p))
    # # simply print in needed format if you want to use pipe-style: python script.py > file
    # for i in range(3):
    #     d, u, p = test()
    #     print('Test #{}\n'.format(i+1))
    #     print('Download: {:.2f} Kb/s\n'.format(d / 1024))
    #     print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
    #     print('Ping: {}\n'.format(p))


if __name__ == '__main__':
    main()