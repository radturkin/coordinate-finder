import unittest

from grpc import StatusCode

from main import app

class flask_test(unittest.TestCase):

    def test1(self):
        pass

    def test_index(self):
        tester=app.test_client(self)
        response=tester.get("/")
        statuscode=response.status_code
        self.assertEqual(statuscode,200)




if __name__ == "__main__":
    unittest.main()
