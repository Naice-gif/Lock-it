import unittest 
from credentials import Credents

class TestCredents(unittest.TestCase):

  def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_credent = Credents("Naice","U0788347151*","Instagram") 


  def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      self.assertEqual(self.new_credent.username,"Naice")
      self.assertEqual(self.new_credent.password,"U0788347151*")
      self.assertEqual(self.new_credent.account_name,"Instagram")

  def test_save_creds(self):
      '''
      test_save_creds test case to test if the Credents object is saved into
      the creds list
      '''
      self.new_credent.save_creds() 
      self.assertEqual(len(Credents.credes_list),1)

  def tearDown(self):
      '''
      tearDown method that does clean up after each test case has run.
      '''
      Credents.credes_list = []  


  def test_save_multiple_creds(self):
      

      self.new_credent.save_creds()
      test_crede = Credents("Naice","U0788347151*","Instagram" )
      test_crede.save_creds()
      self.assertEqual(len(Credents.credes_list),2)   


  def test_find_credentials_by_user(self):
      

      self.new_credent.save_creds()
      test_crede = Credents("Naice","U0788347151*","Instagram" )
      test_crede.save_creds()

      found_credent = Credents.find_by_user("Naice")

      self.assertEqual(found_credent.username,test_crede.username)


if __name__ == '__main__':
    unittest.main()