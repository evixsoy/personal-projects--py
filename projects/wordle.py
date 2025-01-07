# input err -> max. 5 mist, kazde pismeno jen jednou
# input -> zjisti jestli input obsahuje pismena v word -> zjisti jestli jsou na stejnym indexu(jestli ne tak hodi oranz emoji) ->

word = ["m", "a", "u", "v", "e"]
guesscount = 0
output = []
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
indexguess = 0
outputval = 0


while guesscount <6:
    guesscount += 1
    print(f"{guesscount}. Guess word")
    print(lowercase)

    guess = input(">").lower()
    if guesscount > 6:
            print("end")

    for i in guess:   
        indexguess +=1
        if i not in word:
            output.append("wrong")
            if i in lowercase:
                lowercase.remove(i)
        else:
            if indexguess != word.index(i) + 1:
                output.append("different place")
            else:
                output.append("correct")
                outputval +=1
    
    if outputval == 5:
        break
    
    print(output)
    output = []
    guess = ""

if outputval == 5:
    print("you won!!!!")
    kowdw = input()
else:
    print("you lose")