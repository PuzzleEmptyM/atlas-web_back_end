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
