from getresults_identifier import AlphanumericIdentifier

from .identifier_history import IdentifierHistory


class BaseIdentifier(AlphanumericIdentifier):

    history_model = IdentifierHistory

    def __init__(self):
        super(BaseIdentifier, self).__init__(self.last_identifier)

    @property
    def last_identifier(self):
        try:
            identifier_history = self.history_model.objects.filter(identifier_type=self.identifier_type).latest('id')
            last_identifier = identifier_history.identifier
        except self.history_model.DoesNotExist:
            last_identifier = None
        return last_identifier


class PatientIdentifier(BaseIdentifier):

    alpha_pattern = r'^[A-Z]{3}$'
    numeric_pattern = r'^[0-9]{9}$'
    seed = ('AAA', '000000000')
    identifier_type = 'patient'


class ReceiveIdentifier(BaseIdentifier):

    alpha_pattern = r'^[A-Z]{3}$'
    numeric_pattern = r'^[0-9]{4}$'
    seed = ('AAA', '0000')
    identifier_type = 'receive'
