/**
 * Function to perform mathematical operations on two rounded numbers.
 * @param {string} type - The type of operation: 'SUM', 'SUBTRACT', or 'DIVIDE'.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number|string} The result of the operation, or 'Error' if division by zero.
 */
function calculateNumber(type, a, b) {
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  switch (type) {
    case 'SUM':
      return roundedA + roundedB;
    case 'SUBTRACT':
      return roundedA - roundedB;
    case 'DIVIDE':
      if (roundedB === 0) {
        return 'Error';
      }
      return roundedA / roundedB;
    default:
      throw new Error('Invalid type');
  }
}

export default calculateNumber;
