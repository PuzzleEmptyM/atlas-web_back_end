const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {
  var spy;
  beforeEach(function() {
    spy = sinon.spy(console, 'log');
  })
  afterEach(function() {
    spy.restore();
  })
  it('makes sure that the console logs 120', function () {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnceWithExactly('The total is: 120')).to.be.true;
  })
  it('makes sure that the console logs 20', function () {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledOnceWithExactly('The total is: 20')).to.be.true;
  })
});
