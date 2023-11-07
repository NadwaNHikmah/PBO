# open a file 
file1 = open("text.txt", "r")
teks= "Selamat datang di Universitas muhammadiyah Cirebon\n"

file2 = open("text.txt", "a")
file2.write(teks)
file2.close()

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()

