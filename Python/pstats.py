"""
   David Gustafson pstats.py
   CIS 211, Spring 2014

   A program that computes basic stats about an inputted LaTeX project. 
"""
import sys
import os

location = sys.argv[1]
# res = os.system(cmnd)
# res = os.popen(cmnd)

res = list(os.popen('wc Number1/Federalist1.tex'))
s = res[0]
print(list(map(int, s.split()[:3])))

# cmnd = r"grep '\\chapter' {}".format(location)
# res = os.system(cmnd)
# print(res)

# for line in os.walk(location):
# 	top, folder, files = line
# 	for item in files:
# 		if os.path.splitext(item)[1] == '.tex'