def solution(args):
	formatted_list = ""
	first_number = args[0]
	for x in range(1,len(args)):
		if (args[x] - args[x - 1]) != 1:
			if args[x - 1] == first_number:
				formatted_list = (f"{formatted_list}{first_number},")
				first_number = args[x]
			elif abs(args[x - 1] - first_number) == 1:
				formatted_list = (f"{formatted_list}{first_number},{args[x - 1]},")
				first_number = args[x]
			else:
				last_number = args[x - 1]
				list_addition = f"{first_number}-{last_number}"
				formatted_list = (f"{formatted_list}{list_addition},")
				first_number = args[x]

			if x == len(args) - 1:
				formatted_list = (f"{formatted_list}{first_number},")

		elif x == (len(args) - 1):
			if args[x] == first_number:
				formatted_list = (f"{formatted_list}{first_number},")
			elif abs(args[x] - first_number) == 1:
				formatted_list = (f"{formatted_list}{first_number},{args[x]},")
			else:
				last_number = args[x]
				list_addition = f"{first_number}-{last_number}"
				formatted_list = (f"{formatted_list}{list_addition},")
	return formatted_list[:-1]

#print(solution([-60,-58,-56,-53,-51,-50]))
#print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
