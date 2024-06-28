// 2-read_file.js
// Reads a CSV and logs number of students and details based on their fields

const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    if (students.length === 0) {
      console.log('Number of students: 0');
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
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
