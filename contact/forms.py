from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=5)
	email = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea)

#>>> from contact.forms import ContactForm
#>>> f = ContactForm()
#>>> print f
#HTML code
#>>> print f.as_ul()
#HTML list
#>>> print f.as_p()
#...
#>>> print f['subject']
#...
#>>> print f['message']
#...
#>>> f = ContactForm({'subject':'hello', 'email': 'test@test.com', 'message':'Hello World!'})
#>>> f.is_valid()
#True
#>>> f = ContactForm({'subject':'hello', 'email': 'test@test.com', 'message':''})
#>>> f.is_valid()
#False
#>>> f['message'].errors
#[u'This field is required.']
#>>>f.cleaned_date #dados convertidos para o tipo correto em python.


