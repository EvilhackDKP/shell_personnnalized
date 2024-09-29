import os
print("Hello in my little script")
print("""Tips: Execute this script in sudo for have all permission. 
If you not execute in sudo, go to the random folder is impossible
             """)

text = input("How is the text for shell (add a espace a end of this text): ")

print("okay, enter start for start the shell")

launch = input("You want start this script?: ")

def shell():
    while launch =="start":
        shell_modified = input(text)
        os.system(shell_modified)

if launch == "start":
    shell()
else:
    print("[Script]: This syntaxe is not demanded. END")
