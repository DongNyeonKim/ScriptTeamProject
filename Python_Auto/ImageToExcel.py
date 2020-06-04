import openpyxl 
from openpyxl import load_workbook 
from openpyxl import Workbook 
from openpyxl.drawing.image import Image 

openpyxl_version = openpyxl.__version__ 
print(openpyxl_version) #to see what version I'm running 

# downloaded a .png to local directory manually from 
#change to the location and name of your image 

    # test.xlsx already exists in my current directory 

wb = load_workbook('test.xlsx')
ws = wb.active

t=1
i=1
while(t<46):
    t=t+1
    i +=1
    
    i = str(i)
    a= '쇼파'+ i+'.jpg'



    png_loc = r'쇼파'+i+'.jpg' 
    my_png = openpyxl.drawing.image.Image(png_loc) 


    ws.add_image(my_png, 'A'+i) 
    i = int(i)



wb.save('test.xlsx') 