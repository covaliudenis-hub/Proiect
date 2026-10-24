print('Hello World')
print('Am o prietena draguta')
print('Vreau sa zbor cu avionul')
import subprocess
print("1. Test File Python") 
with open("mesaj.txt", "w", encoding="utf-8") as f: 
    f.write("Acesta este un mesaj test pentru a intelege functionalitatea")
print("2. Adaugarea fisierului")
subprocess.run(["git", "add", "."])
print("3. Salvez modificarea")
subprocess.run(["git", "commit", "-m", "Fisier adaugat prin Python"])
print("4. Trimit in Github")
subprocess.run(["git", "push"])
print("Succes! Totul a fost urcat pe GitHub!")