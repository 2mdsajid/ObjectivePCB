import random

def clear():
	import os
	os.system( 'clear' )


def remarks():
	clear()		
	
	#try:
#		if sj == "d":
#			hist = open("history.txt","a")
#			hist.write("{}".format(wrong/right))
#			hist.close()
#	except:
#		print("Bring some Improvements")
	
	
	print(f"\nREMARKS OF MR. {name.upper()}")
	print(f'Total questions attempted = {str(right+wrong+skip)}')
	print(f'Wrong = {str(wrong)}')
	print(f'Right = {str(right)}')
	print(f'Questions skipped = {str(skip)}\n')
	if wrong > right: 
		print("You need to work hard !\n")
	else:
		print("Don't be overconfident !\n")
	#hist = open("history.txt","r")
#	el = hist.readlines()
#	if len(el) != 0:
#		print("\nPrevious statistics !")
#		sum = 0
#		for nn in el:
#			sum += int(nn)
#		print(sum)
#		av = (sum/len(el))
#		if (wrong/right) < av:
#			print("Improvement seen !")
#		else: print("Work hard")
#	else:
#		print("first test")



	if wrong != 0:
		print("Your wrong answers were :- \n")
		for q in w: #GET WRONG QNS
			print(q)
			#wr = open("wrong.txt","w")
#			wr.write("{}\n".format(q))
#			wr.close() 	
		else:
			print("Well done")
		
	re = input("\nWanna more(y/n) ")
	if re == 'y' or re == "":
		start()
	else:
		print("Thank you")
		exit() 
	exit()



#def fvrt():
#	active = True
#	while active:
#		fquestion = open("fquestion.txt","a")
#		fa = open("fa.txt","a")
#		fb = open("fb.txt","a")
#		fc = open("fc.txt","a")
#		fd = open("fd.txt","a")
#		fans = open("fans.txt","a")
#						
#		question.write("\n{}".format(que))
#		a.write("\na) {}".format(aa))
#		b.write("\nb) {}".format(bb))
#		c.write("\nc) {}".format(cc))
#		d.write("\nd) {}".format(dd))
#		ans.write("\n{}".format(anss))
#		print("Question added ! ")


class Bio():
	def b_qp():
		active=True  #FOR LOOPING
		question = open("question.txt")
		a = open("a.txt")
		b = open("b.txt")
		c = open("c.txt")
		d = open("d.txt")
		ans = open("ans.txt")
		que = question.readlines()
		aa = a.readlines()
		bb = b.readlines()
		cc = c.readlines()
		dd = d.readlines()
		anss = ans.readlines()
		global wrong, n
		n = 1
		wrong = 0
		global right,skip
		right = 0
		skip = 0
		global list
		#flist=[]
		list=[] #LIMITING RANDOM
		global w
		w =[]
		ql = int(input("Questions limit = "))
		while active: 
			if right+wrong+skip == (ql):
				active=False
			else: active=True
			question = open("question.txt","r")
			length = len(question.readlines()) - 1
			r = random.randint(1,length)
			if r not in list:
				list.append(r)
				print(f"{n}. {que[r].capitalize().strip()} ")
				print(aa[r].strip())
				print(bb[r].strip())
				print(cc[r].strip())
				print(dd[r].strip())
				answer = input("\nanswer ? "). lower()
				if answer == anss[r].strip():
					right += 1
					n += 1
					clear()	
				elif answer == "e": #TO QUIT
					clear()
					remarks()
				#elif answer== "f":
