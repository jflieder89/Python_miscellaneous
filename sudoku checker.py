sudoku = []
sudoku.append(195743862)
sudoku.append(431865927)
sudoku.append(876192543)
sudoku.append(387459216)
sudoku.append(612387495)
sudoku.append(549216738)
sudoku.append(763524189)
sudoku.append(928671354)
sudoku.append(254938671)

def sudoku_checker():
    
    #first, check the rows
    valid_rows = True #keep flag for rows as valid by default, to be set to False if an error if found
    for row in sudoku:
        row = str(row) #so string methods can be used
        for digit in range (1, 10): #to iterate through 1 through 9 for each row
            if (str(digit) in row) and row.count(str(digit)) == 1:
                pass
            else: 
                valid_rows = False
    # print(valid_rows)
    
    #next create columns and check them
    valid_columns = True #keep flag for columns as valid by default, to be set to False if an error if found
    col_matrix = ['', '', '', '', '', '', '', '', ''] #empty list of column strings
    for row in sudoku:
        row = str(row) #so string methods can be used, and len(row) can be used
        for digit in range(len(row)): #iterate 0 through 8
            # print(digit)
            col_matrix[int(digit)] = col_matrix[int(digit)] + row[digit] #the nth column gets every row's nth digit added to it
    # print(type(col_matrix[0]))
    # print(col_matrix[1])
    # print(col_matrix[2])
    # print(col_matrix[8])
    for column in col_matrix: #the columns are already strings in this case
        for digit in range (1, 10): #to iterate through 1 through 9 for each column
            if (str(digit) in column) and column.count(str(digit)) == 1:
                pass
            else: 
                valid_columns = False
    
    #next create strings of box digits and check them
    valid_boxes = True
    box_matrix = ['', '', '', '', '', '', '', '', ''] #empty list of box strings
    row_number = 0 #create a counter for the row number that is being iterated through
    for row in sudoku:
        row = str(row) #so string methods can be used, and len(row) can be used
        for digit in range(len(row)): #iterate 0 through 8
            #print(row_number, digit)
            if (row_number <= 2) and (digit <= 2):
                box_matrix[0] = box_matrix[0] + row[digit]  
            elif (row_number <= 2) and (digit <= 5):
                box_matrix[1] = box_matrix[1] + row[digit]
            elif (row_number <= 2) and (digit <= 8):
                box_matrix[2] = box_matrix[2] + row[digit] 
                
            elif (row_number <= 5) and (digit <= 2):
                box_matrix[3] = box_matrix[3] + row[digit]
            elif (row_number <= 5) and (digit <= 5):
                box_matrix[4] = box_matrix[4] + row[digit]
            elif (row_number <= 5) and (digit <= 8):
                box_matrix[5] = box_matrix[5] + row[digit]
                
            elif (row_number <= 8) and (digit <= 2):
                box_matrix[6] = box_matrix[6] + row[digit]
            elif (row_number <= 8) and (digit <= 5):
                box_matrix[7] = box_matrix[7] + row[digit]
            elif (row_number <= 8) and (digit <= 8):
                box_matrix[8] = box_matrix[8] + row[digit]
        
        row_number += 1
    
    for box in box_matrix: #the columns are already strings in this case
        for digit in range (1, 10): #to iterate through digits 1 through 9 for each box
            if (str(digit) in box) and box.count(str(digit)) == 1:
                pass
            else: 
                valid_boxes = False
        
    # print(box_matrix)
    # print('Are the rows valid: ', valid_rows)
    # print('Are the columns valid: ', valid_columns)
    # print('Are the boxes valid: ', valid_boxes)
    
    if valid_rows == True and valid_columns == True and valid_boxes == True:
        return 'Yes'
    else: 
        return 'No'

print(sudoku_checker())
