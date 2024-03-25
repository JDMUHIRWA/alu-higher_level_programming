#!/usr/bin/python3
"""function that multiplies 2 matrixes"""

def matrix_mul(m_a, m_b):
  """
  Multiplies two matrices (m_a and m_b) and returns the resulting product matrix.

  Raises:
      TypeError: If m_a or m_b is not a list, or not a list of lists, or contains non-numeric elements, 
                 or is not a rectangle (rows with different lengths).
      ValueError: If m_a and m_b cannot be multiplied (different inner dimensions).
  """
# Calculate the product matrix
  product_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
  for i in range(len(m_a)):
      for j in range(len(m_b[0])):
          for k in range(len(m_b)):
              product_matrix[i][j] += m_a[i][k] * m_b[k][j]
              
  # Check if m_a and m_b are lists
  if not isinstance(m_a, list) or not isinstance(m_b, list):
    raise TypeError("m_a must be a list and m_b must be a list")

  # Check if m_a and m_b are lists of lists
  if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
    raise TypeError("m_a and m_b must be lists of lists")

  # Check if m_a and m_b are empty
  if not m_a or not m_b:
    raise ValueError("m_a and m_b can't be empty")

  # Check if elements in m_a and m_b are integers or floats
  for row in m_a:
    if not all(isinstance(item, (int, float)) for item in row):
      raise TypeError("m_a should contain only integers or floats")
  for row in m_b:
    if not all(isinstance(item, (int, float)) for item in row):
      raise TypeError("m_b should contain only integers or floats")

  # Check if m_a and m_b are rectangles (all rows same size)
  num_cols_a = len(m_a[0]) if m_a else 0  # Handle empty m_a
  if not all(len(row) == num_cols_a for row in m_a):
    raise TypeError("each row of m_a must be of the same size")
  num_rows_b = len(m_b)  # No need to handle empty m_b as previous checks ensure at least one element
  if not all(len(row) == num_cols_a for row in m_b):
    raise TypeError("each row of m_b must be of the same size")

  # Check if matrices can be multiplied (inner dimensions compatible)
  num_cols_a = len(m_a[0])  # Assuming non-empty m_a after previous checks
  num_rows_b = len(m_b)
  if num_cols_a != num_rows_b:
    raise ValueError("m_a and m_b can't be multiplied (incompatible inner dimensions)")

  # Return the resulting product matrix
  return product_matrix

