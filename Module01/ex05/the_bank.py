class Account(object):

  ID_COUNT = 1

  def __init__(self, name, **kwargs):
    self.__dict__.update(kwargs)

    self.id = self.ID_COUNT
    Account.ID_COUNT += 1
    self.name = name
    if not hasattr(self, 'value'):
      self.value = 0

    if self.value < 0:
      raise AttributeError("Attribute value cannot be negative.")
    if not isinstance(self.name, str):
      raise AttributeError("Attribute name must be a str object.")

  def transfer(self, amount):
    self.value += amount

class Bank(object):
  """The bank"""

  def __init__(self):
    self.accounts = []

  def add(self, new_account):
    """ Add new_account in the Bank
    @new_account: Account() new account to append
    @return True if success, False if an error occured
    """
    # test if new_account is an Account() instance and if
    # it can be appended to the attribute accounts
    if not isinstance(new_account, Account):
      return False
    for account in self.accounts:
      if account.name == new_account.name:
        return False
    self.accounts.append(new_account)
    return True

  def transfer(self, origin, dest, amount):
    """ Perform the fund transfer
    @origin: str(name) of the first account
    @dest: str(name) of the destination account
    @amount: float(amount) amount to transfer
    @return True if success, False if an error occured
    """
    origin_account = None
    dest_account = None
    for account in self.accounts:
      if account.name == origin:
        origin_account = account
      if account.name == dest:
        dest_account = account

    if origin_account is None or dest_account is None:
      return False

    if self.__corrupt_account(origin_account) or self.__corrupt_account(dest_account):
      return False

    if amount < 0 or amount > origin_account.value:
      return False

    origin_account.transfer(-amount)
    dest_account.transfer(amount)
    return True

  def fix_account(self, name):
    """ fix account associated to name if corrupted
    @name: str(name) of the account
    @return True if success, False if an error occured
    """
    account_to_fix = None
    for account in self.accounts:
      if account.name == name:
        account_to_fix = account
        break

    if account_to_fix is None:
      return False

    if not hasattr(account_to_fix, 'value'):
      account_to_fix.value = 0
    if not hasattr(account_to_fix, 'id'):
      account_to_fix.id = Account.ID_COUNT
      Account.ID_COUNT += 1

    for attribute in account_to_fix.__dict__:
      if attribute.startswith('b'):
        delattr(account_to_fix, attribute)
      if attribute.startswith('zip') or attribute.startswith('addr'): # TODO check
        setattr(account_to_fix, 'zip_or_addr', getattr(account_to_fix, attribute))
        delattr(account_to_fix, attribute)

    return True



  def __corrupt_account(self, account):
    """ Check if account is corrupted
    @account: Account() account to check for corruption
    @return True if success, False if an error occured
    """

    if len(account.__dict__) % 2:
      return True

    zip_or_addr = False
    for attribute in account.__dict__:
      if attribute.startswith('b'):
        return True
      if attribute.startswith('zip') or attribute.startswith('addr'):
        zip_or_addr = True

    if not zip_or_addr:
      return True
    if not hasattr(account, 'name') or not hasattr(account, 'id') or not hasattr(account, 'value'):
      return True
    if not isinstance(account.name, str) or not isinstance(account.id, int) or not isinstance(account.value, (int, float)):
      return True

    return False

