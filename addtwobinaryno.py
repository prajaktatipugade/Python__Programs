#C++ program to add two
#binary strings

# This function adds two binary strings
# and return result as a third string
def addBinary( A,  B):
	# If the length of string A is greater
	# than the length of B then just swap
	# the string by calling the same#function and make sure to return
	# the function otherwise recursion
	#will occur which leads to calling
	# the same function twice
	if (len(A) > len(B)):
		return addBinary(B, A)

	#Calculating the difference between
	# the length of the two strings.
	diff = len(B) - len(A);

	#Initialise the padding string which
	# is used to store zeroes that should
	# be added as prefix to the string which
	# has length smaller than the other string.
	 
	for i in range(i,i< diff):
		padding.push_back('0')
       A = padding + A
       carry = '0'

	for (int i = len(A) - 1; i >= 0; i--)
	{
		# This if condition solves 110 111
		#possible cases
		if (A[i] == '1' and B[i] == '1'):
		
			if (carry == '1'):
				res.push_back('1'), carry = '1';
			else:
				res.push_back('0'), carry = '1';
		

		# This if condition solves 000 001
		# possible cases
		else if (A[i] == '0' and B[i] == '0'):
		
			if (carry == '1'):
				res.push_back('1'), carry = '0';
			else
				res.push_back('0'), carry = '0';
		

		#This if condition solves 100 101 010
		# 011 possible cases
		else if (A[i] != B[i]):
		
			if (carry == '1'):
				res.push_back('0'), carry = '1';
			else:
				res.push_back('1'), carry = '0';
		
	

	# If at the end their is carry then just
	#add it to the result
	if (carry == '1'):
		res.push_back(carry)
	# reverse the result
	reverse(res.begin(), res.end())

	#To remove leading zeroes
	index = 0;
	while (index + 1 < len(res) and
		res[index] == '0')
		index++
	return (res.substr(index))


	string a = "1101", b = "100";
	cout << addBinary(a, b) << endl;
