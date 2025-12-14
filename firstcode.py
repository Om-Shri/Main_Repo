import win32com.client, shutil, os


speaker = win32com.client.Dispatch("SAPI.SpVoice")  # Windows speech engine
voices = speaker.GetVoices()
speaker.Voice = voices.Item(0)
speaker.Rate = 0
speaker.Volume = 100


copy = "Sanjana.txt"

if os.path.exists(copy):
    print("folder alrady exist.")
else:
    shutil.copytree(r"C:\Users\Pramod sah\first_code.py",copy)

for i in range(10,-1,-1):
    print(i)
    speaker.speak(i)

shutil.rmtree(copy)
print(f"The folder name ''{copy}'' has deleted.")
