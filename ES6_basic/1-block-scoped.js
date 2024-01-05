export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    let task = true;  // Block-scoped, separate from the outer 'task'
    let task2 = false; // Block-scoped, separate from the outer 'task2'
  }

  return [task, task2]; // Always returns the outer scope variables
}
