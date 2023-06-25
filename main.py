import os
from office_versions import versions



directory = r"C:\Program Files\Microsoft Office\Office16"


def main():
    while True:
        usr_input = input("Enter the number of your office:\n"
                        "Enter 1 if the Office 2016\n"
                        "Enter 2 if the Office 2019\n")
        if usr_input == "1":
            if os.path.exists(directory):
                print("Directory exists.")
                os.system(f"{versions['Office 2016']['dir1']} && {versions['Office 2016']['cmd1']} $$ {versions['Office 2016']['cmd2']} && {versions['Office 2016']['cmd3']} && {versions['Office 2016']['cmd4']} && {versions['Office 2016']['cmd5']} && {versions['Office 2016']['cmd6']} && {versions['Office 2016']['cmd7']} && {versions['Office 2016']['cmd8']}")
            else:
                print("Directory does not exist.")
                os.system(f"{versions['Office 2016']['dir2']} && {versions['Office 2016']['cmd1']} $$ {versions['Office 2016']['cmd2']} && {versions['Office 2016']['cmd3']} && {versions['Office 2016']['cmd4']} && {versions['Office 2016']['cmd5']} && {versions['Office 2016']['cmd6']} && {versions['Office 2016']['cmd7']} && {versions['Office 2016']['cmd8']}")
            break
        elif usr_input == "2":
            if os.path.exists(directory):
                print("Directory exists.")
                os.system(f"{versions['Office 2019']['dir1']} && {versions['Office 2019']['cmd1']} $$ {versions['Office 2019']['cmd2']} && {versions['Office 2019']['cmd3']} && {versions['Office 2019']['cmd4']} && {versions['Office 2019']['cmd5']} && {versions['Office 2019']['cmd6']}")
            else:
                print("Directory does not exist.")
                os.system(f"{versions['Office 2019']['dir2']} && {versions['Office 2019']['cmd1']} $$ {versions['Office 2019']['cmd2']} && {versions['Office 2019']['cmd3']} && {versions['Office 2019']['cmd4']} && {versions['Office 2019']['cmd5']} && {versions['Office 2019']['cmd6']}")
            break
        else:
            print("There is no such option..\n")


if __name__ == "__main__":
    print("\t\t\t     ✧༝┉┉┉┉┉˚*❋ ❋ ❋*˚┉┉┉┉┉༝✧")
    print("\t\t\tWelcome to the office activator!")
    print("\t\t   Please feel free to contact me at github")
    print("\t\t\thttps://github.com/HolubievIllya")

    print("\t\t\t\t  ∘₊✧──────✧₊∘")
    main()

