from .models import WebsiteImages, Product, AdminInfo
from django import forms


class AdminInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = AdminInfo
        fields = [
            "email",
            "phonenumber",
            "address",
            "secondary_header",
            "header",
            "about",
            "logo",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "info", "image"]


class WebsiteImageUpdateForm(forms.ModelForm):
    class Meta:
        model = WebsiteImages
        fields = ["image"]
