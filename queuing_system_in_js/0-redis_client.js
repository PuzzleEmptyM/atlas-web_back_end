import { createClient } from 'redis';

console.log('Starting Redis client...');

const client = createClient({
  url: 'redis://127.0.0.1:6379'
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

client.connect().catch(err => {
  console.error('Failed to connect:', err.message);
});

process.stdin.resume();
