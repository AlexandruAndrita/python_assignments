
"""
I have used the following method in order to format the output.
Thus with "ljust" the string will be aligned to the left, with "rjust" to the right and with "center" in the middle.
The string has the width mentioned (the width is the first parameter when calling the method).
Then follows the character that should appear when the string is not printed
(has already been printed or it follows to be printed).
"""

width = int(input("Enter width: "))
squat = float(input("Enter squat: "))
bench = float(input("Enter bench press: "))
deadlift = float(input("Enter deadlift: "))

total = squat + bench + deadlift

title = "#Powerlifting 2022W"
title_squat = "Maximum Squat:"
tile_bench = "Maximum Bench Press:"
tile_deadlift = "Maximum Deadlift:"

title_length = len(title)
squat_length = len(title_squat)
bench_length = len(tile_bench)
deadlift_length = len(tile_deadlift)

print("".center(width,"#"))
value = width-title_length-1
print(title.ljust(title_length+1,' ') + "#".rjust(value,' '))
print("".center(width,"#"))

print(title_squat.ljust(squat_length+1) + f"{squat:.1f}kg".rjust(width-squat_length-1))
print(tile_bench.ljust(bench_length+1) + f"{bench:.1f}kg".rjust(width-bench_length-1))
print(tile_deadlift.ljust(deadlift_length+1) + f"{deadlift:.1f}kg".rjust(width-deadlift_length-1))

print("".center(width,"-"))
print("Total:".rjust(len("Total")+1) + f"{total:.1f}kg".rjust(width-len("Total")-1))