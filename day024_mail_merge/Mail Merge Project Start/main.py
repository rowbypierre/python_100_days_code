import os

# Save the letters in the folder "ReadyToSend".
# os.makedirs("ReadyToSend")

#TODO: Create a letter using starting_letter.txt 
sample_file = "./Input/Letters/starting_letter.txt"
with open(sample_file, "r") as letter:
    sample_text = "".join(line for line in letter.readlines())

#For each name in invited_names.txt
names_file = "./Input/Names/invited_names.txt"
with open(names_file, "r") as name_list:
    names = [name.strip().title() for name in name_list.readlines()]

#Replace the [name] placeholder with the actual name.
for name in names:
    letter_text  = sample_text.replace("[name]", name)

    with open("./ReadyToSend/" + name + ".txt", "w+") as letter:
        letter.write(letter_text)

