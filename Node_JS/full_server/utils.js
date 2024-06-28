// full_server/utils.js
import fs from 'fs';
import path from 'path';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter(line => line.trim() !== '');
      const students = lines.slice(1); // Remove header

      const studentData = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!studentData[field]) {
          studentData[field] = [];
        }
        studentData[field].push(firstname);
      });

      resolve(studentData);
    });
  });
};
