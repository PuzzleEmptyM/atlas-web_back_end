const request = require('request');
const expect = require('chai').expect;

describe('Test suite for the index page', function() {
  it('Checks if the status code is the same', function(done) {
    request('http://localhost:7865/', function(err, response) {
      expect(response.statusCode).to.equal(200);
      done();
    })
  })
  it('Checks if the body returns the correct result', function(done) {
    request('http://localhost:7865/', function(err, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    })
  })
  it('checks whatever "other" is...', function(done) {
    done();
  })
})

describe('Test suite for the cart page', function() {
  it('Checks if the status code is the same', function(done) {
    request('http://localhost:7865/cart/100', function(err, response) {
      expect(response.statusCode).to.equal(200);
      done();
    })
  })
  it('Checks if the status code is 404 on invalid request', function(done) {
    request('http://localhost:7865/cart/hi', function(err, response) {
      expect(response.statusCode).to.equal(404);
      done();
    })
  })
  it('checks if the body response is correct', function(done) {
    request('http://localhost:7865/cart/14', function(err, response, body) {
      expect(body).to.equal('Payment methods for cart 14')
      done();
    })
  })
})
