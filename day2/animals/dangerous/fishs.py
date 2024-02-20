class Fishs:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['carp', 'salmon', 'mandarin fish']
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
