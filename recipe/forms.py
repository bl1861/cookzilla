from django import forms

class RecipeForm(forms.Form):
    recipe_title = forms.CharField(label="recipe_title", max_length=50)
    recipe_content = forms.CharField(label="recipe_content")
    # recipe_servings = forms.CharField(label="recipe_servings", max_length=300)
    recipe_servings = forms.IntegerField()

    iname1 = forms.CharField(label="iname1", max_length=50)
    # quantity1 = forms.CharField(label="quantity1", max_length=50)
    quantity1 = forms.IntegerField()
    unit1 = forms.CharField(label="unit1", max_length=50)

    iname2 = forms.CharField(label="iname2", max_length=50,required=False)
    # quantity2 = forms.CharField(label="quantity2", max_length=50)
    quantity2 = forms.IntegerField(required=False)
    unit2 = forms.CharField(label="unit2", max_length=50, required=False)

    iname3 = forms.CharField(label="iname3", max_length=50, required=False)
    # quantity3 = forms.CharField(label="quantity3", max_length=50)
    quantity3 = forms.IntegerField(required=False)
    unit3 = forms.CharField(label="unit3", max_length=50, required=False)

    OPTIONS = [
        ('1', 'Cake'),
        ('2', 'Bread'),
        ('3', 'Itali food'),
        ('4', 'Chinese food'),
        ('5', 'Korea food')
    ]

    tags = forms.MultipleChoiceField(label="tags", required=False, widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    recipe_photo = forms.FileField(required=False)

