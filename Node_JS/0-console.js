// 0-console.js
// Prints a given string message to the standard output

const process = require('process');

function displayMessage(message) {
  process.stdout.write(message + '\n');
}

module.exports = displayMessage;
