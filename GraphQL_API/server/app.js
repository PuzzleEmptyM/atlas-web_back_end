const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const schema = require('./schema/schema');

const app = express();

app.use('/graphql', graphqlHTTP({
  schema: schema,
  graphiql: true, // Enable the GraphiQL interface
}));

app.listen(4000, () => {
  console.log('Now listening for requests on port 4000');
});
