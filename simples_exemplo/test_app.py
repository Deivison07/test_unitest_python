import unittest
from app import Main


class MainTest(unittest.TestCase):
    def setUp(self):
        #preencher com dados ou instancias que serão usadas para cada teste individualmente
        self.insta = Main()
        print(' --> Novo teste')
    
    def test_setNome(self):
        self.assertEqual(self.insta.setNome('Deivison'),'Deivison')
    
    def test_getNome(self):
        self.insta.setNome('Deivison')
        self.assertEqual(self.insta.getNome(),'Deivison')

if __name__ == '__main__':
    unittest.main()

