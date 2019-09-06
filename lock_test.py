import unittest 
from locked import Lock

class TestLock(unittest.TestCase):

  def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_locked = Lock("ThineOrb","U0788347151?") 


  def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      self.assertEqual(self.new_locked.username,"ThineOrb")
      self.assertEqual(self.new_locked.password,"U0788347151?")

  def test_save_locks(self):
      '''
      test_save_locks test case to test if the Lock object is saved into
      the locker list
      '''
      self.new_locked.save_locks() 
      self.assertEqual(len(Lock.locker_list),1)

  def tearDown(self):
      '''
      tearDown method that does clean up after each test case has run.
      '''
      Lock.locker_list = []  


  def test_save_multiple_locks(self):
      '''
      test_save_multiple_locks to check if we can save multiple passwords
      objects to our locker_list
      '''
      self.new_locked.save_locks()
      test_locking = Lock("ThineOrb","U0788347151?")
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