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

// Function to store hash values in Redis
function createHolbertonSchools() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Function to display the hash values from Redis
function displayHolbertonSchools() {
  client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) {
      console.log(`Error: ${err}`);
    } else {
      console.log(obj);
    }
  });
}

// Calling the functions as per the requirements
createHolbertonSchools();
displayHolbertonSchools();
