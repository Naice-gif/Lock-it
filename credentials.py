class Credents:
  """
  Class that generates new instances of credents
  """

  credes_list = []

   # Init method up here
  def save_creds(self):

        '''
        save_creds method saves credentials objects into creds_list
        '''

        Credents.credes_list.append(self)
   
  def __init__(self,username,password,account_name):

    #docstring removed for simplicity

    self.username = username
    self.password = password
    self.account_name = account_name

  def delete_creds(self):

        '''
        delete_creds method deletes a saved credentials from the creds_list
        '''
