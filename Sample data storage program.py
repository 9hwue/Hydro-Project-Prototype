liist=list()
while True:
    print("\nOperate functions to store data in a digital storage for hydro program purpose.\nInput in a specific pattern with a number on the front for success usage:\n1 \"data(str) storage\"\n2 \"data(str) tend to be wiped\"\n3 (data listing)\n4 (data clearance)\n5 (exit)")
    inputa=str(input()).lstrip(" ")
    if   inputa[0:2]=="1 ":
        inputa=inputa[2:]
        liist.append(inputa)
    elif inputa[0:2]=="2 ":
        inputa=inputa[2:]
        if inputa in liist:
            liist.remove(inputa)
            print("Data removed successfully.")
        else:
            print("Data not stored.")
    elif inputa[0]=="3":
        count=1
        for data in liist:
            print(f"{count} {data}")
            count+=1
    elif inputa[0]=="4":
        print("Are you sure to wipe the entire data sequence? Type a \'y\' to confirm.")
        answer=input().rstrip(" ")
        if answer=="y" or answer=="Y":
            liist.clear()
            print("Data wiped successfully.")
        else:
            print("Data wiped unsuccessfully.")
    elif inputa[0]=="5":
        break;
    else:
        print("Unsupported pattern. Invalid command.")
exit(0);

