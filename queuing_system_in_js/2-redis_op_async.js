import redis from 'redis';
import { promisify } from 'util';

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

const getAsync = promisify(client.get).bind(client);

// Function to set a new value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Async function to get and display a value from Redis
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.log(`Error: ${err}`);
  }
}

// Calling the functions as per the requirements
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();

process.stdin.resume();
