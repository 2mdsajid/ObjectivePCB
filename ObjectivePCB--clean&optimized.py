import random, os

class Objective():
	
	wrong, right, skip = 0, 0, 0
	index, wrongQn = [], []
	
	def __init__(self, qn, a, b, c, d, ans):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.que = qn
		self.an = ans
		self.qn = open(qn).readlines()
		self.ans = open(ans).readlines()
		self.set = (a, b, c, d)
	
	def getAnswer(self, r):
		return self.ans[r].strip()
	
	def questionNumber(self):
		return Objective.skip+Objective.right+Objective.wrong+1

	def getIndex(q,list):
		while True:
			r = random.randint(1,len(q)-1)
			if r not in list:
				list.append(r)
				return r
			return r

	def rightAnswer(self, r):
		if Objective.getAnswer(self, r) == "a":
			return open(self.a).readlines()
		elif Objective.getAnswer(self, r) == "b":
			return open(self.b).readlines()
		elif Objective.getAnswer(self, r) == "c":
			return open(self.c).readlines()
		else: return open(self.d).readlines()

	def printWrongAnswers(self):
		quiz = False
		for el in Objective.wrongQn:
			r = el[0]
			qNum = el[1]
			Objective.printTheQuestions(self, r, qNum, quiz)
			
	def getTheQuestions(self):
		quiz = True
		r = Objective.indexGet(self.qn, Objective.index)
		qNum = Objective.questionNumber(self)
		print(Objective.index)
		Objective.printTheQuestions(self, r, qNum, quiz)
		
	
	def printTheQuestions(self, r, qNum, quiz):
		print(f"\n{qNum}. {self.qn[r].capitalize().strip()} ")
		for el in self.set:
			print(open(el).readlines()[r].strip())
		
		if quiz:
			Objective.getUserAnswer(self, r, qNum)
			os.system("clear")
		else:
			print(f"Right Ans : {Objective.rightAns(self,r)[r].strip()}")
		
	def getUserAnswer(self, r, qNum):
		ans = input("\nanswer ? ").lower()
		if ans == Objective.answer(self,r):
			Objective.right += 1
		elif ans == "":
			Objective.skip += 1
		elif ans == "e":
			remark()
			exit()
		else:
			Objective.wrong += 1
			Objective.wrongQn += [(r,qNum)]
	
	def questionEntry(self):
		op, po = ["a","b","c","d"], []
		q = input("Question : ")
		for el in op:
			po += [input(f"opt {el} : ")]
		while True:
			an = input("Ans : ")
			if an not in op:
				print("Put Option ! ")
			else: break

		open(self.que,"a").write("\n{}".format(q))
		open(self.an, "a").write("\n{}".format(an))
		for a,b,c in zip(op, po, self.set):
			open(c, "a").write("\na) {}".format(b))
			print("Question added !")
			dec = input("more (y/n) ? ")
			if dec != "n":
				os.system("clear")
				Objective.questionEntry(self)
			else: exit()
			
		

physics = Objective("pqn.txt","pa.txt","pb.txt","pc.txt","pd.txt","pans.txt")
biology = Objective("question.txt","a.txt","b.txt","c.txt","d.txt","ans.txt")
chemistry = Objective("cqn.txt","ca.txt","cb.txt","cc.txt","cd.txt","cans.txt")


def remark(wrong, right, skip, name):
	os.system('clear')
	print(f"\nREMARKS OF MR. {name.upper()}")
	print(f'Total questions attempted = {right+wrong+skip}')
	print(f'Wrong = {wrong}')
	print(f'Right = {right}')
	print(f'Questions skipped = {skip}\n')
	if wrong > right: 
		print("You need to work hard !\n")
	else:
		print("Don't be overconfident !\n")
		
def userChoice():
	return input("\n> ").lower()

def startPractice(choice):
	if choice == "a":
		return biology.start()
	elif choice == "b":
		return chemistry.start()
	else: return physics.start()

def questionsLimit():
	limit = input("Qn limit ? ")
	if limit == "":
		return 50
	return int(limit)

def wrongQuestions(choice):
	 if choice == "a":
	 	return biology.wrongPost()
	 elif choice == "b":
	 	return chemistry.wrongPost()
	 else: return physics.wrongPost()


def questionEntrySubject(choice):
	 os.system('clear')
	 print("Write the question, options and the answer respectively !\n")
	 if choice == "b":
	 	return biology.questionEntry()
	 elif choice == "c":
	 	return chemistry.questionEntry()
	 else: return physics.questionEntry()

def questionsPractice():
	wrList = []
	os.system('clear')
	print("""Choose :
a) Biology
b) Chemistry
c) Physics
	""")
	choice = userChoice()
	limit = questionsLimit()
	name = input("Your name > ")
	
	os.system('clear')
	print(f'\nHello {name.upper()} ! You have {limit} questions, each \ncarrying one mark. You have no time limits.\n\n(PS : You can press "e" anytime to exit :) )\n')
	fin = input("Are you ready (y/n) ? ")
	if fin == "n":
		os.system('clear')
		print(f"Oe looser {name} padh gayera natra naam niskanna yesai !")
		exit()

	for a in range(limit):
		startPractice(choice)
	remark(Objective.wrong,Objective.right,Objective.skip, name)
	print("\nYour wrong answers are : ")
	wrongQuestions(choice)
	again = input("\nMore (y/n) ? ")
	if again != "y":
		print("Thanks for using it !")
		exit()
	else: questionsPractice()
	

print("OBJECTIVE QUESTIONS PRACTICE")
print("\nPractice(a) or Entry(b) ? ")
if userChoice() == "a":
	questionsPractice()
else:
	os.system('clear')
	print("""Choose :
a) Physics
b) Biology
c) Chemistry
	""")
	questionEntrySubject(userChoice())