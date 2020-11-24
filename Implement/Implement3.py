#Implement3 왕실의 나이트
column,row = input()
row = int(row)
column = int(ord(column))-int(ord('a'))+1
answer = 0
knight = [(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)]
print(row,column)
for step in knight:
    row_step = step[0] + row
    column_step = step[1] + column
    print(row_step,column_step)
    if row_step >= 1 and row_step <= 8 and column_step >= 1 and column_step <= 8:
        answer += 1

print(answer)