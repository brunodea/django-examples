from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=5)
	email = forms.EmailField(required=False, label='Your email address')
	message = forms.CharField(widget=forms.Textarea)

	#validacao chamada depois da validacao padrao.
	#Django procura por metodos com nomes do tipo:
	#clean_nomedoatributo
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError('Not enough words!')
		return message

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


