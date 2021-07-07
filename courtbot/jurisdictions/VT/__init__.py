import re, os
import courtbot
from wtforms import ValidationError


CASE_ID_REGEX = re.compile('^\s*((?P<court>\w{4})-(?P<year>\d{2})-(?P<case>\d{6}))\s*$')


def validate_court_case(form, field):
    m = CASE_ID_REGEX.match(field.data.upper())
    if not m:
        raise ValidationError('Invalid format for case id.  Case ids will look like: <em>JP13-21-012345</em>')
    if not m.group('court') == 'JP13':
        raise ValidationError('We are only registering court case that begin with JP13 at this time.')


REQUIRED_FIELDS = {
    'case_id': ('Case Number <small>(ex: JP13-20-567890)</small>', validate_court_case),
    # cellphone is automatically included
}
REMINDER_MESSAGE = '''Hello!  You're hearing is tomorrow at {when} and will be held at {location}; {judge} presiding.  Please remember to bring your id, and arrive early.'''


bot = courtbot.state('VT', REQUIRED_FIELDS)


@bot.get_case_callback
def get_case(*, case_id):
    return {}


@bot.registration_callback
def registration_reminder(*, case_id, cellnumber):
    return {}


@bot.cron_callback
def cron(*, case):
    # TODO: fetch the case, compare the courtdate to the saved courtdate
    # TODO: what do we do when the docket indicates multiple hearings?
    pass
