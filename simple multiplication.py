import random
import itertools

num_of_ques = int(input("Number of questions to ask ? "))
score = 0
#generate a list of numbers from 1 to 10
nums = list(range(1,10))

#generate all possible combinations of numbers
bigset = list(itertools.product(nums,nums))


  
while num_of_ques > len(bigset):
	num_of_ques = int(input("Please reduce the number of questions: "))
 
#select random questions from all available options
ques = random.sample(bigset,num_of_ques)

print("\nAnswer the following:\n")

# loop through the questions
for idx, question in enumerate(ques):
    # calculate the result
	result = question[0] * question[1]

	q_str = str(idx+1) + ") " + str(question[0]) + " x " + str(question[1]) + " = "
	ans = input(q_str)
	# check if the answer is correct
	if ans == str(result):
		score += 1
	else:
		print("Wrong! The correct answer is", result)

percentage = int((score/num_of_ques) * 100)
print("\nScore =", score, "out of", num_of_ques, "which is", percentage, "%")
input()