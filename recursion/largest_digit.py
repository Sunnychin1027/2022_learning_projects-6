"""
File: largest_digit.py
Name: Sunny
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, it will be the input integers
	:return: int, this will return the largest digit in the input integers
	"""
	if n < 0:
		n = -n
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, largest_digit):
	if n == 0:
		return largest_digit
	else:
		last_digit = n % 10
		if last_digit > largest_digit:
			largest_digit = last_digit
		return find_largest_digit_helper(n//10, largest_digit)















if __name__ == '__main__':
	main()
