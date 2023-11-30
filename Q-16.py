main_string=input("please enter your main_string:")
sub_string=input("please enter your sub_string:")

count=0
for i in range(len(main_string)):
    if(main_string[i]==sub_string):
        count=count+1

print("the total nuber of",sub_string,"is=",count)