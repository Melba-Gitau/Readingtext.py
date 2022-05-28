def read_file_content(openfile): 
 # [assignment] Add your code here
 with open("./story.txt","r") as openfile:
        read_file_content= openfile.read()
        print(read_file_content)
        return read_file_content

def countwords():
    text =read_file_content("./story.txt")
     # [assignment] Add your code here
    split_text = text.split()
    #print(split_text)
    count={}
    for word in split_text:
        if word in count:
            count[word] +=1
        else:
            count[word] =1
    return count  
        


print(countwords())
