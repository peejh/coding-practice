# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/5806045674995712

def spiral_order(matrix):
  num_rows, num_cols = len(matrix), len(matrix[0])
  total_len = num_rows * num_cols
  visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
  result = []
  direction = 1
  row, col = 0, 0
  row_start, row_end = -1, num_rows
  col_start, col_end = -1, num_cols

  while len(result) < total_len:
    
    # horizontal
    for c in range(col, col_end, direction):
      if visited[row][c]:
        break
      visited[row][c] = True
      result.append(matrix[row][c])
      col = c

    row = row + direction

    if len(result) >= total_len:
      break

    # vertical
    for r in range(row, row_end, direction):
      if visited[r][col]:
        break
      visited[r][col] = True
      result.append(matrix[r][col])
      row = r
    
    col = col - direction

    row_start, row_end = row_end, row_start
    col_start, col_end = col_end, col_start
    direction *= -1
  
  return result