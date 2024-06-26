// testing for payment_token function
const sinon = require('sinon');
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a resolved promise object if true', function(done) {
    getPaymentTokenFromAPI(true).then(response => {
      expect(response).to.have.property('data', 'Successful response from the API');
      done();
    }).catch(err => done(err));
  })
})
