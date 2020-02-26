

@count_elapsed_time
def sum(nums):
    answer = 0
    for num in nums:
        answer += int(num)
    return answer

@count_elapsed_time
def repeatedNumbers(repeatedNumbers, listOfNumbers):
    output = ''
    for repeated in repeatedNumbers:
        count = 0
        for numberList in listOfNumbers:
            if repeated == int(numberList):
                count += 1
        output += 'The number {} is repeated {} times.\n'.format(repeated, count)
    return output
