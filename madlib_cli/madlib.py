import re
## Main method
def User_service():
    '''
    This method runs the whole script , it does not return anything but it
    adds the filled template into a new file which is "make_me_a_video_game_output.txt" in this case
    '''
    print('''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
        *  Hey There ! in this game you will have just to fill each field with the        *
        *  type of it ! Yes as simple as that ! the type of the field will be available   *
        *  to you and you will have to fill it . Enjoy !                                  *                                                                                      
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

          ''')
    reuseable_text = read_template("assets/make_me_a_video_game_template.txt")
    text , words = parse_template(reuseable_text)
    print(words)
    filled_tuple = list()
    for word in words:
        filled_tuple.append(input(f"\ninsert a {word}\n"))
    with open("make_me_a_video_game_output.txt",'w') as file:
        temp = merge(text,(tuple)(filled_tuple))
        file.write(temp) 
        print(temp)
        
## Reading the file content 
def read_template(path):
    '''Reads the template from the provided path.
    -Returns:
     The file content if the path is vaild
                    OR
     Raise an error if the path is not vaild                         
     '''
    try:
        with open (path ,"r")as file:
            return file.read()
    except:
        raise FileNotFoundError    


## saving the words inside '{}' and then replacing them with an empty '{}    
def parse_template(text):
    '''Takes a String (Could be a line or more)
    returns :
    - New text that has filtered to remove the any words between {} in it 
    - The words that we removed from the original text
    '''
    words  = re.findall('{(.*?)}', text)
    textnew = re.sub('{.+?}', '{}', text)  
    return textnew,(tuple)(words)  

## merging the empty template with the user words 
def merge (empty_text,words:tuple):
    '''Takes a template and merges it with the provided tuple of words
    returns:
    - The merged template with the words
    '''
    return empty_text.format(*words)
  
   
                 
                
        
    
       
if __name__ =="__main__":
      User_service()      
    





    