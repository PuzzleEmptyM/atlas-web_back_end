const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 7865;

app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const cartId = req.params.id;
  res.send('Payment methods for cart ' + cartId);
})

app.get('/available_payments', (req, res) => {
  const object = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  }
  res.json(object);
});

app.post('/login', (req, res) => {
  const { userName } = req.body;
  if (!userName) {
    return res.status(400).send('userName is required');
  }
  return res.status(200).send('Welcome ' + userName);
})

app.listen(port, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
