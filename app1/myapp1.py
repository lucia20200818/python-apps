from difflib import get_close_matches
import json
 
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(word , data.keys())) >0:
       
        yn = input("Do you mean %s instead? Enter Y if yes , enter N if no." % get_close_matches(word , data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn =="N":

            return"This word doesn't exist"
        else:
            return "we don't get it"

    else:
        return "Please double check your input"


word = input("Enter the word:" )

output = translate(word)
if type(output) == list:


    for item in output:
       print(item)

else:
    print(output)