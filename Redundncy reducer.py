def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      

    

if __name__=="__main__":
    duplicate = [1,3,4,1,3,4,1,3,4]
    duplicate.sort()
    print(Remove(duplicate)) 
