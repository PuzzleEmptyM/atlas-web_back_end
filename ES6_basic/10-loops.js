export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  let index = 0;

  for (const value of array) {
    newArray[index] = appendString + value;
    index += 1;
  }

  return newArray;
}
