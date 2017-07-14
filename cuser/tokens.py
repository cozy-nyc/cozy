from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """Creates tokens used for user activation.
    """
    def _make_hash_value(self, user, timestamp):
        """ This function generates hash values for tokens

        Creates hash by taking the text_type of a 'user' email(user.pk), time of request
            which is the 'timestamp' and the 'user.email_confirmed' variable which should be false.
        """
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()
