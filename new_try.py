##text lesen
file = open("1.txt","r")

file_content = file.read()
file_array = file_content.split()

file.close()

random_number = 0

while(random_number < 11):
    i = 0
    for item in file_array:
        
        
        string = item
        item_array = string.split(",")
        i2 = 0
        for value in item_array:
            
            value = int(value)
            item_array[i2] = value
            i2 +=1

        ##array with integers in form w1 , b1 , percent away

        ergebnis = (int(item_array[0])*int(random_number))+ int(item_array[1])
        close = abs(5-ergebnis)
        close_in_percent = close*10

        close_in_percent_new = (close_in_percent + item_array[2])/2
        close_in_percent_new = round(close_in_percent_new)
        item = str(item_array[0])+","+ str(item_array[1])+","+str(close_in_percent_new)
        
        file_array[i] = item                             
        
        i += 1
    print("einmal durch")
    random_number +=1




file = open("1.txt","w")
file.write("")
file.close()

file = open("1.txt","a")
number = 0
for value in file_array:
    file.write(file_array[number])
    file.write("\n")
    number +=1



file.close()
    






   

    
