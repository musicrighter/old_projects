from test_harness import *

def normalize(li):
	new_list = []
	if li == []:
		return li
	prev_begin, prev_end, prev_desc = li[0]
	for i in li[1:]:
		begin, end, desc = i:
		if prev_end <= begin:
			new_list.append((prev_begin, prev_end, prev_desc))
			prev_begin, prev_end, prev_desc = i
		else:
			prev_end = end
			prev_desc += ';' + desc
	new_list.append((prev_begin, prev_end, prev_desc))
	return new_list

def unit_tests():
	m = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C'), (7, 9, 'D'), (8, 10, 'E')]

	testEQ('Simple smoke test, already sorted',
		normalize(m),
		[(1,4,'A;B'), (5,7,'C'), (7,10,'D;E')])

if __name__ == '__main__':
	unit_tests()