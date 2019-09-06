class Lock:
  """
  Class that generates new instances of locked
  """

  locker_list = []

   # Init method up here
  def save_locks(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Lock.locker_list.append(self)
   
  # def __init__(self,username,password):

  #   #docstring removed for simplicity

  #   self.username = username
  #   self.password = password

  # def delete_Locks(self):

  #       '''
  #       delete_contact method deletes a saved contact from the contact_list
  #       '''

  #       Lock.locker_list.remove(self) 


  # @classmethod
  # def find_by_name(cls,name):
  #     '''
  #     Method that takes in a number and returns a contact that matches that number.

  #     Args:
  #         number: Phone number to search for
  #       Returns :
  #           Contact of person that matches the number.
  #     '''

  #     for locked in cls.locker_list:
  #         if locked.username == name:
  #           return locked

  

    