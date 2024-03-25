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


  if not isinstance(m_a, list):
    raise TypeError("m_a must be a list")
  if not isinstance(m_b, list):
    raise TypeError("m_b must be a list")

  if not all(isinstance(row, list) for row in m_a):
    raise TypeError("m_a must be a list of lists")
  if not all(isinstance(row, list) for row in m_b):
    raise TypeError("m_b must be a list of lists")


  if not m_a or not m_b:
    raise ValueError("m_a and m_b can't be empty")

  for row in m_a:
    if not all(isinstance(item, (int, float)) for item in row):
      raise TypeError("m_a should contain only integers or floats")
  for row in m_b:
    if not all(isinstance(item, (int, float)) for item in row):
      raise TypeError("m_b should contain only integers or floats")

  num_cols_a = len(m_a[0]) if m_a else 0 
  if not all(len(row) == num_cols_a for row in m_a):
    raise TypeError("each row of m_a must be of the same size")
  num_cols_b = len(m_b[0]) if m_b else 0  
  if not all(len(row) == num_cols_b for row in m_b):
    raise TypeError("each row of m_b must be of the same size")

  
  num_cols_a = len(m_a[0])  
  num_rows_b = len(m_b)
  if num_cols_a != num_rows_b:
    raise ValueError("m_a and m_b can't be multiplied")
  
  product_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
  for i in range(len(m_a)):
      for j in range(len(m_b[0])):
          for k in range(len(m_b)):
              product_matrix[i][j] += m_a[i][k] * m_b[k][j]

  return product_matrix

# Test cases (same as 100-matrix_mul but with NumPy exceptions)
def test_lazy_matrix_mul():
#Valid Multiplication (2x3 * 3x2)
m_a = [[1, 2, 3], [4, 5, 6]]
m_b = [[1, 4], [2, 5], [3, 6]]
expected_product = [[14, 20], [32, 47]]

product_matrix = matrix_mul(m_a, m_b)
assert product_matrix == expected_product

print("Test Case 1 Passed!")

#Test Case 2: Empty Matrices
m_a = []
m_b = [[1, 2, 3]]

try:
  matrix_mul(m_a, m_b)
except ValueError as e:
  assert str(e) == "m_a and m_b can't be empty"
else:
  raise AssertionError("ValueError not raised for empty m_a")

m_a = [[1, 2, 3]]
m_b = []

try:
  matrix_mul(m_a, m_b)
except ValueError as e:
  assert str(e) == "m_a and m_b can't be empty"
else:
  raise AssertionError("ValueError not raised for empty m_b")

print("Test Case 2 Passed!")

#Test Case 3: Incompatible Inner Dimensions
m_a = [[1, 2, 3]]
m_b = [[1], [2]]

try:
  matrix_mul(m_a, m_b)
except ValueError as e:
  assert str(e) == "m_a and m_b can't be multiplied"
else:
  raise AssertionError("ValueError not raised for incompatible dimensions")

print("Test Case 3 Passed!")

#Test Case 4: Non-numeric Elements
m_a = [[1, 2, 3], [4, 5, "text"]]
m_b = [[1, 2], [3, 4]]

try:
  matrix_mul(m_a, m_b)
except TypeError as e:
  assert "m_a should contain only integers or floats" in str(e)
else:
  raise AssertionError("TypeError not raised for non-numeric elements in m_a")

m_a = [[1, 2, 3], [4, 5, 6]]
m_b = [[1, 2.5], [3, "text"]]

try:
  matrix_mul(m_a, m_b)
except TypeError as e:
  assert "m_b should contain only integers or floats" in str(e)
else:
  raise AssertionError("TypeError not raised for non-numeric elements in m_b")

print("Test Case 4 Passed!")

#Test Case 5: Single-element Matrices
m_a = [[1]]
m_b = [[1], [2]]
expected_product = [[1, 2]]

product_matrix = matrix_mul(m_a, m_b)
assert product_matrix == expected_product

print("Test Case 5 Passed!")
