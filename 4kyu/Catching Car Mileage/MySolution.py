def is_interesting(number, awesome_phrases):

    def all_zeroes(num):
        num_len = len(str(num))
        rounded = (num // (10 ** (num_len-1))) * (10 ** (num_len-1))
        return num - rounded == 0.0

    def all_the_same(num):
        num_len = len(str(num))
        rounded = (num // (10 ** (num_len-1)))
        test_number = 0
        for x in range(1,num_len+1):
            test_number = test_number + (10 ** (x-1))
        return num/test_number == rounded

    def increment(num):
        num_list = [int(x) for x in str(num)]
        for x in range(1,len(num_list)):
            if (num_list[x] - num_list[x-1] != 1) and (num_list[x] - num_list[x-1] != -9):
                return False
        return True

    def decrement(num):
        num_list = [int(x) for x in str(num)]
        for x in range(1,len(num_list)):
            if (num_list[x] - num_list[x-1] != -1):
                return False
        return True

    def palindrome(num):
        num_list_forward = [int(x) for x in str(num)]
        num_list_backwards = num_list_forward[::-1]
        for x in range(len(num_list_forward)):
            if num_list_forward[x] != num_list_backwards[x]:
                return False
        return True

    def awesome_check(num, awesome_list):
        for x in awesome_list:
            if num == x:
                return True
        return False

    def interesting_check(num, awesome_list):
        return (all_zeroes(num) or
                all_the_same(num) or
                increment(num) or
                decrement(num) or
                palindrome(num) or
                awesome_check(num, awesome_list)
                )

    def length_check(num, awesome_list):
        return len([int(x) for x in str(num)]) > 2 and interesting_check(num, awesome_list)

    if length_check(number, awesome_phrases):
            return 2
    elif length_check(number+1, awesome_phrases): 
            return 1
    elif length_check(number+2, awesome_phrases):
            return 1
    else:
        return 0

