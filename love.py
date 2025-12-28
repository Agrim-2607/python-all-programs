# for i in range(1000):
#     print("I love you❣️")


#----FIXED SIZE CODES----

'''
# Heart pattern using loops:- 
a=int(input("Enter the number of rows "))
for i in range(a):          # Outer loop (rows)
    for j in range(a+1):      # Inner loop (columns)
        # Condition to print '*'
        if (i == 0 and j % 3 != 0) or \
           (i == 1 and j % 3 == 0) or \
           (i - j == 2) or \
           (i + j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''


# for i in range(6):
#     for j in range(7):
#         # if (i==1 and j==) or (i==1 and j==3) or (i==1 and j==5) or (i==1 and j==6):
#         if (i == 0 and (j == 1 or j == 2 or j == 4 or j == 5)) or \
#            (i == 1 and (j == 0 or j == 3 or j == 6)) or \
#            (i == 2 and (j == 0 or j == 6)) or \
#            (i == 3 and (j == 1 or j == 5)) or \
#            (i == 4 and (j == 2 or j == 4)) or \
#            (i == 5 and j == 3):
#             print("❤️", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#----USER DEFINED SIZE CODE----

# rows = int(input("Enter heart height (recommended 6–15): "))

# # width should be about 1.5× height
# cols = rows + rows // 2

# for i in range(rows):
#     for j in range(cols):
#         # Equation-based heart shape
#         if (i == 0 and j % 3 != 0) or \
#            (i == 1 and j % 3 == 0) or \
#            (i - j == rows // 2 - 1) or \
#            (i + j == cols - rows // 2 + 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()       
 
for i in range(6):
    for j in range(7):
        if (i == 0 and (j == 1 or j == 2 or j == 4 or j == 5)) or \
           (i == 1 and (j == 0 or j == 3 or j == 6)) or \
           (i == 2 and (j == 0 or j == 6)) or \
           (i == 3 and (j == 1 or j == 5)) or \
           (i == 4 and (j == 2 or j == 4)) or \
           (i == 5 and j == 3):
            print("❤️", end=" ")
        else:
            print(" ", end=" ")
    print()