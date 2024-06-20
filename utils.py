def calculate_average(numbers):
  """
  Calcule la moyenne d'une liste de nombres.

  Args:
    numbers: Une liste de nombres.

  Returns:
    La moyenne des nombres dans la liste ou 0 si la liste est vide.
  """
  if not numbers:
    return 0
  return sum(numbers) / len(numbers)