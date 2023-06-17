import random
import math
import time

num_of_ques = int(input("Number of questions to ask ? "))
t1 = time.time()
score = 0
highest_num = math.ceil(math.sqrt(num_of_ques)) # highest number to be multiplied, such that we have enough questions
nums = list(range(1, max(10, highest_num+1)))

questions = []
for i in range(num_of_ques):
	questions.append((random.choice(nums), random.choice(nums)))

print(int((time.time()-t1)*1000), "ms")

for idx, (a, b) in enumerate(questions):
    result = a * b
    
    ans = input(f"{idx+1}) {a} x {b} = ")
    
    if ans == str(result):
        score += 1
    else:
        print("Wrong! The correct answer is", result)

print(f"Your score is {score} out of {num_of_ques}, which is {int(score/num_of_ques*100)}%")