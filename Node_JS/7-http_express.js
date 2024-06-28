// 7-http_express.js
// Creates more complex HTTP server that responds with different messages

const express = require('express');
const fs = require('fs');

const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      if (students.length === 0) {
        resolve('Number of students: 0');
        return;
      }

      const fieldCounts = {};
      const fieldLists = {};

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');
        if (field) {
          if (!fieldCounts[field]) {
            fieldCounts[field] = 0;
            fieldLists[field] = [];
          }
          fieldCounts[field] += 1;
          fieldLists[field].push(firstname);
        }
      });

      let output = `Number of students: ${students.length}\n`;
      for (const [field, count] of Object.entries(fieldCounts)) {
        const list = fieldLists[field].join(', ');
        output += `Number of students in ${field}: ${count}. List: ${list}\n`;
      }

      resolve(output.trim());
    });
  });
}

const dbFilePath = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  if (!dbFilePath) {
    res.status(500).send('Database file path not provided');
    return;
  }

  countStudents(dbFilePath)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

const port = 1245;
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
