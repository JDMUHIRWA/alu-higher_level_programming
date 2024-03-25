#!/usr/bin/python3
"""multipying 2 matrixes"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
  """
  Multiplies two matrices (m_a and m_b) using NumPy and returns the resulting product matrix.

  Raises:
      TypeError: If m_a or m_b is not a list.
      ValueError: If m_a and m_b are empty, or cannot be multiplied (different inner dimensions).
  """

  # Check if m_a and m_b are lists
  if not isinstance(m_a, list) or not isinstance(m_b, list):
    raise TypeError("m_a and m_b must be lists")

  # Check if m_a and m_b are empty
  if not m_a or not m_b:
    raise ValueError("m_a and m_b can't be empty")

  # Convert lists to NumPy arrays for efficient multiplication
  try:
    m_a = np.array(m_a)
    m_b = np.array(m_b)
  except ValueError:
    raise TypeError("m_a and m_b elements must be convertible to NumPy arrays (numeric types)")

  # Check if matrices can be multiplied (inner dimensions compatible)
  if m_a.shape[1] != m_b.shape[0]:
    raise ValueError("m_a and m_b can't be multiplied (incompatible inner dimensions)")

  # Perform matrix multiplication using NumPy
  product_matrix = np.matmul(m_a, m_b)

  return product_matrix

# Test cases (same as 100-matrix_mul but with NumPy exceptions)
def test_lazy_matrix_mul():
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
  assert str(excinfo.value) == "m_a and m_b elements must be convertible to NumPy arrays (numeric types)"

  # Test 4: Valid multiplication (assuming other test cases from 100-matrix_mul are valid for NumPy conversion)
  m_a = [[1, 2], [3, 4]]
  m_b = [[1, 2], [3, 4]]
  product_matrix = lazy_matrix_mul(m_a, m_b)
  assert np.array_equal(product_matrix, [[7, 10], [15, 22]])

# You can use a testing framework like pytest to run the test cases

