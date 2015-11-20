def greet():
	s = 'hello'
	def f(x):
		return s + ', ' + x
	return f

say_hi = greet()
print(say_hi('Fred'))



class Hello(Frame):

	languages = ['English', 'French', 'Spanish']

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.pack()

		self._msg = Label(self, text='', height=3, width=20, font=('Helvetica', '24'))
		self._msg.pack()

	for x in Hello.languages:
		def cb(language=x):
			Button(self, text=x, command=lambda x=x: self.say_hi(x).pack())

	def say_hi(self, lang):
		self.msg.configure(text=Hello.languages[lang])