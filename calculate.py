from random import randrange

i = 0

while(i < 1000):
    ##user input welche nummer
    input_user = 1
    ##ai soll erkennen das 5 ist am besten
    close_in_percent = 6
    s1 = int(input_user)


    #calculate

    w1 = randrange(11)
    b1 = randrange(11)

    ergebnis = (w1 * s1)+b1
    close = abs(5-ergebnis)
    close_in_percent = close*10










    ## write it down
    text_document = open("1.txt","a")
    ##w1,b1,wie nah dran prozentual
    text_document.write(str(w1)+ ","+str(b1)+ ","+ str(close_in_percent)+"\n")



    text_document.close()
    i -= -1