#					fvrt()
				elif answer=="s" or answer=="":
					skip += 1
					n+=1
					clear()
				#elif answer == "f":
					
				else:
					w.append(que[r].strip())
					w.append(aa[r].strip())
					w.append(bb[r].strip())
					w.append(cc[r].strip())
					w.append(dd[r].strip())
					if anss[r].strip() == "a":
						w.append("Ans : {}\n".format(aa[r].strip()))
					elif anss[r].strip() == "b":
						w.append("Ans : {}\n".format(bb[r].strip()))
					elif anss[r].strip() == "c":
						w.append("Ans : {}\n".format(cc[r].strip()))
					elif anss[r].strip() == "d":
						w.append("Ans : {}\n".format(dd[r].strip()))
					wrong += 1
					n += 1
					clear()
		remarks()
	
			
	#INITIATE QN ENTRY
	def b_qe():
		active = True
		while active:
			question = open("question.txt","a")
			a = open("a.txt","a")
			b = open("b.txt","a")
			c = open("c.txt","a")
			d = open("d.txt","a")
			ans = open("ans.txt","a")
							
			question.write("\n{}".format(que))
			a.write("\na) {}".format(aa))
			b.write("\nb) {}".format(bb))
			c.write("\nc) {}".format(cc))
			d.write("\nd) {}".format(dd))
			ans.write("\n{}".format(anss))
			print("Question added ! ")
			m = input("\nmore (y/n) ? ")
			if m == "n":
				exit()
			elif m == "y":
				com_e()
				


class Phy():
	def p_qp():
		active=True  
		p_qn = open("pqn.txt")
		p_a = open("pa.txt")
		p_b = open("pb.txt")
		p_c = open("pc.txt")
		p_d = open("pd.txt")
		p_ans = open("pans.txt")
		p_que = p_qn.readlines()
		p_aa = p_a.readlines()
		p_bb = p_b.readlines()
		p_cc = p_c.readlines()
		p_dd = p_d.readlines()
		p_anss = p_ans.readlines()
		global wrong, n
		wrong=0
		n = 1
		global right,skip
		right = 0
		skip = 0
		global plist
		#flist=[]
		plist=[] #LIMITING RANDOM
		global w
		w =[] #EPPEND WRONG QN
		ql = int(input("Questions limit = "))
		while active: 
			if right+wrong+skip == (ql):
				active=False
			else: active=True
			p_qn = open("pqn.txt","r")
			length = len(p_qn.readlines()) - 1
			r = random.randint(1,length)
			if r not in plist:
				plist.append(r)
				print(f"{n}. {p_que[r].capitalize().strip()} ")
				print(p_aa[r].strip())
				print(p_bb[r].strip())
				print(p_cc[r].strip())
				print(p_dd[r].strip())
				p_answer = input("\nanswer ? ").lower()
				if p_answer ==p_anss[r].strip():
					right += 1
					n += 1
					clear() 	
				elif p_answer == "e": 
					clear()
					remarks()
				elif p_answer=="s" or p_answer == "":
					skip += 1
					n += 1
					clear()
				else:
					w.append(p_que[r].strip())
					w.append(p_aa[r].strip())
					w.append(p_bb[r].strip())
					w.append(p_cc[r].strip())
					w.append(p_dd[r].strip())
					if p_anss[r].strip() == "a":
						w.append("Ans : {}\n".format(p_aa[r].strip()))
					elif p_anss[r].strip() == "b":
						w.append("Ans : {}\n".format(p_bb[r].strip()))
					elif p_anss[r].strip() == "c":
						w.append("Ans : {}\n".format(p_cc[r].strip()))
					elif p_anss[r].strip() == "d":
						w.append("Ans : {}\n".format(p_dd[r].strip()))
					wrong += 1
					n += 1
					clear() 
		remarks()	
			
	#INITIATE QN ENTRY
	def p_qe():
		active = True
		while active:
			
			p_qn = open("pqn.txt","a")
			p_a = open("pa.txt","a")
			p_b = open("pb.txt","a")
			p_c = open("pc.txt","a")
			p_d = open("pd.txt","a")
			p_ans = open("pans.txt","a")
			
			p_qn.write("\n{}".format(que))
			p_a.write("\na) {}".format(aa))
			p_b.write("\nb) {}".format(bb))
			p_c.write("\nc) {}".format(cc))
			p_d.write("\nd) {}".format(dd))
			p_ans.write("\n{}".format(anss))
			print("Question added ! ")
			m = input("\nmore (y/n) ? ")
			if m != "y":
				exit()
			else:
				com_e()
		
				
				


