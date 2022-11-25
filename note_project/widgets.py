from django import forms

class DatePickerInput(forms.DateInput):
        input_type = 'date'
class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'
class MypasswordInput(form.PasswordInput):
        input_type='PasswordInput'