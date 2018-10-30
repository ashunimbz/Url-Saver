from authorize.models import Category,Url
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Div,Submit,HTML,Button,Row,Field,Fieldset
from crispy_forms.bootstrap import AppendedText ,PrependedText,FormActions


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']


    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'label_help_cls'

        self.helper.layout = Layout(

            Field('name',css_class='input '),
            FormActions(
                Submit('save_changes', 'Add Category', css_class="button-primary right ")
        )
        )


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields =['url','description']


    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'label_help_cls'

        self.helper.layout = Layout(

            Field('url',css_class='input'),
            Field('description',css_class='input',rows ='7'),
            FormActions(
                Submit('save_changes', 'Add Url', css_class="button-primary right ")
        )
        )


