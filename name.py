# for row in range(5):
#     for col in range(4):
# #        if (col==0 or col==4) or ((row==0 or row==2 or row==4) and (row >=0 and row<=6))or (col==2 and (row > 1 and row<4))or(col==4 and (row> 3 and row<6)):
            
#         if (row==0 or row==2 or row==4) or ( col==0 and(row==1 and row <2)) or   (col==4 and (row==3 and row<5)):

#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()    

for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or ((row==0 or row==3 ) and (col>0 and col<4)):


            print(" *",end=" ")
        else:
            print(end=" ")
    print()