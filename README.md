# crypto_trade_trick

POC to levrage the difference in price between different crypto pairs

Exchange used: CoinDcx

The public APIs are used to get current market details.


#Example

Buy UNI using USDT and sell UNI in INR
The final INR value that you get after selling UNI will be more than what You used for buying USDT, considering all the transaction fees

#POC Result
There is a chance of profit, but it is very less.
To have significant profit:
1. The crypto should have large spread in the exchange
2. One needs to use a larger sum of money

#Future
1. Similar script can be written for different exchanges, every exchange will have different response in the API so the methods would need remodelling.
2. You can leverage out of this and place automated orders to your exchange using the APIs
