def main():
    string = ""
    for i in range (81):
        if i<10:
            string += "0" + str(i)+ " "
        else:
            string += str(i) +" "
        if i%9 == 8:
            string += "\n"
    print string
main()