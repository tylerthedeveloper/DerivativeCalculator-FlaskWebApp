from itertools import *
from forms import EntryForm
import re

#div_calculator 2.0
# "X(5x^2)^2"

power = 0
power1 = 0
var = ''  
var1 = ''
#(5x^2)
inExp = ''


#expression = raw_input("Please enter your expression: ")
# signList = []			
# 5x^2 + (8u5r843ut984) + - 

#expression = ''

def derive(expression):

	t = True

	while t:
	
		expList = []

		expression = expression

		derivative = []
	
		signList = re.findall(r"[+\-]", expression)
#		print signList
	
		# for exp in range(len(expression)):
# 			if "cos" in expression:
# 				exp = expression[expression.find("cos(")+4:expression.find(")")]
	# 			expList.append(exp)
	#		while exp <= len(expression)-1:
			
			
		if '(' and ')'in expression:
			# exp = re.split("[+-]", expression)
# 				print exp, 'hi'
			# get stuff before and after parantheses
			# split nirmal way
			first = (expression.find("("))+1
			second = expression.find(")")
			if second == (len(expression)-1) and expression[(first-1)] == expression[0]:
				if (expression.find('+') > first and expression.find('+') < second) or (expression.find('-') > first and expression.find('-') < second): #or '-'
					exp = expression[first:second]
					print exp
					exp = re.split(r"[+-]", exp)
					print exp
					expList.append(exp)
				else:
					exp = expression[first:second]
					exp = re.split("()", exp)
# 						print 'exp:', exp
					expList.extend(exp)
			else:
				print 'ho'
				# for indice in expression[:first-1]:
				print expression
#				expFront = re.split("[+-]", expression[:first-2])
				expFront = expression[:first-2].split("[+-]")
				expMid = re.split("[+-]", expression[first:second])
				expBack = re.split(r"[+-]", expression[second+2:])
				expList.append(expFront+expMid+expBack)
		
			print expList
			
# 				for indice in expression[second:]:
# 					exp = re.split("[+-]", expression[second:])
# #						print exp
# 					expList.append(exp)
# 					break
# 				#alternative to for loop?
# 				for index in expression[first:second]:
# 					if (expression.find('+') > first and expression.find('+') < second) or (expression.find('-') > first and expression.find('-') < second): #or '-'
# 						exp = re.split(r"([+-])", exp)
# #							print exp
# 						expList.append(exp)
# 						break
# 					else:
# 						exp = expression[first:second]
# 						exp = re.split("()", exp)
# # 						print 'exp:', exp
# 						expList.append(exp)
# 						break


			
		else:	
			exp = re.split("[+-]", expression)
			print exp
			expList.append(exp)

#		print expList
# 			else:
# 		#	elif '(' and ')'in expression: #and (expression.find(")")+1) != '':
# 				print 'no stuff'
# 				first = expression.find("(")+1
# 				second = expression.find(")")
#  				if '+' or '-' in expression:				
# 					exp = expression[first:second]
# 					exp = re.split("[+-]", exp)
# 				else:
# 					exp = expression[first:second]
# 					exp = re.split("", exp)

# 	 			print exp
#	  			print expList
		
		for exp in expList[0][:]:
			exp = str(exp)
	#		print 'exp is' , exp
			num = exp.split('x') # only want [0] as below, not array...
			# ^need to make for all variables, not just x
			numtest = int(str(num[0][:]))
	#		print 'numtest is ' , numtest

			if '^' in exp:
				power = exp.rsplit('^',1) # only want [0] as below, not array...
				powtest = int(str(power[1][:]))
	#			print 'powtest is ', powtest
			else:
				powtest = 0
			
			var = re.search(r'[a-zA-Z]', exp)
			try:
				varPrint = str(var.group())
			except:
				varPrint = '' # none
		
			if powtest == 1:
				derivative.append(str(numtest) + varPrint)
			elif powtest == 0:
				if varPrint == '':
					derivative.append('')
				else:
					derivative.append(str(numtest))
			else:
				if powtest == 2:
					derivative.append(str((powtest * numtest)) + str(varPrint))
				else:
					derivative.append(str((powtest * numtest)) + str(varPrint) + '^' + str(powtest-1))
	# 			derivative += numtest
	# 			derivative += varPrint
		
		testList = []
	#	print signList
	#	print derivative
		if len(expList[0]) > 1:
			# zip -> not equal on last character ... will not print...
			testList = [item for pair in izip_longest(derivative, signList, fillvalue='') for item in pair]
	#		testList = [filter(None, pair) for pair in izip_longest(derivative,signList)]
			#range(len(signList)), range(len(derivative)):
			#testList += str(signList[i]), str(derivative[i])
	#http://stackoverflow.com/questions/11318977/zipping-unequal-lists-in-python-in-to-a-list-which-does-not-drop-any-element-fro
			x = ''.join(testList)		
			if x[-1] == '+' or x[-1] == '-':
				print x[:-1]
				#textList.insert(END, ("Derivative of " + expression + ' is ' + x[:-1] + '\n'))
				#E1.delete(0, END)
 				t = False
 				return x[:-1] #, False
			else:	
#				tkMessageBox.showinfo("Derivative", x)
				#textList.insert(END, ("Derivative of " + expression + ' is ' + x + '\n'))
				#E1.delete(0, END)
				t = False
				return x #, t
				#return False
			# for index in expList:
			#	expList[index] = derivative

		else:
			y = str(''.join(derivative))
			print y
			#tkMessageBox.showinfo("Derivative", y)
			#textList.insert(END, ("Derivative of " + expression + ' is ' + y + '\n'))
			#E1.delete(0, END)
# 			derivative = []
# 			expression = ''
#			derive()
			t = False
			return y #, t
		
		#	expression.replace(expression.find('+'), 'x')	
		#	print derivative


#		print expression
# 		if '+' or '-' in expression:
# 			print 'hi'
# take expList ... leave plus or minus signs 
# take exp, derive, return to list .replace ... 
# explist[exp].replace(derive(exp))
			
		
#(int(num[0])*int(powerPrint)) , varPrint ,  '^' , (powerPrint-1)	
#	print expList[0][1]
#	print derivative #, ' hi'
#	derivative+=exp

#derivative = 
# 		print num[0]
# 		print powerPrint
# 		print varPrint
		
		
#stepOne()
#calc()

# def main():
# #	derive()
# 	GUI()
# 	Deriver.mainloop()
# 	
# if __name__ == "__main__":
#     main()


# errors:
			
# 1. trig functions ...
# 3. 5x+3x ... should be 8x
# 	5x + 3x = 5 + 3 = 8
# if both numbers .. eval (exp , signList, exp)
# stuff in parantheses)
# if parantheses and nothing in front AND back, drop
# ^ if only front
# ^ if only back