class Chem():
	def c_qp():
		active=True  
		c_qn = open("cqn.txt")
		c_a = open("ca.txt")
		c_b = open("cb.txt")
		c_c = open("cc.txt")
		c_d = open("cd.txt")
		c_ans = open("cans.txt")
		c_que = c_qn.readlines()
		c_aa = c_a.readlines()
		c_bb = c_b.readlines()
		c_cc = c_c.readlines()
		c_dd = c_d.readlines()
		c_anss = c_ans.readlines()
		global wrong, n
		n = 1
		wrong = 0
		global right,skip
		right = 0
		skip = 0
		global clist
		#flist=[]
		clist=[] 
		global w
		w =[] 
		ql = int(input("Questions limit = "))
		while active: 
			if right+wrong+skip == (ql):
				active=False
			else: active=True 
			c_qn = open("cqn.txt","r")
			length = len(c_qn.readlines()) - 1
			r = random.randint(1,length)
			if r not in clist:
				clist.append(r)
				print(f"{n}. {c_que[r].capitalize().strip()} ")
				print(c_aa[r].strip())
				print(c_bb[r].strip())
				print(c_cc[r].strip())
				print(c_dd[r].strip())
				c_answer = input("\nanswer ? ").lower()
				if c_answer ==c_anss[r].strip():
					right += 1
					n += 1
					clear()
				elif c_answer == "e":
					clear() 
					remarks()
				elif c_answer=="s" or c_answer == "":
					skip += 1
					n += 1
					clear()
				else:
					w.append(c_que[r].strip())
					w.append(c_aa[r].strip())
					w.append(c_bb[r].strip())
					w.append(c_cc[r].strip())
					w.append(c_dd[r].strip())
					if c_anss[r].strip() == "a":
						w.append("Ans : {}\n".format(c_aa[r].strip()))
					elif c_anss[r].strip() == "b":
						w.append("Ans : {}\n".format(c_bb[r].strip()))
					elif c_anss[r].strip() == "c":
						w.append("Ans : {}\n".format(c_cc[r].strip()))
					elif c_anss[r].strip() == "d":
						w.append("Ans : {}\n".format(c_dd[r].strip()))
					wrong += 1
					n += 1
					clear() 
		remarks()
		
			
			
	#INITIATE QN ENTRY
	def c_qe():
		active = True
		while active:
			c_qn = open("cqn.txt","a")
			c_a = open("ca.txt","a")
			c_b = open("cb.txt","a")
			c_c = open("cc.txt","a")
			c_d = open("cd.txt","a")
			c_ans = open("cans.txt","a")
							
			c_qn.write("\n{}".format(que))
			c_a.write("\na) {}".format(aa))
			c_b.write("\nb) {}".format(bb))
			c_c.write("\nc) {}".format(cc))
			c_d.write("\nd) {}".format(dd))
			c_ans.write("\n{}".format(anss))
			print("Question added ! ")
			m = input("\nmore (y/n) ? ")
			if m != "y":
				exit()
			else:
				com_e()



