"""A3. Tester for the function common_words in tweets.
"""

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    """Tester for the function common_words in tweets.
    """

    def test_empty(self):
        """Empty dictionary."""

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_four_word_limit_one(self):
        """Dictionary with four word to test accept one word. All keys has 
        different count numbers."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 1}
        arg2 = 1
        exp_arg1 = {'mind': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
        
    def test_four_word_limit_two(self):
        """Dictionary with four word to test accept two word. All keys has 
        different count numbers."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 1}
        arg2 = 2
        exp_arg1 = {'mind': 4, 'words': 3}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
        
    def test_four_word_limit_one_samely(self):
        """Dictionary with four word to test accept one word. There are two 
        keys which have same value locted at the largest values."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 4}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)   
    
    def test_four_word_limit_two_samely(self):
        """Dictionary with four word to test accept two word. There are two 
        keys which have same value locted at the largest values."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 4}
        arg2 = 2
        exp_arg1 = {'mind': 4, 'google': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)   
    
    def test_four_word_limit_one_samely_at_smaller(self):
        """Dictionary with four word to test accept one word. There are two 
        keys which have same value locted at the medium values."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 3}
        arg2 = 1
        exp_arg1 = {'mind': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)  
        
    def test_four_word_limit_two_samely_at_smaller(self):
        """Dictionary with four word to test accept two word. There are two 
        keys which have same value locted at the medium values."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 3}
        arg2 = 2
        exp_arg1 = {'mind': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)   
        
    def test_four_word_limit_three_samely_at_smaller(self):
        """Dictionary with four word to test accept three word. There are two 
        keys which have same value locted at the medium values."""
        
        arg1 = {'key': 2, 'words': 3, 'mind': 4, 'google': 3}
        arg2 = 3
        exp_arg1 = {'words': 3, 'mind': 4, 'google': 3}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)
