
msg = "hello"
msg2 = "Give me a sentence and I'll make an anagram out of it"
i = 0 #keeps track of current iteration
count = 0 #count of letter
#countletter = 0

for letter0 in msg:
    for letter1 in msg:
        if(letter1 == letter0): 
            count += 1
        #countletter += 1
    msg2  = msg[0:i]
    if (count == 1):
        print ("there is " + str(count) + " " + letter0 + " in " + msg )
    elif (letter0 not in msg2):
        print ("there are " + str(count) + " " + letter0 + "'s in " + msg )
    
    count = 0
    i += 1


listofchar = list(msg)              # makes a ist of msg
print(listofchar)                   # prints list
