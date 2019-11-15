file = open("1.txt","r")
file_read = file.read()
file_array = file_read.split()
best_percent = 100
best_percent_number = 0


i = 0
for item in file_array:
    item_array = item.split(",")

    percent = int(item_array[2])

    if(percent<= best_percent):
        best_percent = percent
        print(str(percent)+"w1"+str(item_array[0])+"b1"+str(item_array[1]))
    
    
    i += 1


