import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Call the method to get the data point
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    # Calculate the expected price based on the quotes
    expected_price = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price'])/2

    # Add the assertion
    self.assertEqual(price, expected_price)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Call the method to get the data point
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    # Calculate the expected price based on the quotes
    expected_price = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
    self.assertGreater(bid_price, ask_price)


  def test_getRatio(self):
    # Test case with non-zero price_b
    result = getRatio(10, 2)
    self.assertEqual(result, 5)

    # Test case with price_b equal to 0
    result = getRatio(10, 0)
    self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
