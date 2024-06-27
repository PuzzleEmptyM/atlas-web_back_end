import redis from 'redis';

console.log('Starting Redis client...');

const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('ready', () => {
  console.log('Redis client ready to use');
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('reconnecting', () => {
  console.log('Redis client reconnecting to the server');
});

client.on('end', () => {
  console.log('Redis client connection closed');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to get and display a value from Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

// Calling the functions as per the requirements
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

process.stdin.resume();
