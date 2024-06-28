// 3-read_file_async.js
// Reads CSV file and logs number of students and details based on their fields

const fs = require('fs');

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
        console.log('Number of students: 0');
        resolve();
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

      console.log(`Number of students: ${students.length}`);
      for (const [field, count] of Object.entries(fieldCounts)) {
        const list = fieldLists[field].join(', ');
        console.log(`Number of students in ${field}: ${count}. List: ${list}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
