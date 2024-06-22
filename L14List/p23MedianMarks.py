# You are given a list marks that has the marks scored by a class of students in a Mathematics test. Find the median marks and store it in a float variable named median. You can assume that marks is a list of float values.
# Procedure to find the median
# (1) Sort the marks in ascending order. Do not try to use built-in methods.
# (2) If the number of students is odd, then the median is the middle value in the sorted sequence. If the number of students is even, then the median is the arithmetic mean of the two middle values in the sorted sequence.
# Input                              Expected Output
# Test Case1
# 30,50,40,10,20                           30.0
# Test Case2
# 60,10,30,40,20,50                        35.0

def solution(marks):
    sorted_marks = [ ]  
    while marks != [ ]:
        min_mark = marks[0]
        for mark in marks:
            if mark < min_mark:
                min_mark = mark
        marks.remove(min_mark)
        sorted_marks.append(min_mark)

    n = len(sorted_marks)
    if n % 2 != 0:
        mid = n // 2
        median = sorted_marks[mid] 
    else:
        mid2 = n // 2
        mid1 = mid2 - 1
        median = (sorted_marks[mid1] + sorted_marks[mid2]) / 2
    return median

print(solution([30,50,40,10,20]))