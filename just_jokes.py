# Wrote this to inspire my daughter thinking that she would consider
# learning some python.
# Who knows, I will check back in 10 years ;-)
import pyjokes
import art 

art.tprint("LOL", "random")

repeat = "" 
while True:
    playing = input(f"Do you want to hear a{repeat} joke (y/n)? ")
    print()
    if playing.lower() != "y":
        print("Good Bye!")
        print()
        art.aprint("happy")
        print()
        break
    else:
        joke = pyjokes.get_joke()       
        print(art.decor("random"), joke) 
        print()      
        repeat = "nother"

