// full_server/server.js
import express from 'express';
import path from 'path';
import router from './routes/index.js';

const app = express();
const port = 1245;

const dbFilePath = process.argv[2];
app.set('dbFilePath', dbFilePath);

app.use('/', router);

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

export default app;
