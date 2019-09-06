class credents:
  """
  Class that generates new instances of credents
  """

  credes_list = []

   # Init method up here
  def save_creds(self):

        '''
        save_creds method saves contact objects into contact_list
        '''

        Lock.locker_list.append(self)
   
  def __init__(self,username,password):

    #docstring removed for simplicity

    self.username = username
    self.password = password

  def delete_Locks(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
