"""This is a module with functions removed from the view file"""

from our_post.models import Photo


def save_form_db(key, request, post_form) -> None:
    form_data = post_form.save(commit=False)
    form_data.userId = request.user
    post_form.cleaned_data
    form_data.save()
    #  збереження фотографій в базі даних
    for i in request.FILES.getlist(key):
        form_data.content.add(Photo.objects.create(photo=i))
    form_data.save()
    

        