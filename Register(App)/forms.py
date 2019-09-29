from django import forms
from register.models import Profile,City
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password

CITIES = [
    ('hyderabad','Hyderabad'),
    ('vizag','Vizag',),
    ('bangalore','Bangalore'),
    ('delhi','Delhi'),
]
GENDER = [
    ('M','male'),
    ('F','female')
]

class ProfileForm(forms.Form):
    alpha = RegexValidator(r'^[a-zA-Z_]*$',"Name must be in characters only")
    phone_reg = RegexValidator(r'^[6-9]\d{9}$',"Enter valid mobile number")

    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'regform'}),validators=[alpha],max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(),validators=[alpha],max_length=50,required=True)
    email = forms.EmailField(widget=forms.EmailInput(),required=True, max_length=100)
    phone = forms.CharField(widget=forms.NumberInput(),validators=[phone_reg],required=True,max_length=10)
    gender = forms.ChoiceField(widget=forms.RadioSelect(),choices = GENDER,required=True)
    city = forms.ChoiceField(widget=forms.Select(attrs={}), required=True,choices=list(City.objects.all().values_list()))
    password = forms.CharField(widget=forms.PasswordInput(),required=True,min_length=8,max_length=16)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True,min_length=8,max_length=16)
    tandc = forms.BooleanField(widget=forms.CheckboxInput(),required=True)

    # class Meta:
    #     model = Profile
    #     fields = "__all__"


    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError("User already exists with this email")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if Profile.objects.filter(phone=phone).exists():
            raise forms.ValidationError("User already exists with this mobile number")
        return phone

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        MIN_LENGTH = 8
        MAX_LENGTH = 16
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password and Confirm password should be same")
            else:
                if len(password) < MIN_LENGTH:
                    raise forms.ValidationError("Password should have atleast %d charecters " % MIN_LENGTH)
                if len(password) > MAX_LENGTH:
                    raise forms.ValidationError("Password can contain a maximum of %d charecters only" % MIN_LENGTH)
                if password.isdigit() or password.isalpha() or password.isalnum():
                    print("pwd check")
                    raise forms.ValidationError("Password should be a combination of Alphabets,Numbers and Special characters")







    # alphanumeric = RegexValidator('^(\w+\d+|\d+\w+)+$')
    # numeric = RegexValidator('^(\d+)+$')
    # email_reg = RegexValidator("/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]{3,8}+(?:\.[a-zA-Z0-9-]+{2,4)*$/")
    #
    # first_name = forms.CharField(min_length=6,max_length=40,required=True,error_messages={'required': 'Please enter your name'})
    # last_name = forms.CharField(max_length=40,required=True,error_messages={'required': 'Please enter your last name'})
    # email = forms.EmailField(max_length=50,required=True,validators=[email_reg],error_messages={'required': 'Please enter valid email id'})
    # phone = forms.IntegerField(required=True,validators=[RegexValidator('^[6-9][0-9]{9}$/',message="Enter valid mobile number")])
    # gender = forms.RadioSelect(choices=GENDER)
    # city = forms.ChoiceField(choices=CITIES,required=True,widget=forms.Select(attrs={'required':'required'}),error_messages={'required': 'Please select a city'})
    # password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=8,max_length=16,validators=[alphanumeric],error_messages={'required': 'Password should be a combination of Alphabets and Numbers'})
    # confirm_password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=8,max_length=16,validators=[alphanumeric],error_messages={'required': 'Password should be a combination of Alphabets and Numbers'})
    # tandc = forms.BooleanField(required=True,error_messages={'required': 'You should accept terms and conditions'})


    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     is_exists = Profile.objects.filter(phone=phone).exists()
    #     if is_exists:
    #         raise forms.ValidationError("User already exists with this mobile number")
    #     return phone
    #
    # def clean(self):
    #     form_data = self.cleaned_data
    #     if form_data['password'] != form_data['confirm_password']:
    #         print("in")
    #         self._errors["password"] = ["Password do not match"]  # Will raise a error message
    #         del form_data['password']
    #     return form_data

    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     print(email)
    #     try:
    #         print("email try")
    #         mt = Profile.objects.get(email=email)
    #     except:
    #         print("email except")
    #         return self.cleaned_data["email"]
    #     raise forms.ValidationError("Email already exists")
    #     # return email

