const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  var stub = sinon.stub(Utils, 'calculateNumber').returns(10);
  var spy = sinon.spy(console, 'log');
  it('makes sure that the stub function returns 10', function () {
    sendPaymentRequestToApi(100, 20);
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spy.calledOnceWithExactly('The total is: 10')).to.be.true;
  })
});
