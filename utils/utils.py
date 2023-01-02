from rest_framework import serializers


class ChoiceField(serializers.ChoiceField):
    # Explain choice field customization bug:
    # https://github.com/encode/django-rest-framework/discussions/8586
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # support inserts with value
        if data == '' and self.allow_blank:
            return ''

        try:
            return self.choice_strings_to_values[str(data)]
        except KeyError:
            self.fail('invalid_choice', input=data)
