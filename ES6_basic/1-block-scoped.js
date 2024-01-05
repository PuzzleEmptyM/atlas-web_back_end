export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    (function() {
      var task = true;  // This 'task' is scoped to the IIFE
      var task2 = false; // This 'task2' is scoped to the IIFE
    })();
  }

  return [task, task2]; // Always returns the outer scope variables
}
