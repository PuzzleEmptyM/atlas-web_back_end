// full_server/controllers/StudentsController.js
import { readDatabase } from '../utils.js';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const dbFilePath = req.app.get('dbFilePath');
    try {
      const data = await readDatabase(dbFilePath);
      const sortedFields = Object.keys(data).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));

      let response = 'This is the list of our students\n';
      sortedFields.forEach(field => {
        response += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const dbFilePath = req.app.get('dbFilePath');

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const data = await readDatabase(dbFilePath);
      const students = data[major];

      if (!students) {
        res.status(500).send('Cannot load the database');
        return;
      }

      const response = `List: ${students.join(', ')}`;
      res.status(200).send(response);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
