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

def test_lazy_matrix_mul_without_numpy():

    # Test 1: Empty matrices
    m_a = []
    m_b = [[1, 2]]
    with pytest.raises(ValueError) as excinfo:
        lazy_matrix_mul(m_a, m_b)
    assert str(excinfo.value) == "m_a and m_b can't be empty"

    # Test 2: Incompatible inner dimensions
    m_a = [[1, 2], [3, 4]]
    m_b = [[1], [2, 3]]
    with pytest.raises(ValueError) as excinfo:
        lazy_matrix_mul(m_a, m_b)
    assert str(excinfo.value) == "m_a and m_b can't be multiplied (incompatible inner dimensions)"

    # Test 3: Non-numeric elements (using string)
    m_a = [[1, 2], ["text", 4]]
    m_b = [[1], [2]]
    with pytest.raises(TypeError) as excinfo:
        lazy_matrix_mul(m_a, m_b)
    assert "m_a and m_b elements must be numeric" in str(excinfo.value)  # Adjusted message for clarity

    # Test 4: Valid multiplication
    m_a = [[1, 2], [3, 4]]
    m_b = [[1, 2], [3, 4]]
    product_matrix = lazy_matrix_mul(m_a, m_b)
    assert product_matrix == [[7, 10], [15, 22]]  # Direct comparison without NumPy
