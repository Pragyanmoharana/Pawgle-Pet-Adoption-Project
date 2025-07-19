from django.contrib import admin, messages
from .models import DonatePet, Pet

@admin.register(DonatePet)
class DonatePetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_type', 'breed', 'age', 'gender', 'contact', 'submitted_at', 'is_converted')
    list_filter = ('is_converted', 'pet_type', 'gender')
    actions = ['approve_and_convert']

    def approve_and_convert(self, request, queryset):
        count = 0
        for donation in queryset:
            if not donation.is_converted:
                try:
                    Pet.objects.create(
                        user=donation.user,
                        name=donation.name,
                        species=donation.pet_type,  # pet_type maps to Pet.species
                        gender=donation.gender,
                        age=donation.age,
                        description=donation.description,
                        image=donation.image,
                        is_approved=True
                    )
                    donation.is_converted = True
                    donation.save()
                    count += 1
                except Exception as e:
                    messages.error(request, f"Error converting {donation.name}: {e}")
        if count > 0:
            self.message_user(request, f"{count} pet(s) successfully converted!", messages.SUCCESS)
        else:
            self.message_user(request, "No pets were converted.", messages.WARNING)

    approve_and_convert.short_description = "✅ Approve & Convert to Pet"

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'gender', 'age', 'is_approved', 'user')
    list_filter = ('is_approved', 'species', 'gender')
