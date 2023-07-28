import random
num_of_ques = 10
num_of_ques = int(input("Number of questions to ask ? "))
score = 0
print("\nAnswer the following:\n")
for qloop in range (0,num_of_ques):
	firstnum = random.randint(1,10)
	secondnum = random.randint(1,10)
	ans = input(str(qloop+1) + ") " + str(firstnum) + " x " + str(secondnum) + " = ")	
	if ans == str(firstnum * secondnum):
		score=score +1
print("\nScore = " + str(score) + "/" + str(num_of_ques))
input()
