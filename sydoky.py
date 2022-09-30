import random

#this program generates a sudoku value field

def tests():

#some tests

  print('if all values in the lists are 45, then the tests were successful')

  line_sum = []
  line_ = []
  for i in range(9):
    line_ = []
    for j in range(9):
      line_.append(int(table[i][j]['apr']))
    line_sum.append(sum(line_))  
  print(line_sum)

  col_sum = []
  col_ = []
  for i in range(9):
    col_ = []
    for j in range(9):
      col_.append(int(table[j][i]['apr']))
    col_sum.append(sum(col_))  
  print(col_sum)

  s_sum = []
  s_ = []
  list_square = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
  for x in list_square:
    s_ = []
    for i in range(9):    
      for j in range(9):
        if table[j][i]['sq'] == x:
          s_.append(int(table[j][i]['apr']))
    s_sum.append(sum(s_))  
  print(s_sum)


def create_table():

# the function generates a dictionary of values 
# for the Sudoku field, with keys for cells: 
# accepted value('apr'), square ('sq'), possible values('va')
# as we know, the numbers should not be repeated
# horizontally and vertically, but also in a square


  global table  
  table = {
      line : {
        col : {
          'sq' : squares_write(line, col), 'va' : '123456789', 'apr' : None
          } for col in range(9)
          } for line in range(9)
          }
  

def squares_write(line, col):
  sq = None
  if line < 3 and col < 3:
    sq = 'A'
    return sq 
  if line < 3 and 2 < col < 6:
    sq = 'B'
    return sq 
  if line < 3 and col > 5:
    sq = 'C'
    return sq 
  if 2 < line < 6 and col < 3:
    sq = 'D'
    return sq 
  if 2 < line < 6 and 2 < col < 6:
    sq = 'E'
    return sq 
  if 2 < line < 6 and col > 5:
    sq = 'F'
    return sq 
  if line > 5 and col < 3:
    sq = 'G'
    return sq 
  if line > 5 and 2 < col < 6:
    sq = 'H'
    return sq 
  if line > 5 and col > 5:
    sq = 'I'
    return sq 


def exclusion(line, col, num, square):

  # we exclude the current random value 
  # from the possible values, and also if 
  # there is one option left in the possible 
  # values, we assign it to the accepted value for the cell
  
  for x in range(9):
    if table[line][x]['apr'] == None:
      table[line][x]['va'] = table[line][x]['va'].replace(str(num), '')     

  for y in range(9):
    if table[y][col]['apr'] == None:
      table[y][col]['va'] = table[y][col]['va'].replace(str(num), '')      

  for i in range(9):
    for j in range(9):
      if table[i][j]['apr'] == None:
        if table[i][j]['sq'] == square:
          table[i][j]['va'] = table[i][j]['va'].replace(str(num), '')

  for i in range(9):
    for j in range(9):
      if len(str(table[i][j]['va'])) == 1:
        table[i][j]['apr'] = table[i][j]['va']
        table[i][j]['va'] = None
        exclusion(i, j, table[i][j]['apr'], table[i][j]['sq'])
  

def set_number_if_unique(line, col, square): 

  # we check the presence of unique values vertically and horizontally, 
  # for example, if there is one non-repeating number in the array of 
  # horizontal values, we assign it to the cell

  list_of_variable = []
  for x in range(9):
    if table[line][x]['apr'] == None:
      list_of_variable.append(table[line][x]['va'])     

  list_of_variable = [x for x in ''.join(list_of_variable)]
  unique_list = []

  for i in list_of_variable:
    if list_of_variable.count(i) == 1:
        unique_list.append(i)

  if unique_list:
    i = 0
    for _ in unique_list:      
      for x in range(9):
        if table[line][x]['apr'] == None:
          if unique_list[i] in [x for x in table[line][x]['va']]:
            table[line][x]['va'] = None
            table[line][x]['apr'] = unique_list[0]
            exclusion(line, x, unique_list[i], square)
      i += 1

  list_of_variable = []

  for y in range(9):
    if table[y][col]['apr'] == None:
      list_of_variable.append(table[y][col]['va'])     

  list_of_variable = [x for x in ''.join(list_of_variable)]
  unique_list = []

  for i in list_of_variable:
    if list_of_variable.count(i) == 1:
        unique_list.append(i)

  if unique_list:
    i = 0
    for _ in unique_list:
      for y in range(9):
        if table[y][col]['apr'] == None:
          if isinstance(unique_list[0], list(table[line][x]['va'])):
            table[y][col]['va'] = None
            table[y][col]['apr'] = unique_list[0]
            exclusion(y, col, unique_list[0], square)     
      i += 1  
  

def filling():

# we take random values for the cells and if they satisfy us, we assign

  create_table()
  for line in range(9):
    for col in range(9):
      if table[line][col]['apr'] == None:
        if table[line][col]['va'] == '':
          return False
        num = random.choice(str(table[line][col]['va']))
        table[line][col]['apr'] = num
        table[line][col]['va'] = None        
        exclusion(line, col, num, table[line][col]['sq'])
        set_number_if_unique(line, col, table[line][col]['sq'])


def run():

# we run the program until the filling function is fully completed, 
# usually no more than 4 passes are required

  filling()
  generation_attempts = 0
  while filling() == False:  
    filling()
    generation_attempts += 1
  tests()
  print(f'attempts = {generation_attempts}')
  for line in range(9):    
    print([table[line][col]['apr'] for col in range(9)])


run()



