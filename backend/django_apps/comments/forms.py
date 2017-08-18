from django import forms

class CommentForm(forms.Form):
    """Form to create comment object

    Atributes:
        content_type: characterfield for the type of content
        object_id : integer that represents the ID of the comment
        content: the actual text for the comment
    """
    content_type = forms.CharField(widget = forms.HiddenInput)
    object_id    = forms.IntegerField(widget = forms.HiddenInput)
    content = forms.CharField(label = '', widget = forms.Textarea)
