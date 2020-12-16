from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def integer_8_length_validate(value):
    if len(str(value)) != 8:
        raise ValidationError(
            _('%(value)s length is not equal 8'),
            params={'value': value},
        )
def integer_4_length_validate(value):
    if len(str(value)) != 4:
        raise ValidationError(
            _('%(value)s length is not equal 4'),
            params={'value': value},
        )