class Common():				
		def com():
			global right,skip,wrong,w,n
			right=0
			skip = 0
			wrong=0
			w=[]
			n = 1
			#ql=int(input("Questions limit ? "))
			active=True  #FOR LOOPING
			question = open("question.txt")
			a = open("a.txt")
			b = open("b.txt")
			c = open("c.txt")
			d = open("d.txt")
			ans = open("ans.txt")
			que = question.readlines()
			aa = a.readlines()
			bb = b.readlines()
			cc = c.readlines()
			dd = d.readlines()
			anss = ans.readlines()
			global list
			list=[] 
			while active: 
				if right+wrong+skip == 24:
					active=False
				quest = open("question.txt","r")
				leng = len(quest.readlines()) - 1
				r = random.randint(1,leng)
				if r not in list:
					list.append(r)
					print(f"{n}. {que[r].capitalize().strip()} ")
					print(aa[r].strip())
					print(bb[r].strip())
					print(cc[r].strip())
					print(dd[r].strip())
					answer = input("\nanswer ? ").lower()
					if answer == anss[r].strip():
						right += 1
						n += 1
						clear()	
					elif answer == "e": #TO QUIT
						remarks()
						clear()
					elif answer=="s" or answer=="":
						n += 1
						skip += 1
						clear()
					else:
						w.append(que[r].strip())
						w.append(aa[r].strip())
						w.append(bb[r].strip())
						w.append(cc[r].strip())
						w.append(dd[r].strip())
						if anss[r].strip() == "a":
							w.append("Ans : {}\n".format(aa[r].strip()))
						elif anss[r].strip() == "b":
							w.append("Ans : {}\n".format(bb[r].strip()))
						elif anss[r].strip() == "c":
							w.append("Ans : {}\n".format(cc[r].strip()))
						elif anss[r].strip() == "d":
							w.append("Ans : {}\n".format(dd[r].strip()))
						wrong += 1
						n += 1
						clear()
						
			active=True  
			p_qn = open("pqn.txt")
			p_a = open("pa.txt")
			p_b = open("pb.txt")
			p_c = open("pc.txt")
			p_d = open("pd.txt")
			p_ans = open("pans.txt")
			p_que = p_qn.readlines()
			p_aa = p_a.readlines()
			p_bb = p_b.readlines()
			p_cc = p_c.readlines()
			p_dd = p_d.readlines()
			p_anss = p_ans.readlines()
			global plist
			#flist=[]
			plist=[] #LIMITING RANDOm
			while active: 
				if right+wrong+skip == 34:
					active=False
				p_qn = open("pqn.txt","r")
				leng = len(p_qn.readlines()) - 1
				r = random.randint(1,leng)
				if r not in plist:
					plist.append(r)
					print(f"{n}. {p_que[r].capitalize().strip()} ")
					print(p_aa[r].strip())
					print(p_bb[r].strip())
					print(p_cc[r].strip())
					print(p_dd[r].strip())
					p_anr = input("\nanswer ? ").lower()
					if p_anr ==p_anss[r].strip():
						right += 1
						n += 1
						clear() 	
					elif p_anr == "e":
						n += 1
						remarks()
						clear()
					elif p_anr=="s" or p_anr =="":
						skip += 1
						clear()
					else:
						w.append(p_que[r].strip())
						w.append(p_aa[r].strip())
						w.append(p_bb[r].strip())
						w.append(p_cc[r].strip())
						w.append(p_dd[r].strip())
						if p_anss[r].strip() == "a":
							w.append("Ans : {}\n".format(p_aa[r].strip()))
						elif p_anss[r].strip() == "b":
							w.append("Ans : {}\n".format(p_bb[r].strip()))
						elif p_anss[r].strip() == "c":
							w.append("Ans : {}\n".format(p_cc[r].strip()))
						elif p_anss[r].strip() == "d":
							w.append("Ans : {}\n".format(p_dd[r].strip()))
						wrong += 1
						n += 1
						clear() 
	
			active=True  
			c_qn = open("cqn.txt")
			c_a = open("ca.txt")
			c_b = open("cb.txt")
			c_c = open("cc.txt")
			c_d = open("cd.txt")
			c_ans = open("cans.txt")
			c_que = c_qn.readlines()
			c_aa = c_a.readlines()
			c_bb = c_b.readlines()
			c_cc = c_c.readlines()
			c_dd = c_d.readlines()
			c_anss = c_ans.readlines()
			global clist
			clist=[] 
			while active:
				if right+wrong+skip == 49:
					active=False
				c_qn = open("cqn.txt","r")
				leng = len(c_qn.readlines()) - 1
				r = random.randint(1,leng)
				if r not in clist:
					clist.append(r)
					print(f"{n}. {c_que[r].capitalize().strip()}")
					print(c_aa[r].strip())
					print(c_bb[r].strip())
					print(c_cc[r].strip())
					print(c_dd[r].strip())
					c_anr = input("\nanswer ? ").lower()
					if c_anr ==c_anss[r].strip():
						right += 1
						n += 1
						clear()
					elif c_anr == "e":
						clear()
						remarks()
					elif c_anr=="s" or c_anr=="":
						skip += 1
						n += 1
						clear()
					else:
						w.append(c_que[r].strip())
						w.append(c_aa[r].strip())
						w.append(c_bb[r].strip())
						w.append(c_cc[r].strip())
						w.append(c_dd[r].strip())
						if c_anss[r].strip() == "a":
							w.append("Ans : {}\n".format(c_aa[r].strip()))
						elif c_anss[r].strip() == "b":
							w.append("Ans : {}\n".format(c_bb[r].strip()))
						elif c_anss[r].strip() == "c":
							w.append("Ans : {}\n".format(c_cc[r].strip()))
						elif c_anss[r].strip() == "d":
							w.append("Ans : {}\n".format(c_dd[r].strip()))
						wrong += 1
						n += 1
						clear()
			remarks()
			
