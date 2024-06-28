// 1-stdin.js
// This program prompts the user to input their name and then displays it

console.log('Welcome to Holberton School, what is your name?');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (input) => {
  const name = input.trim();
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  process.stdin.pause();
});
