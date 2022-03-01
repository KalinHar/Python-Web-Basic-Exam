from django import forms

from myexam.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = Profile
        fields = ('Username', 'Email', 'Age')


class CreateAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f_name, field in self.fields.items():
            # field.label = f_name     # this is set field label = exact to value of model
            # if f_name == 'Genre':         # this is set initial value-'Other' in choicefield-'Genre'
            #     field.initial = 'Other'
            #     continue
            field.widget.attrs['placeholder'] = field.label  # this is equal to widgets code in class Meta

    class Meta:
        model = Album
        fields = ('Album_Name', 'Artist', 'Genre', 'Description', 'Image_URL', 'Price')
        # widgets = {
        #     'Album_Name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
        #     'Artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
        #     'Description': forms.Textarea(attrs={'placeholder': 'Description'}),
        #     'Image_URL': forms.TextInput(attrs={'placeholder': 'Image URL'}),
        #     'Price': forms.TextInput(attrs={'placeholder': 'Price'}),
        # }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('Album_Name', 'Artist', 'Genre', 'Description', 'Image_URL', 'Price')


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
