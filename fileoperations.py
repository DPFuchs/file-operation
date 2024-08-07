names = "c:/users/DPF Programming/desktop/names.txt"
output = "c:/users/DPF Programming/desktop/output.txt"

with open(names, 'r') as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print(f"Word Count: {wordCount}")

with open(output, 'w') as file:
    line1 = file.write('Careers IT \n')
    line2 = file.write("System Development \n")
    line3 = file.write("Assessor - Mr Masiya")
    file.close()
    print("Sucessfully written to file")