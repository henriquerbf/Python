list = [32,2,6,456,7114,121,45,1,9079,23]
# list = [1,2,3,4,5,6,7,8,9,10]

def bubbleSort(list):
    valueChanged = True
    for j in range(len(list)-1):
       
        # in case of list is already ordened it will stop it
        if not valueChanged:
            return
        
        valueChanged = False

        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                valueChanged = True
                temp = list[i]
                list[i]=list[i+1]
                list[i+1]=temp

bubbleSort(list)
print(list)