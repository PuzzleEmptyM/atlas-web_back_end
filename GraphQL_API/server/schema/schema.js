const {
  GraphQLObjectType,
  GraphQLString,
  GraphQLInt,
  GraphQLSchema,
} = require('graphql');

// Define TaskType
const TaskType = new GraphQLObjectType({
  name: 'Task',
  fields: () => ({
    id: { type: GraphQLString },
    title: { type: GraphQLString },
    weight: { type: GraphQLInt },
    description: { type: GraphQLString },
  }),
});

// Define RootQuery
const RootQuery = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    task: {
      type: TaskType,
      args: { id: { type: GraphQLString } },
      resolve(parent, args) {
        // This is where you would get the data from a data source
        // For now, returning a static example task
        return {
          id: args.id,
          title: 'Example Task',
          weight: 10,
          description: 'This is an example task description',
        };
      },
    },
  },
});

module.exports = new GraphQLSchema({
  query: RootQuery,
});
