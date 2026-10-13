text = input("Enter any sentence to check the vowels:")

vowel = "aeiou"
count= 0
for ch in text.lower():     #Here ".lower" is working to convert all the uppercase letters into lowercase.
    if ch in vowel:
        count+=1
print("Total count of vowel in this sentence is:", count)

        #OR

vowel = ['a','e','i','o','u']
count = 0
for ch in text.lower():     #Here ".lower" is working to convert all the uppercase letters into lowercase.
    if ch in vowel:
        count=count+1
print("Total number of vowel outcome:",count)

        #OR

vowel = {'a','e','i','o','u'}
count = 0
for ch in text.lower():
    if ch in vowel:
        count+=1
        print(ch)
print("Total count of vowels in this sentence is:",count)

        #OR

count = 0
for ch in text.lower():
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count+1
print("Total count of vowel in this sentence is:",count)

        #OR

count = 0
count = sum(1 for ch in text.lower() if ch in 'aeiou')      #1 is coming when the condition is passing
print("Total vowels in the given sentence are:",count)

        #OR

count = 0
list = [ch for ch in text.lower() if ch in 'aeiou']     #ch is storing the vowels outcome
print("Vowels outcome:",list)
print("vowels count",len(list))

        #OR

count = 0

for ch in 'aeiou':
    count += (text.lower()).count(ch)
print("Total vowels:",count)