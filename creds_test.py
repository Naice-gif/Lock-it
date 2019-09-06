import unittest 
from credentials import Credents

class Testcreds(unittest.TestCase):

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

  def test_save_credentil(self):
      '''
      test_save_credentil test case to test if the Credents object is saved into
      the creds list
      '''
      self.new_credent.save_credentil() 
      self.assertEqual(len(Credents.creds_list),1)

  def tearDown(self):
      '''
      tearDown method that does clean up after each test case has run.
      '''
      Credents.creds_list = []  


  def test_save_multiple_credentil(self):
      

      self.new_credent.save_credentil()
      test_locking = Credents("Naice","U0788347151*","Instagram" )
      test_locking.save_locks()
      self.assertEqual(len(Lock.locker_list),2)   


  def test_find_locker_by_name(self):
      '''
      test to check if we can find a contact by phone number and display information
      '''

      self.new_locked.save_locks()
      test_locking = Lock("ThineOrb","U0788347151?")
      test_locking.save_locks()

      found_locked = Lock.find_by_name("ThineOrb")

      self.assertEqual(found_locked.username,test_locking.username)


if __name__ == '__main__':
    unittest.main()