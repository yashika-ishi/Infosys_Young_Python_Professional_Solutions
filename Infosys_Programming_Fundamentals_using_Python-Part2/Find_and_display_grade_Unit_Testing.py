# A teacher in a school wants to find and display the grade of a student based on his/her percentage score. The criterion for grades is as given below:
# Assume that the percentage score is a whole number.
# Write a python program for the above requirement. Identify the test data and use it to test the program.

score=67
if(score>=80 and score<=100):
    print("Grade:A")
elif(score>=73 and score<=79):
    print("Grade:B")
elif(score>=65 and score<=72):
    print("Grade:C")
elif(score>=64 and score<=0):
    print("Grade:D")
else:
    print("Grade:Z")