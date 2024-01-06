export default function appendToEachArrayValue(array, appendString) {
  let newArray = [];
  let index = 0;

  for (const value of array) {
    newArray[index] = appendString + value;
    index++;
  }

  return newArray;
}