def com_e():
	active=True
	global que,aa,bb,cc,dd,anss,q_sub
	clear()
	print(msg)
	que = input("Question : ")
	aa = input("opt a - ")
	bb = input("opt b - ")
	cc = input("opt c - ")
	dd = input("opt d - ")
	while True:
		anss = input("Ans - ").lower()
		if anss == "a" or anss == "b" or anss == "c" or anss == "d":
			break
		elif anss == "q":
			exit()
		else:
			print("\nput option !")
			continue
			
	if q_sub == "cc":
		 Phy.p_qe()
	elif q_sub == "bb":
		 Chem.c_qe()
	elif q_sub == "aa":
		 Bio.b_qe()
	else:
		while True:
			q_sub = input("\nSubject (p/c/b) ?")
			if q_sub.lower() == "p":
				Phy.p_qe()
				break
			elif q_sub.lower() == "c":
				Chem.c_qe()
				break
			elif q_sub.lower() == "b":
				Bio.b_qe()
				break
			elif q_sub == "":
				print("\nNo such subject")
				continue
	
	
#STARTING THE PROGRAM		
def start():
	global sj,c,msg,cnf,q_sub

	msg = "Write the question, options and the answer respectively !\n"
	print("OBJECTIVE QUESTIONS PRACTICE")
	c = input("\nPractice(a) or Entry(b) ? ")
	if c.lower() =="b":
		clear()
		print("""Choose subject :
a) Biology
b) Chemistry
c) Physics
d) Common Entry
	""")
		q_sub = input("> ").lower()
		if q_sub == "a":
			q_sub=q_sub.replace("a","aa")
		if q_sub == "b":
			q_sub=q_sub.replace("b","bb")
		if q_sub == "c":
			q_sub=q_sub.replace("c","cc")
		com_e()
		
	elif c =="a":
		clear()
		print("""Choose :
a) Biology
b) Chemistry
c) Physics
d) Common Test
	""")
		sj = input("> ").lower()
		if sj == "d" or sj == "":
			comm()
		elif sj == "a" or sj == "b" or sj == "c":
			service()
	else:
		comm()


def service():
	global name
	name = input("Your name ? ")
	clear()
	print(f'\nHello {name} ! You have 50 questions, each \ncarrying one mark. You have no time limits.\n\n(PS : You can press "e" anytime to exit :) )\n')
	
	fin = input("Are you ready (y/n) ? ")
	if fin.lower() =="y" or fin =="":
		command()
	elif fin.lower() == "n":
		print(f"Oe looser {name} padh gayera natra naam niskanna yesai !")
		exit()


def command():
	if sj =="a" and c=="a":
		clear()
		Bio.b_qp()
	elif sj =="b" and c == "a":
		clear()
		Chem.c_qp()
	elif sj =="c" and c == "a":
		clear()
		Phy.p_qp()
		
		
def comm():
		global name
		print(f"You have 50 Questions, 25 Bio, 15 Chem and 10 Phy\nNo time limit !")
		name = input("Your name ? ")
		Common.com()

start()