# forms.py
from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "room_number"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full h-32 px-4 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            ),
            "room_number": forms.Select(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            ),
        }
        labels = {
            "title": "Judul Laporan",
            "description": "Deskripsi Laporan",
            "room_number": "Nomor Kamar",
        }
        help_texts = {
            "title": "Berikan judul laporanmu.",
            "description": "Berikan deskripsi lengkap tentang laporanmu.",
            "room_number": "Pilih nomor kamar Anda.",
        }
        error_messages = {
            "title": {
                "max_length": "This title is too long.",
            },
            "description": {
                "required": "Please provide a description.",
            },
            "room_number": {
                "required": "Please choose your room number.",
            },
        }
