"""A3. Tester for the function extract_mentions in tweets.
"""

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    """Tester for the function extract_mentions in tweets.
    """

    def test_empty(self):
        """Empty tweet."""

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        """Non-empty tweet with no mentions."""

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_all_lowcase_mention(self):
        """Non-empty tweet with all lowcase mentions."""
        
        arg = '@many @cats extra @meow?!'
        actual = tweets.extract_mentions(arg)
        expected = ['many', 'cats', 'meow']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_lowcase_mention_mix_with_uppercase_mention(self):
        """Non-empty tweet with lowcase mentions mixed with uppercase 
        mentions."""
        
        arg = 'Hi @UofT do you like @cats @CATS #meowmeow'
        actual = tweets.extract_mentions(arg)
        expected = ['uoft', 'cats', 'cats']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
    
    def test_end_with_other_symbol_mentions(self):
        """Non-empty tweet which mention is end with the symble instead 
        of empty space."""
        
        arg = '@many @cats$extra @meow?!'
        actual = tweets.extract_mentions(arg)
        expected = ['many', 'cats', 'meow']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_only_symbol_in_mention(self):
        """Non-empty tweet which only have symbol in the mention."""
        
        arg = 'No valid mentions @! here?'
        actual = tweets.extract_mentions(arg)
        expected = []        
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        


if __name__ == '__main__':
    unittest.main(exit=False)
