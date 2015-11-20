import sys

DS = 'darkened-skin'
EF = 'exposed-flesh'
BS = 'bone-seen'
LH = 'like-human'

class Sample:
	def __init__(self, sample_list):
		"""Create a sample object with a list containing zdogs or zombies
		Arguments:
			sample_list: a list containing zdogs or zombies or both
        """
		self.sample_batch = sample_list
		
	def sort(self):
		"""Sort sample_batch in nonincreasing order, notice error happens if we try to
		sort a mixed sample, because we can't compare a normal zombie with a zdog so we must 
		categorize before sorting
		"""
		
		#sort function is implemented for you, but read this function still.
		#this double for loop is exactly where the __ls__ function is IMPLICITLY called, try to
		#figure out where the calling happens 
		def bubble_sort(list):
			for i in range(len(list)):
				for j in range(i, len(list)):
					if list[i] < list[j]:
						pass
					else:
						temp = list[i]
						list[i] = list[j]
						list[j] = temp
			return list
						
		self.sample_batch = bubble_sort(self.sample_batch)
		return 
		
	def categorize(self):
		"""categorize the sample and return two samples, first one is zombie sample, second one is zdog sample
		"""
		zdog_list = []
		zombie_list = []
		#FIXME
		#hint you can use item.__class__.__name__ to refer to the name of an object's class
				
		return Sample(zombie_list), Sample(zdog_list)
		
	def __str__(self):
		"""string representation of a sample object
		"""
		sample_str = ''
		for item in self.sample_batch:
			sample_str = sample_str + str(item)
		return sample_str

class Zdog:
	def __init__(self, length, weight, infec_level):
		"""Create an zombie-dog object associated with length, weight, rot_level
		Arguments:
			length: an float num
			weight: an float num
			infection_level: a string describing the level to which the zombie has rotten:
			DS for 'darkened-skin', EF for 'exposed-flesh', BS for 'bone-seen' 
        """
		self.length = length
		self.weight = weight
		self.infec_level = infec_level
		
	def __str__(self):
		"""String representation of a zdog.
		Example:
			length: 4.0 | weight: 32 | infec_level: bone seen
			after rewriting this function we can directly use print() function upon objects of
			this class, for print() implicitly calls str()
		"""
		length = str(self.length)
		weight = str(self.weight)
		infec_level = self.infec_level
		
		return 'Zdog: '+'length: '+length+' | '+'weight: '+weight+' | '+'infection level: '+ infec_level + '\n'
		
	def __lt__(self, other):
		""" we compare several properties of zdog, first its length; then weight if heights are the 
			same; then infec_level if weights are same.
			Infection levels should be sorted as follows: 
			'darkened-skin' < 'exposed-flesh' < 'bone-seen'
		"""
		#FIXME
		
class Zombie:
	def __init__(self, height, weight, infec_level):
		"""Create an zombie object associated with height, weight, rot_level
		Arguments:
			height: an float num
			weight: an float num
			infection_level: a string describing the level to which the zombie has rotten:
			LH for 'like-human', EF for 'exposed-flesh', BS for 'bone-seen' 
			
        """
		self.height = height
		self.weight = weight
		self.infec_level = infec_level
		
	def __str__(self):
		"""String representation of a zombie.
		Example:
			height: 6.4 | weight: 145 | infec_level: bone seen
			after rewriting this function we can directly use print() function upon objects of
			this class, for print() implicitly calls str()
		"""
		height = str(self.height)
		weight = str(self.weight)
		infec_level = self.infec_level
		
		return 'Zombie: '+'height: '+height+' | '+'weight: '+weight+' | '+'infection level: '+ infec_level+ '\n'
		
	def __lt__(self, other):
		""" we compare several properties of zombie, first its height; then weight if heights are the 
			same; then infec_level if weights are the same.
			Infection levels should be sorted as follows: 
			'like-human' < 'exposed-flesh' < 'bone-seen'
		"""
		
		#FIXME 
		
	
if __name__ == "__main__":

	sample_txt = open(sys.argv[1])
	sample_list = []
	
	for item in sample_txt:
		#we instantiate either zombie or zdog depending on the type, specified by the first word 
		#in every line from input file
		item = item.split()
		if item[0] == 'zdog':
			item = Zdog(item[1], item[2], item[3])
		else:
			item = Zombie(item[1], item[2], item[3])
			
		sample_list.append(item)
		
	#first we make the mixed sample, then we call categorize() to classify it into two 'pure' samples
	mixed_sample = Sample(sample_list)
	zombie_sample, zdog_sample = mixed_sample.categorize() 
		
	#sort each sample
	zombie_sample.sort()
	zdog_sample.sort()
	
	#print the result
	print('zombie sample:')
	print(zombie_sample)
	print('zombie dog sample:')
	print(zdog_sample)
	
    
