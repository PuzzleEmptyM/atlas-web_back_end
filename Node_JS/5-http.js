// 5-http.js
// Creates more complex HTTP server that responds with different messages

const http = require('http');
const fs = require('fs');
const url = require('url');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1); // Remove the header line

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

const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!\n');
    res.end();
  } else if (parsedUrl.pathname === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    countStudents(dbFilePath)
      .then((output) => {
        res.write(output);
        res.end();
      })
      .catch((error) => {
        res.write(error.message);
        res.end();
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.write('Not Found\n');
    res.end();
  }
});

const port = 1245;
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
