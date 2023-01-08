from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget= forms.Textarea )


    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class':'form-control'})
    subject.widget.attrs.update({'class':'form-control'})
    message.widget.attrs.update({'class':'form-control'})