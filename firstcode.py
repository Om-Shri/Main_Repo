import random
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
speaker.Voice = voices.Item(0)
speaker.Rate = 0
speaker.Volume = 100

a = random.randint(1, 100)

speaker.speak("Guess the number between 1 to 100")

for i in range(9, -1, -1):

    b = float(input("Guess the number(between 1 to 100) :--> "))
    
    if b == a:
        print("Waaw! You guessed it correct.", "Remaining chances --->", i)
        speaker.speak(f"Waaw You guessed it correct Remaining chances {i}")
        break
    elif b > a:
        print("Your guess is greater. Try again. Chances left:", i)
        speaker.speak(f"Your guess is greater Try again Chances left {i}")
    else:
        print("Your guess is smaller. Try again. Chances left:", i)
        speaker.speak(f"Your guess is smaller Try again Chances left {i}")
else:
    print("Sorry, you've used all chances. The correct number was:", a)
    speaker.speak(f"Sorry you've used all chances The correct number was {a}")

print("-------- Game Over --------")